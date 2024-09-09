# Deploy EVE-NG
## 0. はじめに
前回構築したproxmox上にEVE-NGのVMを建てます。  
私は主にCCIE用に使用しており、メモリを50GB程度割り振ればDNACを除いたフルラボ構成で十分使用できるかと思います。  
また、IOS以外にもJuniperやfortinet等の各種ベンダOSが動作するので、普段の業務での確認にも使いやすいかと思います。  

<br><br>

## 1. ISOダウンロード

ここからeve-ngのISOイメージをダウンロードします。

[https://www.eve-ng.net/index.php/download/](https://www.eve-ng.net/index.php/download/)
  ![](images/image-35-1024x577.png)

<br><br>

## 2. Proxmox上でVMを作成

次にproxmox側で管理画面右上の「VMを作成」をクリックし、VMを作成します。

  ![](images/image-25-1024x239.png)

VMの名前を入力します。

  ![](images/image-27.png)

ダウンロードしてきたISOイメージを選択します。

  ![](images/image-28.png)

管理画面上から リモートでVMをshutdownできるように、Qemuエージェントを追加します。

  ![](images/image-29.png)

VMが使用するストレージとサイズを選択します。

  ![](images/image-30.png)

使用するCPUのコア数を選択します。  
また、EVE-NGではネストされた仮想環境になるので種別をhostにします。

  ![](images/image-31.png)

使用するメモリサイズを指定します。

  ![](images/image-32.png)

ネットワークの設定はデフォルトのブリッジを使用します。

  ![](images/image-33.png)

nested virtualizationを有効にします。  
proxmoxホスト上で、シェルを開きます。

  ![](images/image-47-1024x267.png)

シェル上で、以下コマンドでnestedが有効かどうか確認します。デフォルトで有効だと思います。

・Intel CPUの場合(有効ならY)
```
cat /sys/module/kvm_intel/parameters/nested
```

・amd CPUの場合(有効なら1)
```
cat /sys/module/kvm_amd/parameters/nested
```

以下コマンドでcpu typeを固定します。vmidはproxmox管理画面上のVM名の左に記載されている番号になります。

```
qm set <vmid> --cpu host
```

  ![](images/image-49.png)

<br><br>

## 3. EVE-NGのインストール

作成したVMを起動し、EVE-NGのインストールを進めていきます。

  ![](images/image-34-1024x422.png)

デフォルトのままDone。

  ![](images/image-36-1024x765.png)

VM作成時にブリッジを選択しているので、今回はproxmoxと同セグメントにします。

  ![](images/image-37-1024x779.png)

今回はproxyを使用しないので、そのままDone。

  ![](images/image-38.png)

Continueを選択。

  ![](images/image-39.png)

Install completeとなったら、proxmox上で作成したVMのISOドライブを解除します。  
CD/DVDドライブをダブルクリックし、メディアを使用しないを選択。

  ![](images/image-55.png)
  ![](images/image-45.png)

VMに戻り、Reboot Nowで再起動します。

  ![](images/image-40-1024x779.png)

再起動後、root/eveでログインします。  
初期ログイン後はsetup画面が表示されます。

  ![](images/image-50-1024x449.png)

eve-ngに実際にログインするIPを設定します。  
今回はDHCPにしますが、固定で振りたい場合はstaticを選択します。

  ![](images/image-51.png)

proxyを使用しないのでdirect connectionにします。

  ![](images/image-52.png)

設定完了後、起動するとhttp://<設定したIP>/ が表示されるので、ブラウザに入力しログイン。

  ![](images/image-53.png)

admin/eveでログインできます。

  ![](images/image-54.png)

このままだと、proxmox上からshutdownが出来ないので、eve-ngのCLI上でqemu-guest-agentをインストールします。  

```
apt update
apt install qemu-guest-agent
```

以上になります。
