# mii VPM Repository

miiが公開するVRChat向けツールのVPMリポジトリです。

- [配布ページ・Add to VCC](https://vpm.mii.dev/)
- リポジトリURL: `https://vpm.mii.dev/index.json`
- 作者: [mii](https://github.com/mii443) / mii@mii.dev

## 導入

VCCの **Settings → Packages → Add Repository** に上記のリポジトリURLを入力してください。ALCOMでは **パッケージ管理 → VPMリポジトリを追加** から登録できます。

プロジェクトのパッケージ管理画面から **VRCLens MA Installer** を追加します。

Modular Avatar / NDMFの配布元も登録してください: `https://vpm.nadena.dev/vpm.json`。

## 配布パッケージ

| パッケージ | ID | 説明 |
| --- | --- | --- |
| [VRCLens MA Installer](https://github.com/mii443/vrclens-ma-installer) | `dev.mii.vrclens-ma-installer` | アバター直下でVRCLensを設定し、NDMFビルド時に非破壊で導入します。 |

VRCLens 1.10.0本体と、任意のVRCLens_Customは別途購入・インポートが必要です。このリポジトリと配布ZIPには、Shinano・VRCLens・VRCLens_Custom等の有料アセット本体のコード・Prefab・画像・アニメーション等を含めません。

本ツールはVRCLens / Modular Avatarの非公式アダプターです。詳しい使用方法と対応範囲は[パッケージのREADME](https://github.com/mii443/vrclens-ma-installer/blob/main/README.md)を参照してください。

## 更新を公開するには

1. [Installer専用リポジトリ](https://github.com/mii443/vrclens-ma-installer)でコードを管理します。`package.json`の`version`と`url`を更新し、CHANGELOGに変更内容を記載してpushします。
2. 専用リポジトリの **Actions → Build Release → Run workflow** を実行します。許可リストにある独自ファイルだけを含むZIPが生成され、`v<version>`タグのGitHub Releaseとして公開されます。詳細は専用リポジトリのREADMEを参照してください。
3. このリポジトリの`source.json`の該当パッケージの`releases`配列へ、公開されたZIPのURLを追加してpushします。既存バージョンのURLは残してください。
4. **Actions → Build Repo Listing** の成功を確認します。成功するとGitHub Pagesの一覧JSONと配布ページが更新されます。手動のRun workflowでも再生成できます。

公開後の同じバージョンのZIPは差し替えず、変更時はバージョンを上げてください。過去のReleaseとZIPは、既存プロジェクトがそのバージョンを復元するために保持します。GitHubの自動生成するSource code ZIPはVPMパッケージとして使用しません。

## 構成

このリポジトリは配布一覧・Webページを管理します。Installerのソース・Releaseは専用リポジトリで管理し、0.1.1のReleaseは互換性のため本リポジトリに残します。`Packages/`内の説明書は、旧バージョンからのリンク用です。

配布ページの生成には[VRChat公式のPackage Listing Template](https://github.com/vrchat-community/template-package-listing)を使用しています。GitHub PagesのSourceは **GitHub Actions**、カスタムドメインは`vpm.mii.dev`、HTTPSを有効にしています。
