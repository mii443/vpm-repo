"""Build an allowlisted source-only package. Never export Unity dependencies."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

PROJECT = Path(__file__).resolve().parents[1]
PACKAGE = PROJECT / "Packages/dev.mii.vrclens-ma-installer"
FILES = [
    "package.json", "README.md", "LICENSE.md", "CHANGELOG.md",
    "Runtime/VRCLensInstaller.cs", "Runtime/VRCLensMAInstaller.Runtime.asmdef",
    "Editor/InstalledVRCLens.cs", "Editor/AssetGraph.cs", "Editor/InstallerBuild.cs",
    "Editor/InstallerEditor.cs", "Editor/EarlyFavoritesCompatibility.cs", "Editor/VRCLensMAInstaller.Editor.asmdef",
    "Editor/CustomizationMenuRouting.cs", "Editor/LyraIntegration.cs",
    "Prefabs/VRCLens MA Installer.prefab",
]


def main():
    paths = list(FILES)
    paths += [path + ".meta" for path in FILES]
    paths += ["Runtime.meta", "Editor.meta", "Prefabs.meta"]
    for path in paths:
        source = PACKAGE / path
        if not source.is_file() or source.is_symlink():
            raise RuntimeError(f"Missing or unsafe release file: {source}")
    own_guids = set()
    for path in paths:
        if path.endswith(".meta"):
            own_guids.update(re.findall(r"guid: ([0-9a-f]{32})", (PACKAGE / path).read_text(encoding="utf-8")))
    prefab = (PACKAGE / "Prefabs/VRCLens MA Installer.prefab").read_text(encoding="utf-8")
    foreign = set(re.findall(r"guid: ([0-9a-f]{32})", prefab)) - own_guids - {"0" * 32}
    if foreign or "setupObject: {fileID: 0}" not in prefab:
        raise RuntimeError("The distribution prefab must not reference vendor assets or a populated setup.")
    metadata = json.loads((PACKAGE / "package.json").read_text(encoding="utf-8"))
    name, version = metadata["name"], metadata["version"]
    if name != PACKAGE.name or not re.fullmatch(r"[a-z0-9.-]+", name) or not re.fullmatch(r"[0-9A-Za-z.+-]+", version):
        raise RuntimeError("Package identity and directory must match, with safe name/version characters.")
    output = PROJECT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / f"{name}-{version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(paths):
            bundle.write(PACKAGE / path, path)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    archive.with_suffix(".files.txt").write_text("\n".join(sorted(paths)) + "\n", encoding="utf-8")
    print(f"Created {archive} ({archive.stat().st_size} bytes, {len(paths)} files)")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
