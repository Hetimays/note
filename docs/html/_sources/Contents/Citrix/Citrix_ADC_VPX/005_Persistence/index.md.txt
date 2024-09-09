# Parsistence

## 0. はじめに
ロードバランスの続きで進めていきます。  
パーシステンスは、source ipやcookieを用いて同一サーバへ転送する機能です。  
ECサイトの決済システムなど、同一サーバで処理をしたいパターンでよく使われます。  

今回は、source ipによるパーシステンスの動作を確認していきます。

<br><br>

## 1. VPXの設定
設定は簡単です。  
前回設定したvServerに対してパーシステンスの設定を追加します。  
```Traffic Management > Load Balancing > Virtual Servers```  
![vs1](image.png)  
![vs2](image-1.png)  

<br><br>

## 2. 確認
クライアントのIPを変えつつ確認をしていきます。  
まずは、**10.0.10.1**からアクセスして振り分けを確認します。  
![c1](image-3.png)
![c2](image-4.png)

次にクライアント側のIPを**10.0.10.2**に変更しアクセスします。  
![c3](image-5.png)
![c4](image-6.png)

source ipによって振り分けられるサーバが固定されていることが確認できました。  
