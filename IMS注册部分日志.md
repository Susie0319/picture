#### REGISTER

aucSipMsg:REGISTER sip:ims.mnc060.mcc460.3gppnetwork.org SIP/2.0
To: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>
From: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=Y2fcb1D
Contact: <sip:460600100049906@[2001:683:890:1942:1::9e0b:baea]:5060>;+sip.insta
nce="<urn:gsma:imei:86774304-000024-0>";+g.3gpp.accesstype="cellular2";audio;+g.
3gpp.smsip;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"
Expires: 600000
**P-Access-Network-Info**: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Supported: path,sec-agree
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,UPDATE,PRACK,NOTIFY,MESSAGE,REFER
Require: sec-agree
Proxy-Require: sec-agree
**Security-Client**: 

**ipsec-3gpp**;**alg**=hmac-sha-1-96;**prot**=esp;**mod**=trans;**ealg**=des-ede3-
cbc;**spi-c**=26157848;**spi-s**=69326023;**port-c**=31100;**port-s**=31800,

ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=null;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=des-ede3-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=aes-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=null;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800
**Authorization**: Digest username="460600100049906@ims.mnc060.mcc460.3gppnetwork.org",**realm**="ims.mnc060.mcc460.3gppnetwork.org",**uri**="sip:ims.mnc060.mcc460.3gppnetwork.org",**nonce**="",**response**=""
Call-ID: X1fcb1DXa@[2001:683:890:1942:1::9e0b:baea]
CSeq: 1 REGISTER
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:5060;branch=z9hG4bKZ3fcb1DXaWVqLBkaaaUO;rport
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0

**P-Access-Network-Info**：携带用户接入位置信息

**Security-Client**：其中alg为完整性保护算法，spi-c/spi-s为安全参数索引SPI（Security Parameter Index），port-c/port-s为UE的安全端口号。  

**Authorization**：

- realm（领域）：必须的，在所有的盘问中都必须有。它是目的是鉴别SIP消息中的机密。在实际应用中，它通常设置为server所负责的域名。

- nonce （现时）：必须的，这是由服务器规定的数据字符串，在服务器每次产生一个摘要盘问时，这个参数都是不一样的（与前面所产生的不会雷同）。nonce 通常是由一些数据通过md5杂凑运算构造的。这样的数据通常包括时间标识和服务器的机密短语。确保每个nonce 都有一个**有限的生命期**（也就是过了一些时间后会失效，并且以后再也不会使用），而且是**独一无二的**（即任何其它的服务器都不能产生一个相同的nonce ）。客户端使用这个“现时”来产生摘要响应（digest response），需要和server 盘问中携带的nonce保持一致，这样服务器也会在一个摘要响应中收到“现时”的内容。服务器先要检查了“现时”的有效性后，才会检查摘要响应的其它部分。

  因而，nonce 在本质上是一种标识符，确保收到的摘要机密，是从某个特定的摘要盘问产生的。还限制了摘要盘问的生命期，防止未来的重播攻击。

- username： 不用再说明了

- response：这是由用户代理软件计算出的一个字符串，以证明用户知道口令。比如可以通过 username、password、http method、uri、以及nonce、qop等使用MD5加密生成。

- uri：这个参数包含了客户端想要访问的URI。

  1. server 确认用户 
     确认用户主要由两部分构成：
     1. 检查nonce的有效性
     2. 检查摘要响应中的其他信息， 比如server可以按照和客户端同样的算法生成一个response值，和client传递的response进行对比。

#### 401

aucSipMsg:SIP/2.0 401 Unauthorized
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:5060;branch=z9hG4bKZ
3fcb1DXaWVqLBkaaaUO;rport=5060
Call-ID: X1fcb1DXa@[2001:683:890:1942:1::9e0b:baea]
From: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=Y2fcb1D
To: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=2ke0helt
CSeq: 1 REGISTER
**WWW-Authenticate**: Digest realm="ims.mnc060.mcc460.3gppnetwork.org",**nonce**="nTD5N
ZXcGXhEIzR7Y5CL7l6EMyJYfRERnE3UeQOjxgs=",**algorithm**=AKAv1-MD5
**Security-Server**: ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;s
pi-c=2605593363;spi-s=3790665812;port-c=9950;port-s=9900
Content-Length: 0

#### REGISTER

aucSipMsg:REGISTER sip:ims.mnc060.mcc460.3gppnetwork.org SIP/2.0
To: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>
From: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=W4fcb1D
Expires: 600000
P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Supported: path,sec-agree
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,UPDATE,PRACK,NOTIFY,MESSAGE,REFER
Require: sec-agree
Proxy-Require: sec-agree
**Security-Client**:

 ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=des-ede3-
cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=null;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=des-ede3-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=aes-cbc;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800,

ipsec-3gpp;alg=hmac-md5-96;prot=esp;mod=trans;ealg=null;spi-c=26157848;spi-s=69326023;port-c=31100;port-s=31800

**Security-Verify**: ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;s
pi-c=2605593363;spi-s=3790665812;port-c=9950;port-s=9900
CSeq: 2 REGISTER
Call-ID: X1fcb1DXa@[2001:683:890:1942:1::9e0b:baea]
**Authorization**: Digest **nonce**="nTD5NZXcGXhEIzR7Y5CL7l6EMyJYfRERnE3UeQOjxgs=",user
name="460600100049906@ims.mnc060.mcc460.3gppnetwork.org",uri="sip:ims.mnc060.mcc
460.3gppnetwork.org",**realm**="ims.mnc060.mcc460.3gppnetwork.org",algorithm=AKAv1-M
D5,**response**="01b656a14d1bc707e362cfb27a8accdb"
Contact: <sip:460600100049906@[2001:683:890:1942:1::9e0b:baea]:31800>;+sip.inst
ance="<urn:gsma:imei:86774304-000024-0>";+g.3gpp.accesstype="cellular2";audio;+g
.3gpp.smsip;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKX5fcb1DXa
WVqLBkaaGUO;rport
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0

#### 200 OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
X5fcb1DXaWVqLBkaaGUO;rport=31100
Call-ID: X1fcb1DXa@[2001:683:890:1942:1::9e0b:baea]
From: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=W4fcb1D
To: <sip:460600100049906@ims.mnc060.mcc460.3gppnetwork.org>;tag=gqj0iolo
CSeq: 2 REGISTER
Accept-Resource-Priority: wps.4
**P-Associated-URI**: <sip:+8613801049906@ims.huawei.com>  <sip:+8613801049906@ims.huawei.com;user=phone>
Contact: <sip:460600100049906@[2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800>;
expires=900;+sip.instance="<urn:gsma:imei:86774304-000024-0>";+g.3gpp.accesstype
="cellular2";audio;+g.3gpp.smsip;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.im
s.icsi.mmtel"
Content-Length: 0

S-CSCF创建的头域，携带隐式注册集列表，表示此次注册上的用户列表

![1534853171920](C:\Users\Z84108~1\AppData\Local\Temp\1534853171920.png)



![1534852213031](C:\Users\Z84108~1\AppData\Local\Temp\1534852213031.png)