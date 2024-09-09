# Deploy on EVE-NG
## 0. はじめに
CitrixのCitrix ADC VPX製品について記載していきます。  
本製品はL4,L7ロードバランサ、SSLオフロード、コンテンツスイッチなどの機能があります。  
VPXは仮想イメージのため、パイパーバイザ上であれば問題なく、専用アプライアンス・汎用サーバ・AWS/Azure/GCP等のクラウド上に建てることができます。  
専用アプライアンスは廃止になる噂もあり、最近は汎用サーバorクラウド上に構築するのが前提になってきているように見えます。

<br><br>

## 1. 初期セットアップ
今回はEVE-NG上で構築しました。（EVE-NG上にVPXを建てるところは他ノードと同様のため省略）  
構成は以下の様なワンアーム構成でHAを組み、E2Eでトラフィックを流すところまで進めます。  

![topo1](images/image-33.png)  

<br>
<br>
<details><summary>sw preconfig</summary>

```
##cisco sw
conf t
vlan 10,20
int ra e0/0-1
 switchport trunk allowed vlan 1,10,20
 switchport mode trunk
int e0/2
 switchport access vlan 10
 switchport mode access
int e0/3
 switchport access vlan 20
 switchport mode access
end
```

</details>  
<br>
<br>

起動後、コンソール接続し、**ID:nsroot / PW:nsroot**でログイン。初回ログイン時は新しいパスワード入力を求められるので設定します。

![init_password](images/image.png)  

初期設定では、管理IPが**192.168.100.1**になっています。  
今回の外部NWは**192.168.10.0/24**のため、設定を変更します。  
(EVE-NGのnetworkオブジェクトにあるManagement(Cloud0)が物理NICの所属するNWに繋がっています)  


![change_mgmt_ip](images/image-3.png)  

設定後、再起動します。  
立ち上がってきたらブラウザから設定したIPにアクセスします。

![login_page](images/image-4.png)  

初期設定のウィザードが表示されるので、順番に設定していきます。

![wizard1](images/image-5.png)  

VPXには3種類のIPがあります。  
このウィザードではsnipを設定するので、上記トポロジのvlan10,20のIPを設定します。
| IP | Description |
| ---- | ---- |
| nsip | 管理用のIP |
| snip | インターフェースのIP |
| vip | クライアント側からアクセスするIP |
  
<br>

![config_nsip](images/image-9.png)  
  
次にホスト名などの設定を行います。

![wizard2](images/image-11.png)  


![alt text](images/image-10.png)  

<br><br>

## 2. HAの設定
HA Monitoring / HA Heartbeatの処理を行うインターフェースを指定します。  
デフォルトで有効かつ今回は1/1のみでHAパケットをやり取りしたいので、それ以外のインターフェースでOFFにします。  

```System > Network > Interfaces```

![select_if1](images/image-12.png)  
![if_config1](images/image-13.png)  


次にHAの対向機器を設定します。  
Remote Node IP Addressに対向HA機器の管理IP、Remote System Login Credential
に対向HA機器のクレデンシャルを入力します。  
この設定は片系のみで問題ありません。

```System > High Availability > Nodes```

![ha1](images/image-14.png)  
![ha2](images/image-15.png)  

設定後、画面更新をするとNODE STATEがUPになり、HAが組めていることが確認できます。  

![ha3](images/image-16.png)  

今回はホスト名がvpx1のノードをprimaryにして進めようと思いますので、右クリックからForce failoverをします。

![ha4](images/image-17.png)  
![ha5](images/image-18.png)  
![ha6](images/image-19.png)  

vpxのHA heartbeatはvlan1, UDP3003でやり取りされます。  
fwを経由していたり、aclがある場合は注意しましょう。
![ha7](images/image-20.png)  

<br><br>

## 3. networkの設定
通信用のVLANインターフェースを作成します。  
vlan10,vlan20分を作成し、先程作成したsnipを紐づけます。

![vlan1](images/image-21.png)  
![vlan2](images/image-22.png)  
![vlan3](images/image-24.png)  
![vlan4](images/image-23.png)  

この時点でclient/serverからvpxまでpingが到達するはずです。
![ping1](images/image-2.png)  
![ping2](images/image-25.png)  

<br><br>

## 4. vServerの設定
vServerの設定では、クライアントがアクセスする、VPXが持つサーバの仮想IP(vip)を設定します。 
vipはclient側でルーティングを考慮しなくても良いように、snipと同セグメントで設定します。
また、今回はSSLオフロードはせず、クライアント-VPX間をHTTPで受け、ロードバランスする設定にしています。

```Traffic Management > Load Balancing > Virtual Servers```

![vs1](images/image-26.png)  
![vs2](images/image-31.png)  

<br><br>

## 5. Server, Serviceの設定
vServerにサーバ情報を紐づけていないため、まだ通信は通りません。  
次はServerの設定をしていきます。  
IPAddressにはロードバランス先の実際のサーバのIPを設定します。

```Traffic Management > Load Balancing > Servers```

![sv1](images/image-27.png)  
![sv2](images/image-29.png)  


次に上記で定義したServerをServiceに紐づけます。  
Serviceはデフォルトでsnipから設定したServerのIPへTCPを使用したヘルスチェックを行います。  
今回は、serverでport8080でhttpを受け付けるようにしますので、service側も同様に8080で設定します。  
Server側でpythonの簡易web serverを実行。
```
python3 -m http.server 8080
```
VPXに戻り、serviceを設定。
```Traffic Management > Load Balancing > Services```

![service1](images/image-30.png)  
![service2](images/image-39.png)  
![service3](images/image-32.png)  

Serviceの設定が完了したら、次は再度vServerの設定に戻ります。  
Services and Service Groupsで定義したServiceを紐づけます。  
設定後、紐づくServiceがUPになっているため、vServer自体もSTATEがUPになります。  

```Traffic Management > Load Balancing > Virtual Servers```

![vs3](images/image-28.png)  
![vs4](images/image-34.png)  
![vs5](images/image-35.png)  
![vs6](images/image-36.png)  
![vs8](images/image-38.png)  

<br><br>

## 6. 確認
設定が完了したので、clientからport8080でhttpアクセスをしてみましょう。  
キャプチャはVPXとSWの間で取っていますので、client-VPX / VPX-server 間の両方を確認できます。

![http1](images/image-37.png)  
![http2](images/image-40.png)  
