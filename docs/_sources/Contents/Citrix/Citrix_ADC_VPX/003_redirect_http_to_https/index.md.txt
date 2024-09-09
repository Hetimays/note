# HTTPS Redirect 
## 0. はじめに
vServerのvip宛にHTTPでアクセスがあった場合に、HTTPSにリダイレクトする設定を確認します。  

**参考：**
[レスポンダーを使用して HTTP リクエストを HTTPS にリダイレクトする方法](https://docs.netscaler.com/ja-jp/citrix-adc/current-release/appexpert/responder/how-to-redirect-HTTP-requests-HTTPS-using-responder.html)

<br><br>

## 1. VPXの設定
まず、レスポンダー機能を有効にします。  
```System > Settings```  
![system1](images/image.png)  

レスポンダーアクションを設定します。  
後述のレスポンダーポリシーにmatchしたトラフィックに対して行う操作を定義します。  
ここで設定している内容は、URLのプロトコル以降をそのままに、プロトコルだけを **https://** に置き換えています。  
```AppExpert > Responder > Actions```  
![responder1](images/image-1.png)

レスポンダーポリシーにはHTTPリクエストパケットがmatchするように設定します。  
なお、version13.1にはGUIだと設定できないバグがあるみたいなので、14.1以降を使用するか、CLIで設定してください。  
```AppExpert > Responder > Policies```  
![responder2](images/image-2.png)

HTTPを受けるvServerはリダイレクト処理を行うため常にUPしている必要があります。  
また、HTTPでアクセスしてきたパケットはサーバ側へルーティングしてはいけません。  
そこで、自身のloopbackを宛先にしたモニタを設定し、それを紐づけたServiceを定義します。  
vServerには常にUPになるように設定したServiceをbindします。  
```Traffic Management > Load Balancing > Monitors```  
![monitor1](images/image-3.png)

Serviceに設定するIPはどこにも使われていないIPを指定します。  
Monitorsには先程定義したモニタを指定します。  
```Traffic Management > Load Balancing > Services```  
![service1](images/image-4.png)
![service2](images/image-5.png)

vServerのプロトコルはHTTP、リダイレクト先のHTTPSに対応するvServerと同じIPにします。  
```Traffic Management > Load Balancing > Virtual Servers```  
![vs1](images/image-6.png)

定義したレスポンダーをvServerに紐づけます。  
![vs2](images/image-7.png)
![vs3](images/image-8.png)

<br><br>

## 2. 確認
SSLで受けるvServerに合わせたweb serverを起動します。  
```python3 -m HTTP.server 8080```

クライアント側のブラウザからHTTPでアクセスするとHTTPSにリダイレクトされていることが確認できました。
![client2](images/image-9.png)
![client1](images/image-10.png)
