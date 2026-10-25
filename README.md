# mii VPM Repository

miiが公開するVRChat向けツールのVPMリポジトリです。

- [配布ページ・Add to VCC](https://mii443.github.io/vpm-repo/)
- リポジトリURL: `https://mii443.github.io/vpm-repo/index.json`
- 作者: [mii](https://github.com/mii443) / mii@mii.dev

## 導入

VCCの **Settings → Packages → Add Repository** に上記のリポジトリURLを入力してください。ALCOMでは **パッケージ管理 → VPMリポジトリを追加** から登録できます。

プロジェクトのパッケージ管理画面から **VRCLens MA Installer** を追加します。

Modular Avatar / NDMFの配布元も登録してください: `https://vpm.nadena.dev/vpm.json`。

## 配布パッケージ

| パッケージ | ID | 説明 |
| --- | --- | --- |
| [VRCLens MA Installer](Packages/dev.mii.vrclens-ma-installer/README.md) | `dev.mii.vrclens-ma-installer` | アバター直下でVRCLensを設定し、NDMFビルド時に非破壊で導入します。 |

VRCLens 1.10.0本体と、任意のVRCLens_Customは別途購入・インポートが必要です。このリポジトリと配布ZIPには、有料アセット本体のコード・Prefab・画像・アニメーション等を含めません。

本ツールはVRCLens / Modular Avatarの非公式アダプターです。詳しい使用方法と対応範囲は[パッケージのREADME](Packages/dev.mii.vrclens-ma-installer/README.md)を参照してください。

## 更新を公開するには

1. `Packages/dev.mii.vrclens-ma-installer/package.json`の`version`と`url`を更新し、CHANGELOGに変更内容を記載します。
2. このリポジトリのルートで `python Tools/build_release.py` を実行します。許可リストにあるファイルだけを含むZIPとSHA-256ファイルが`dist/`に生成されます。
3. パッケージのソース変更をコミット・pushします。
4. GitHub Releasesで`vrclens-ma-installer-v<version>`タグのReleaseを公開し、生成されたZIPと`.zip.sha256`を添付します。GitHubの自動生成するSource code ZIPはVPMパッケージとして使用しません。
5. `source.json`の該当パッケージの`releases`配列へ、新しいZIPのURLを追加してpushします。既存バージョンのURLは残してください。
6. **Actions → Build Repo Listing** の成功を確認します。成功するとGitHub Pagesの一覧JSONと配布ページが更新されます。手動のRun workflowでも再生成できます。

公開後の同じバージョンのZIPは差し替えず、変更時はバージョンを上げてください。過去のReleaseとZIPは、既存プロジェクトがそのバージョンを復元するために保持します。

Unityの開発プロジェクトは別の場所で管理し、このリポジトリへは公開対象の独自ファイルだけを同期してください。Include Dependencies付きのUnity Exportは使用しません。

## 構成

配布ページの生成には[VRChat公式のPackage Listing Template](https://github.com/vrchat-community/template-package-listing)を使用しています。GitHub PagesのSourceは **GitHub Actions** です。
