# sip协议

> by zsq  2018/08/01

#### sip功能

sip协议本身不提供服务，只提供了一个基础，在此基础上加载其他协议一起工作能对终端提供完整的用户服务。

在建立、维持、终止多媒体会话协议上支持五个方面

1. 用户定位：检查终端用户位置
2. 用户有效性：检查用户参与会话的意愿程度
3. 用户能力：检查媒体和媒体的参数
4. 建立会话：建立会话参数在呼叫方和被叫方
5. 会话管理：包括发送和终止会话，修改会话参数，激活服务等



sip不提供服务，提供基础，可以实现不同服务。提供一套安全服务：防止拒绝服务、认证服务、完整性保护、加密、隐私服务。

sip可以基于ipv4也可以ipv6



SIP URI——sip标志，统一分配的资源，用户名+主机名。sip还提供保密URI，称SIPS URI，保证通话安全，被叫者和呼叫的所有SIP消息是加密传输的（叫做TLS，加密机制是基于被叫方宿主服务器实现的）。

定位服务（location service）是一个逻辑概念。他是让代理服务通过输入一个URI来查询到底应该向哪里转发请求。可以简单通过用户注册来建立这个定位服务所需要的资料，也可以通过其他方法。可以通过其他任意的地址映射方式来实现定位服务。



#### SIP网络组件

 ![1533091701475](C:\Users\Z84108~1\AppData\Local\Temp\1533091701475.png)

UA：通过交互sip请求和响应来建立和终结会话

UAC：产生新的sip请求的客户端

UAS：为接收到的sip请求产生响应消息的服务器；响应消息用来接收、拒绝和重定向sip请求

proxy server：主要负责将sip请求消息路由到UAS和将sip响应消息路由到UAC

registrar：接收sip register消息的服务器；负责将用户位置更新到location server

location server：用来存储用户位置信息的服务器

redirect server：为所接收到的sip请求信息返回被叫用户的一个或多个联系地址；不对sip请求进行转发



####  sip分层

![1533037979428](C:\Users\Z84108~1\AppData\Local\Temp\1533037979428.png)

语法和编码层。编码方式：扩展的Backus-Naur Form grammar(BNF范式) 

传输层。定义客户端如何发送请求和接受应答，服务器如何接收请求和发送应答。SIP协议的传输是基于TCP、UDP。如果请求的大小和MTU差在200字节内，或者大小大于1300字节使用TCP，小于1300字节采用UDP。UDP是一个不可靠的传输层协议。SIP协议发现发送失败会进行消息重传处理，而且在重传中采用了应用层的Session Time超时机制。

![1533037991633](C:\Users\Z84108~1\AppData\Local\Temp\1533037991633.png)

事务层。处理应用服务层的重发，匹配请求的应答，以及应用服务层的超时。

事务用户（TU）。每一个SIP实体，除了无状态代理，都是一个事务用户。 当一个TU发出一个请求，它首先创建一个客户事务实例（client transaction instance）并且和请求一起发送，这包括了目标IP地址、端口号、以及发送请求的设备。TU可以创建客户事务，也可以取消客户事务。



#### sip消息

SIP消息是指UAC与UAS之间的请求与应答。SIP协议是一个基于文本的协议，使用UTF-8字符集。



##### 请求

![1533085607420](C:\Users\Z84108~1\AppData\Local\Temp\1533085607420.png)

一个请求行有三个元素：Method、Request-URI、SIP-Version。

Method表示请求的方法，所包含的具体方法有：

|        |                                                              |
| ------ | ------------------------------------------------------------ |
| INVITE | 发起会话                                                     |
| PRACK  | 对1xx响应消息的确认请求消息                                  |
| ACK    | 对INVITE的最终响应消息的确认                                 |
| BYE    | 发起会话终止                                                 |
| OPTION | 查询对端信息或功能（心跳机制）                               |
| CANCEL | 在收到请求信息的最终响应前，取消请求，只能用于cancel INVITE事务 |

Request-URI表示下一跳地址，就是消息即将发往的目的点。



##### 应答

![1533085622417](C:\Users\Z84108~1\AppData\Local\Temp\1533085622417.png)

一个状态行也有三个元素组成：SIP-Version、Status-Code、Reason-Phrase。

Status-Code表示UAS对请求处理的结果指示，取值范围100~699。按照结果类型可分为六大类：



|      | 响应消息                                         |                                                              |
| ---- | ------------------------------------------------ | ------------------------------------------------------------ |
| 1xx  | 临时响应，UAS已经收到了请求并且正在进行处理      | **100** Trying, **180** Ringing, **181** Call is Being Forwarded, **182** Queued, **183** Session Progress |
| 2xx  | 成功响应，请求已经被UAS成功处理                  | **200** OK                                                   |
| 3xx  | 重定向响应，表示处理该请求还需要进行下一阶段处理 | **300** Multiple Choices, **301** Moved Permanently, **302** Moved Temporarily, **305** Use Proxy, **380** Alternative Service |
| 4xx  | 客户端出错，请求语法或信息有问题导致UAS无法处理  | **400** Bad Request,  **401** Unauthorized,  **402** Payment Required,  **403 Forbidden**,  **404** Not Found, ....... |
| 5xx  | 服务器端出错，UAS侧问题导致请求无法处理          | **500** Server Internal Error,  **501** Not Implemented,  **502** Bad Gateway,  **503** Service Unavailable,  **504** Server Time-out,  **505** Version Not Supported,  **513** Message To Large |
| 6xx  | 全局故障，请求无法被任何UAS处理                  | **600** Busy Everywhere ,  **603** Decline,  **604** Does Not Exists Anywhere,  **606** Not Acceptable |



#### 头域

Message-header消息头必须包含有Via、Call-ID、From、To、Cseq、Max-Forwards六个头域。

**Via**：描述当前请求所经历的路径，也就是当前处理节点的地址信息，并且标志了应答所应当经过的路径。响应按照Via记录路径回退给UAC。Via头域的branch ID参数提供了事务的标志，并且用于proxy来检查循环路由。 

**Call-ID**：用于标识一次SIP呼叫，而一次多媒体又分为多个不同Call-ID的呼叫，例如一次多方通话中，主叫A用户先完成与B用户的普通呼叫之后HOLD被叫B用户，A与B之间的呼叫是一个Call-ID。然后主叫A用户呼叫C用户，A与C之间的呼叫Call-ID又是另一个值。Call-ID是大小写敏感的并且是字节/字节比较的。

**From**：描述了请求的来源、发起者。这个可能和对话的来源的不同，被叫方到呼叫方的请求会在From头域使用被叫方的地址。

**TO**：标识了请求的目的、接受者，与From结构相同，标识一次会话需要三个元素来确定，Call-ID、INVITE请求From中的tag以及1XX响应To头域中的tag。Tag的作用除了标识会话之外，还可以用户容灾系统中，备用服务器可以根据tag生成的相关性对会话进行判别，从而识别并接替主用服务器之前提供的服务。

**CSeq**：请求中的Cseq头域包含了一个单个的数字序列号和请求的方法。这个序列号必须是表示成为一个32位的无符号整数。在Cseq的请求方法部分是大小写敏感的。Cseq头域是为了在会话中对事务进行排序的，提供事务的唯一标志，并且区分请求和请求的重发。如果序列号相等，并且请求的方法相等，那么两个Cseq头域就是相等的。 在UAC中，初始值可为任意值，在后续相同Call-ID的不同消息，初始值加1（重发保持不变）；在UAS中，应答CSeq的数值复制UAC请求中所带数值。

**Max-Forwards**：最大跳数，表示请求消息允许在传送过程中允许代理或网关转发的次数，每被转发一次数值减一。70



**Contact**：描述了请求的发起方URI，格式可以为SIP URI或者SIPS URI，而且必须和Request-URI或Route头域中的URI格式一致（SIP URI或者SIPS URI）。INVITE、ACK中的Contact字段指示该请求发出的位置。它使被叫可以直接将请求（如BYE请求）发往该地址，而不必借助Via字段经由一系列代理服务器返回。

**Route**：强制请求经过的路由列表。在初始请求中，由发起请求的UA将出站代理地址和Service-Route中的条目放入Route中；也可以由代理设置，从请求URI或收到的Path消息头中发现下一跳。后续请求中，由发起请求的UAC将初始请求路由中的Record-Route所采集到的条目放入Route中。

**Record-Route**：proxy在请求中增加的，用来强制会话中的后续请求经过本proxy的。 创建会话后续请求的Route头域。 

**Expires**：消息预留时间。例如“Expires: 1800”表示1800秒后，请求超时失效。对于一个INVITE的超时时间并不影响这个INVITE请求建立的实际的会话。不过，会话描述协议可以描述在一个会话上的的时间限制。 

**Allow:** 表示所支持的SIP方法列表。例如“Allow: INVITE,ACK,OPTIONS,BYE,  CANCEL, INFO, PRACK, NOTIFY, MESSAGE, REFER, UPDATE”。

**Supported**：表示服务器所支持的扩展类型.

**Content-Length/Content-Type**：表示所带消息体的长度以及类型。





#### 对话

![1533085184678](C:\Users\Z84108~1\AppData\Local\Temp\1533085184678.png)

被叫发送200ok后，进入confirmed dialog状态；主叫收到200ok后，进入  状态；后续可以通过re-INVITE、UPDATE修改会化妆台。进入最终对话后，可以发起呼叫内的其他事物。

![1533085354941](C:\Users\Z84108~1\AppData\Local\Temp\1533085354941.png)

#### OPTIONS

比如，在客户端试图在INVITE请求头中增加一个请求字段选项的时候，它并不知道对方UAS能否支持这个选项，它就可以用OPTIONS来查询一下UAS，通过检查OPTIONS返回的Supported头域，就可以知道是否支持这个选项。所有的UA都必须支持OPTIONS方法。 





#### SIP呼叫路由机制

##### 响应消息路由

SIP响应经过的路径和请求完全相同，SIP请求消息每经过一个节点，每个节点都会讲自身地址添加到请求消息的VIA头域顶端。

UAS将请求中的Via地址原样拷贝到响应里面，当Proxy接收到响应时，检查顶端的Via是否是自己，如果是，则将顶端的Via删除，并检查下一个Via地址，将响应发送到下一个Via地址，如果没有下一个Via地址，则表示这个响应到此终结。

![1533086618071](C:\Users\Z84108~1\AppData\Local\Temp\1533086618071.png)

##### 请求消息路由

SIP初始请求消息可能会经过很多proxy，可能是通过DNS查询，也可能是预配置的路由，对于后续的请求，没有必要经过初始请求经过的每隔proxy。

中间proxy可以根据自身策略决定后续请求是否需要经过自己，如果需要，则中间proxy需要在请求中加入Record-Route头域，这个头域包含了自己的地址，与Via头域类似，是一个栈结构，如果不需要，则不用。

UAS收到请求后，将请求消息中的Record-Route头域保存为自己的路由集，将请求消息中的Contact作为Remote Target，并在响应消息中将Record-Route头域带回给UAC，。当UAC收到响应消息后，将Record-Route头域保存的地址反序保存为自己的路由集，将响应消息中的Contact作为Remote Target。

当UA需要发起后续请求时，将Remote Target作为Request-URI，并将生成的路由集拷贝到Route头域中，如果存在Route，则将请求路由到Route的第一个值，否则将请求路由到Remote Target.

当proxy收到后续请求，检查最顶端的Route是否是自己，如果是，则将其删除，检查是否还有Route，如果有，则将请求路由到Route的第一个值，如果没有，则将请求路由到Request-URI指向的值。

![1533086585968](C:\Users\Z84108~1\AppData\Local\Temp\1533086585968.png)

![1533086599111](C:\Users\Z84108~1\AppData\Local\Temp\1533086599111.png)



#### 事务

事务主要分为：INVITE事务：采用三次握手； 非INVITE事务：采用两次握手；特殊事务（ACK、CANCEL）

##### 客户端事务

INVITE事务

![img](file:///C:\Users\Z84108~1\AppData\Local\Temp\msohtmlclip1\01\clip_image002.jpg)



![1533087131447](C:\Users\Z84108~1\AppData\Local\Temp\1533087131447.png)

![1533089985530](C:\Users\Z84108~1\AppData\Local\Temp\1533089985530.png)

非INVITE事务

![1533086949529](C:\Users\Z84108~1\AppData\Local\Temp\1533086949529.png)

![1533087165243](C:\Users\Z84108~1\AppData\Local\Temp\1533087165243.png)



















