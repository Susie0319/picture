### BEGIN



![1533631150971](C:\Users\Z84108~1\AppData\Local\Temp\1533631150971.png)

#### `INVITE

aucSipMsg:INVITE tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phonecontext=ims.mnc060.mcc460.3gppnetwork.org>
P-Preferred-Identity: <sip:+8613801049906@ims.huawei.com>
Contact: <sip:+8613801049906@[2001:683:890:1942:1::9e0b:baea]:31800>;+sip.instance="<urn:gsma:imei:86774304-000024-0>";+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";audio;+g.3gpp.mid-call;+g.3gpp.srvcc-alerting;+g.3gpp.ps2cs-srvcc-orig-pre-alerting
Accept-Contact: *;+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"
**P-Access-Network-Info**: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
**P-Preferred-Service**: urn:urn-7:3gpp-service.ims.icsi.mmtel
**P-Early-Media**: supported
**Supported**: 100rel,histinfo,join,norefersub,**precondition**,replaces,timer,sec-agree
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,UPDATE,INFO,PRACK,NOTIFY,MESSAGE,REFER
Accept: application/sdp,application/3gpp-ims+xml
**Session-Expires**: 1800
**Min-SE**: 90
**Route**: <sip:[2001:1111:2222:4444::1]:9900;lr>
**Require**: sec-agree
**Proxy-Require**: sec-agree
**Security-Verify**: ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;spi-c=2605593363;spi-s=3790665812;port-c=9950;port-s=9900
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 1 INVITE
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKZ1fcbfd9S
avDrBkaaWTO;rport
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Type: application/sdp
Content-Length: 808





v=0 		//SDP版本号，目前为0
o=rue 3200 3200 IN IP6 2001:683:890:1942:1::9e0b:baea		//主叫源地址，类型等
s=- 		//主题
c=IN IP6 2001:683:890:1942:1::9e0b:baea		//连接
b=AS:49		// 指示RTP/RTCP所需带宽
b=RR:1837
b=RS:612
t=0 0		// 时间戳
m=audio 31000 RTP/AVP 107 106 105 104 101 102		//媒体（媒体格式，端口号，媒体传输类型）
b=AS:49
b=RR:1837
b=RS:612
a=rtpmap:107 AMR-WB/16000/1
a=fmtp:107 mode-change-capability=2;max-red=0
a=rtpmap:106 AMR-WB/16000/1
a=fmtp:106 octet-align=1;mode-change-capability=2;max-red=0
a=rtpmap:105 AMR/8000/1
a=fmtp:105 mode-change-capability=2;max-red=0
a=rtpmap:104 AMR/8000/1
a=fmtp:104 octet-align=1;mode-change-capability=2;max-red=0
a=rtpmap:101 telephone-event/16000
a=fmtp:101 0-15
a=rtpmap:102 telephone-event/8000
a=fmtp:102 0-15			// 媒体属性（媒体编码：AMR-WB宽带，AMR窄带，采样率） telephone-event说明支持DTMF信令

a=ptime:20		// 表示1帧/20ms
a=maxptime:240		// 表示1帧/240秒是个界限，网络侧不能低于这个速率

a=sendrecv			// SDP协商
a=curr:qos local none			//当前状态（precondition type：qos，status type：local）
a=curr:qos remote none
a=des:qos mandatory local sendrecv
a=des:qos optional remote sendrecv		// des：期望，derection tag：sendrecv

级别：optional，级别从低到高是none（资源没有），optional（资源可选），mandatory（资源一定要有）



#### `100 TRYING 	

//100 Trying表示网络侧在尝试连接被叫

aucSipMsg:SIP/2.0 100 Trying
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bKZ1fcbfd9SavDrBkaaWTO;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>
CSeq: 1 INVITE
Content-Length: 0



#### `183 SESSION PROGRESS		

//网络侧回183表示网络侧在做资源预留，建立QCI5，QCI1等承载

aucSipMsg:SIP/2.0 183 Session Progress
Via:SIP/2.0/UDP[2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bKZ1fcbfd9SavDrBkaaWTO;rport=31100
Record-Route: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
CSeq: 1 INVITE
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,NOTIFY,MESSAGE,UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffffff-ffffffff>
Require: 100rel,precondition
RSeq: 1
P-Early-Media: gated
Feature-Caps: *;+g.3gpp.srvcc;+g.3gpp.srvcc-alerting
Recv-Info: g.3gpp.state-and-event
Content-Length: 517
Content-Type: application/sdp

v=0
o=- 20067 20067 IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
s=SBC call
c=IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
t=0 0
m=audio 47994 RTP/AVP 107 102
a=rtpmap:107 AMR-WB/16000
a=fmtp:107 mode-set=0,1,2,8;mode-change-period=2;mode-change-capability=2;mode-change-neighbor=1;max-red=0
a=rtpmap:102 telephone-event/8000
a=ptime:20
a=maxptime:20
a=curr:qos local sendrecv
a=curr:qos remote none
a=des:qos optional local sendrecv
a=des:qos mandatory remote sendrecv
a=conf:qos remote sendrecv



#### `PRACK

aucSipMsg:PRACK sip:[2001:1111:2222:4444::1]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffffff-ffffffff SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
Route: <sip:[2001:1111:2222:4444::1]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 2 PRACK
Max-Forwards: 70
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer
P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKaafcbfd9SavDrBkaa8PQ;rport
RAck: 1 1 INVITE
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0

#### 183 SESSION PROGRESS

aucSipMsg:SIP/2.0 183 Session Progress
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Record-Route: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
CSeq: 1 INVITE
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,NOTIFY,MESSAGE,UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffffff-ffffffff>
Require: 100rel,precondition
RSeq: 1
P-Early-Media: gated
Feature-Caps: *;+g.3gpp.srvcc;+g.3gpp.srvcc-alerting
Recv-Info: g.3gpp.state-and-event
Content-Length: 517
Content-Type: application/sdp

v=0
o=- 20067 20067 IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
s=SBC call
c=IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
t=0 0
m=audio 47994 RTP/AVP 107 102
a=rtpmap:107 AMR-WB/16000
a=fmtp:107 mode-set=0,1,2,8;mode-change-period=2;mode-change-capability=2;mode-change-neighbor=1;max-red=0
a=rtpmap:102 telephone-event/8000
a=ptime:20
a=maxptime:20
a=curr:qos local sendrecv
a=curr:qos remote none
a=des:qos optional local sendrecv
a=des:qos mandatory remote sendrecv
a=conf:qos remote sendrecv



#### `200 OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
aafcbfd9SavDrBkaa8PQ;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
CSeq: 2 PRACK
Content-Length: 0



#### `UPDATE

aucSipMsg:UPDATE sip:[2001:1111:2222:4444::1]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffffff-ffffffff SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
Contact: <sip:+8613801049906@[2001:683:890:1942:1::9e0b:baea]:31800>;+sip.instance="<urn:gsma:imei:86774304-000024-0>";+g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel";audio;+g.3gpp.mid-call;+g.3gpp.srvcc-alerting;+g.3gpp.ps2cs-srvcc-orig-pre-alerting
P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer,sec-agree
Require: precondition,sec-agree
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,UPDATE,INFO,PRACK,NOTIFY,MESSAGE,REFER
Proxy-Require: sec-agree
Security-Verify: ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;s
pi-c=2605593363;spi-s=3790665812;port-c=9950;port-s=9900
Route: <sip:[2001:1111:2222:4444::1]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 3 UPDATE
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKbbfcbfd9S
avDrBkaaaTO;rport
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Type: application/sdp
Content-Length: 459

v=0
o=rue 3200 3201 IN IP6 2001:683:890:1942:1::9e0b:baea
s=-
c=IN IP6 2001:683:890:1942:1::9e0b:baea
b=AS:49
b=RR:1837
b=RS:612
t=0 0
m=audio 31000 RTP/AVP 107
b=AS:49
b=RR:1837
b=RS:612
a=rtpmap:107 AMR-WB/16000/1
a=fmtp:107 mode-set=0,1,2,8;mode-change-capability=2;max-red=0
a=ptime:20
a=maxptime:20
a=sendrecv
a=curr:qos local sendrecv
a=curr:qos remote sendrecv
a=des:qos mandatory local sendrecv
a=des:qos optional remote sendrecv

#### `200 OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
bbfcbfd9SavDrBkaaaTO;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 3 UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=
3;TRC=ffffffff-ffffffff>
P-Early-Media: gated
Content-Length: 454
Content-Type: application/sdp

v=0
o=- 20067 20068 IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
s=SBC call
c=IN IP6 2001:1111:2222:4444:0000:0000:0000:0007
t=0 0
m=audio 47994 RTP/AVP 107
a=rtpmap:107 AMR-WB/16000
a=fmtp:107 mode-set=0,1,2,8;mode-change-period=2;mode-change-capability=2;mode-
change-neighbor=1;max-red=0
a=ptime:20
a=maxptime:20
a=curr:qos local sendrecv
a=curr:qos remote sendrecv
a=des:qos optional local sendrecv
a=des:qos mandatory remote sendrecv



#### `183

aucSipMsg:SIP/2.0 183 Session Progress
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Record-Route: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;lr;Hpt=8e62_1
16;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 1 INVITE
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,NOTIFY,MESSAGE,UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=
3;TRC=ffffffff-ffffffff>
Require: 100rel,precondition
RSeq: 2
P-Early-Media: sendrecv
Feature-Caps: *;+g.3gpp.srvcc;+g.3gpp.srvcc-alerting
Recv-Info: g.3gpp.state-and-event
Content-Length: 0

#### `PRACK

aucSipMsg:PRACK sip:[2001:1111:2222:4444::1]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffff
ff-ffffffff SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
Route: <sip:[2001:1111:2222:4444::1]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-
ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 4 PRACK
Max-Forwards: 70
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer
P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKccfcbfd9S
avDrBkaaWlQ;rport
RAck: 2 1 INVITE
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0



#### 183

aucSipMsg:SIP/2.0 183 Session Progress
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Record-Route: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;lr;Hpt=8e62_1
16;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 1 INVITE
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,NOTIFY,MESSAGE,UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=
3;TRC=ffffffff-ffffffff>
Require: 100rel,precondition
RSeq: 2
P-Early-Media: sendrecv
Feature-Caps: *;+g.3gpp.srvcc;+g.3gpp.srvcc-alerting
Recv-Info: g.3gpp.state-and-event
Content-Length: 0

#### `200 OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
ccfcbfd9SavDrBkaaWlQ;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 4 PRACK
Content-Length: 0



#### `180 RINGING

aucSipMsg:SIP/2.0 180 Ringing
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Record-Route: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;lr;Hpt=8e62_1
16;CxtId=3;TRC=ffffffff-ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phonecontext=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
CSeq: 1 INVITE
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,NOTIFY,MESSAGE,UPDATE
Contact: <sip:[2001:1111:2222:4444:0000:0000:0000:0001]:9900;Hpt=8e62_16;CxtId=
3;TRC=ffffffff-ffffffff>
Require: 100rel,precondition
RSeq: 3
P-Early-Media: sendrecv
Feature-Caps: *;+g.3gpp.srvcc;+g.3gpp.srvcc-alerting
Recv-Info: g.3gpp.state-and-event
Content-Length: 0



#### `PRACK

aucSipMsg:PRACK sip:[2001:1111:2222:4444::1]:9900;Hpt=8e62_16;CxtId=3;TRC=ffffff
ff-ffffffff SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org>;tag=eqnh4fic
Route: <sip:[2001:1111:2222:4444::1]:9900;lr;Hpt=8e62_116;CxtId=3;TRC=ffffffff-
ffffffff;X-HwB2bUaCookie=2030>
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 5 PRACK
Max-Forwards: 70
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer
P-Access-Network-Info: 3GPP-E-UTRAN-FDD;utran-cell-id-3gpp=460601013000721E
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKddfcbfd9S
avDrBkaaOAQ;rport
RAck: 3 1 INVITE
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0



#### 180 RINGING



#### `200OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
ddfcbfd9SavDrBkaaOAQ;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 5 PRACK
Content-Length: 0



#### `CANCEL

aucSipMsg:CANCEL tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org
 SIP/2.0
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>
Route: <sip:[2001:1111:2222:4444::1]:9900;lr>
Reason: SIP;cause=487;text="request terminated"
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer,sec-agre
e
Security-Verify: ipsec-3gpp;alg=hmac-sha-1-96;prot=esp;mod=trans;ealg=aes-cbc;s
pi-c=2605593363;spi-s=3790665812;port-c=9950;port-s=9900
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
CSeq: 1 CANCEL
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKZ1fcbfd9S
avDrBkaaWTO;rport
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0

#### `200OK

aucSipMsg:SIP/2.0 200 OK
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=ipidp5z8
CSeq: 1 CANCEL
Content-Length: 0

#### `487 REQUEST TERMINATED

aucSipMsg:SIP/2.0 487 Request Terminated
Via: SIP/2.0/UDP [2001:0683:0890:1942:0001:0000:9E0B:BAEA]:31800;branch=z9hG4bK
Z1fcbfd9SavDrBkaaWTO;rport=31100
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
CSeq: 1 INVITE
Warning: 399 [2001:1111:2222:4444:0000:0000:0000:0001] "SS250200F156L921[00000]
 Cancel received on initial invite"
Content-Length: 0

#### `ACK

aucSipMsg:ACK tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.org SI
P/2.0
To: "13801049907"<tel:13801049907;phone-context=ims.mnc060.mcc460.3gppnetwork.o
rg>;tag=eqnh4fic
From: <sip:+8613801049906@ims.huawei.com>;tag=Y-fcbfd
CSeq: 1 ACK
Call-ID: X9fcbfd9S@[2001:683:890:1942:1::9e0b:baea]
Route: <sip:[2001:1111:2222:4444::1]:9900;lr>
Max-Forwards: 70
Via: SIP/2.0/UDP [2001:683:890:1942:1::9e0b:baea]:31800;branch=z9hG4bKZ1fcbfd9S
avDrBkaaWTO;rport
Supported: 100rel,histinfo,join,norefersub,precondition,replaces,timer
User-Agent: IM-client/OMA1.0 HW-Rto/V1.0
Content-Length: 0