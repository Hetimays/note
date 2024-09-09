# SSL Offloading
## 0. はじめに
前回は、HTTPのみのロードバランス構成を試しました。
今回は、自己証明書の作成とSSLオフロードの動きを確認します。

<br><br>

## 1. 自己証明書の作成
SSL通信用に自己証明書を用意します。  
今回はルート証明書とそれで署名したサーバ証明書を作成します。  

### ルートCA用の秘密鍵の生成
```
openssl genrsa -out ROOTCA.key 2048
```

### ルートCA用の証明書作成
```
openssl req -x509 -new -nodes -key ROOTCA.key -sha256 -days 2000 -subj /CN=TEST_ROOTCA -out ROOTCA.pem
```

### サーバ証明書用の秘密鍵の生成
```
openssl genrsa -out SERVER.key 2048
```

### サーバ証明書用のCSRの生成
内容は何でも良いのですが、CNだけTEST_SERVERに、他はデフォルトで生成しました。
```
openssl req -new -key SERVER.key -sha256 -out SERVER.csr
```
![csr1](images/image.png)

### サーバ証明書の生成
```
openssl x509 -req -in SERVER.csr -CA ROOTCA.pem -CAkey ROOTCA.key -CAcreateserial -out SERVER.crt -days 2000 -sha256
```

<br><br>

## 2. VPXの設定
VPXでは使用する機能を個別で有効にする必要がありますので、SSLオフロード機能を有効にします。  
```System > Settings```  

![ssl9](images/image-9.png)

次に１で作成したサーバ証明書・鍵 (SERVER.crt, SERVER.key) をVPX内にアップロードします。  
```Traffic Management > SSL```  

![ssl1](images/image-1.png)
![ssl2](images/image-2.png)
  
vServerと証明書を紐付ける際に使用する証明書ペアを定義します。  
```Traffic Management > SSL > Certificates > Server Certificates```  

![ssl3](images/image-3.png)
![ssl4](images/image-4.png)

新しくvServerwを定義します。プロトコルはSSLにします。
```Traffic Management > Load Balancing > Virtual Servers```  

![ssl5](images/image-5.png)
![ssl6](images/image-6.png)

vServerの設定で、前回作成したServiceを紐づけます。  
![ssl7](images/image-7.png)

続いて、先程設定した証明書ペアを指定します。
![ssl8](images/image-8.png)

VPXの設定はこれで完了なので、web serverを立ち上げましょう。  
vServerがUPするはずです。  
```python3 -m http.server 8080```

![ssl10](images/image-10.png)

<br><br>

## 3. 確認
それではクライアントからHTTPSでサーバにアクセスします。  
クライアントーVPX間がSSL、VPX-サーバ間がHTTPで通信していることが確認できました。  

![client2](images/image-12.png)
![client1](images/image-11.png)
