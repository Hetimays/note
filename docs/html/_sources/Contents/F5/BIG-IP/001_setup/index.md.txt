# 0. はじめに
BIG-IPをEVE-NG上に構築します。  
細かい機能確認等は他サイト様が詳しく載せているのでそちらを参照。  
情報が無いもの、バージョン差分で動作が変わっているものについては更新するかもしれません。  

<br><br>

# 1. 初期セットアップ
まずはイメージファイルをダウンロードします。  
[https://my.f5.com/manage/s/downloads](https://my.f5.com/manage/s/downloads)  
BIG-IPのVirtual Editionを選択します。Product Versionはlatest想定で進めます。  
![f5_1](images/image.png)  

Select a product containerから **[latest-version]_Virtual-Edition** を選択、  
Select a download fileから **BIGIP-[latest-version].ALL.qcow2.zip** を選択。  
画面下部で選択情報とdownload locationを確認し、ダウンロードします。  
![f5_2](images/image-1.png)

ダウンロード後、以下リンクからイメージをEVE-NGに追加します。  
[eve-ng install big-ip images/image](https://www.eve-ng.net/index.php/documentation/howtos/howto-add-f5-bigip/)  

ノードを追加後、デフォルトではvCPUが **1** 、RAMが **2048MB** になっています。  
F5の提示するリソース要件に合わせて変更します。  
また、EVE-NG側のBIG-IPのノード追加要件にConsole設定は **VNC** とあるので、併せて変更します。
[https://my.f5.com/manage/s/article/K15796](https://my.f5.com/manage/s/article/K15796)  
![eve-ng](images/image-2.png)  

MgmtインターフェースはDHCPサーバのあるネットワークに接続し、ノードを起動します。
![eve-ng](images/image-3.png)  

初期CLIログイン時のクレデンシャルは、**root** / **default**です。  
ログイン後、パスワード変更が求められるので設定します。  
![bigip](images/image-4.png)

mgmtインターフェースはデフォルトでDHCPクライアント設定になっているので、以下コマンドで払い出されたIPを確認します。
```ifconfig mgmt```
![bigip](images/image-5.png)

ブラウザからBIG-IPに払い出されたIPにアクセスします。  
クレデンシャルは **admin** / **<CLIで設定したパスワード>** です。  
初回GUIログイン時は再度パスワード変更が求められるので設定します。  
```https://<big-ip_mgmt-ip>```
![bigip](images/image-6.png)
![bigip](images/image-7.png)

初回ログイン後、ライセンス登録をします。  
左側ペインからLicenseを選択し、Base Registration Keyにライセンスキーを入力します。  
![bigip](images/image-8.png)  

アクティベート後に自動構成があり、完了するとライセンスが適用されていることが確認できます。  
![bigip](images/image-9.png)
