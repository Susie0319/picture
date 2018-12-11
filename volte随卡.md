# 重点

### 安卓系统架构——RIL

**RIL**（无线接入层）——Android中负责通信功能的Telephony中间层 

Android手机要实现与网络端的通信，需要跨越两个层：

- RIL Java(RILJ)：负责将上层APP的通信请求发送给HAL层；
- RIL C++(RILD、RILC)： 系统守护进程，负责将RILJ的请求命令发送给BP(Communication Processor)，HAL层中的C/C++程序。

RILJ属于系统Phone进程的一部分，随Phone进程启动而加载；而RILD守护进程是通过Android的Init进程进行加载的 。

Android RIL的一个结构图。

- 最上层的是应用程序，如通话，短信以及SIM卡管理，它们主要负责将用户的指令发送到RIL Framework(以后统称RILJ）；
- 对于RIL的java框架部分，被分成了两个部分，一个是RIL模块，这个模块主要用于与下层的rild进行通信，另外一个是Phone模块，这个模块直接暴露电话功能接口给应用开发用户，供他们调用以进行电话功能的实现。为上层提供了通用的API，如TelephonyManager(包括通话，网络状态； SubscriptionManager(卡状态）以及SmsManager等，同时RILJ还负责维持与RILD的通信，并将上层的请求发送给RILD；
- 应用程序框架与内核之间分成了两个部分，一个部分是rild,它负责socket与应用程序框架进行通信。另外一个部分是Vendor RIL，这个部分负责向下是通过两种方式与radio进行通信，它们是直接与radio通信的AT指令通道和用于传输包数据的通道，数据通道用于手机的上网功能。RILD的功能主要功能是将RILJ发送过来的请求继续传递给BP，同时会及时将BP的状态变化发送给RILJ；
- Linux驱动层：kernel驱动层接受到数据后，将指令传给BP，最后由BP发送给网络端，等网络返回结果后，BP将传回给RILD；

![1532674293504](C:\Users\Z84108~1\AppData\Local\Temp\1532674293504.png)



RILJ与RILD（RILD与BP的通信）都是通过一个个消息进行数据传递。消息主要分两种：

一种是RILJ主动发送的请求（solicited），常见的有`RIL_REQUEST_GET_SIM_STATUS`(获取SIM卡状态）， `RIL_REQUEST_DIAL`(拨打电话），`RIL_REQUEST_SEND_SMS`（发送短信）， `RIL_REQUEST_GET_CURRENT_CALLS`（获取当前通话状态），`RIL_REQUEST_VOICE_REGISTRATION_STATE`（获取网络状态）； 

另一种则是从BP主动上报给RIL的消息（unsolicited)，如网络状态发生变化时，BP会上报`RIL_UNSOL_RESPONSE_VOICE_NETWORK_STATE_CHANGED`，有新短信时，会上报`RIL_UNSOL_RESPONSE_NEW_SMS`，有来电时会上报`RIL_UNSOL_CALL_RING`。 

> RIL相关的请求命令与数据结构都定义在`/android/hardware/ril/include/telephony/ril.h` 



在整个过程中，有几个关键问题：

1. 上层是如何得知RILJ状态变化的？

   ​	为方便上层实时监听网络状态、通话状态以及BP的状态变化，RIL提供了一个专门的监听接口`IPhoneStateListener.aidl`，上层需要监听上述状态变化时，只需要实现上述接口,并在Android系统服务TelephonyRegistry中对上述接口实现进行注册： 

   ​	另外，也可以在TelephonyManager中对RIL状态进行监听： 

2. RILJ与RILD是怎么进行通信的？

   ​	RILJ在创建过程中，会启动两个线程：RILSender和RILReceiver，RILSender负责将指令发送给RILD，而RILReceiver则负责从读取从RILD发送过来的数据。RILJ与RILD的通信通道就是在RILReceiver中建立起来的。 

   ​	RILReceiver启动时，会建立一个UNIX Domain socket(LocalSocket，kernel层对应`/dev/socket/rild`)，与RILD进行通信，然后一直从socket中读取数据,并将数据传给上层。连接成功后，RILD会发送一个消息给RILJ，表示连接成功了，这样RILJ就可以将请求数据发送给RILD，进行通信了。 

3. RILJD与BP又是如何进行通信的？

   ​	RILD与BP（可以看做是两个运行在不同BPU上的进程通信）交换数据方式一般有两种情况。如果AP与BP集中在一个芯片上，如高通的平台就是将AP与BP集中在一块芯片上，这时通常采用共享内存的方式实现跨进程通信；而如果不是在同一块芯片，而是AP与BP分别采用不同厂商的平台，则一般采用字符设备(character devices) 进行通信。总的说来，共享内存的方式在速度上要优于字符设备。 



### 随卡位置

AT 即Attention  所有调制解调器制造商采用的一个调制解调器命令语言 





### 如何随卡

xml文件用于查看和修改NV配置，而bin文件是在实际代码中加载使用。由于ril和kernel中缺乏xml文件解析库函数，且xml格式文件的加载和解析的效率较低，因此我们会将xml格式源文件转换为bin

随卡匹配文件分为三类：

1)       NV初始值恢复配置文件（COMMON）

由于海思平台没有办法在手机正常运行的状态下读到版本默认NV值，因此需要提前将随卡匹配所有涉及到的NV，按照版本默认值提前配好，用于在不同运营商间进行随卡参数切换时，以及在插入无需执行随卡匹配的卡时，将此前被修改过的NV恢复为版本默认值。

2)       运营商随卡NV配置文件（如CMCC_CN、DT_DE、VDF_ES）

运营商NV配置文件记录了该运营商的全部NV随卡数据。当程序判断匹配上某个运营商参数时，会将其对应配置文件中的所有NV参数写入至NVIM中，然后重启Modem子系统，使这些NV修改生效。

3)       索引文件（CONFIG）

索引文件可以理解为运营商卡信息与运营商随卡NV配置文件的一个映射表。也就是说通过索引文件可以容易的查到某一NV配置文件都对应哪些运营商的卡（通过MCCMNC或ICCID标识，下同），反过来也可以确认某个运营商的卡匹配的是哪个NV配置文件。



**CONFIG.xml**

NV_FILE_NAME：NV配置文件的文件名。运营商_国家，无中文，不超过31字符

MCCMNC_SIZE：该NV随卡文件，对应的卡的MCCMNC（HPLMN）个数，最大值40。
MCCMNC_LIST：该NV随卡文件，对应的卡的MCCMNC列表，能支持1-6位MCCMNC匹配。

ICCID_SIZE：该NV随卡文件，对应的卡的ICCID的个数，最大值为10。需要与ICCID_LIST配合使用。 
ICCID_LIST：该NV随卡文件，对应的卡的ICCID的列表。能够支持1~8位的ICCID匹配。

MODEM_NUM：表示该NV随卡文件，对应在哪个modem上生效。 （0或不配--均生效、1--modem0/2--modem1）



**运营商NV配置文件** 

NV ID：需要配置的NV项的ID值。

NAME：该NV项的名称，该项内容不会生成到bin文件里。

MODEM_NUMBER：表示当前NV要写入哪个Modem。（3.0不用，兼容2.0用，优先级高）

PARAM_VALUE：该NV项的具体配置内容。

NV_SIZE：该NV项内容的长度，也就是字节数。



feature随卡配置文件，支持直接修改某个NV中的某个字段的值，而不影响其他字段的值。

**feature索引表（feature_index.xml）** 

FEATUREINDEX：表示该特性的编号，用于唯一标识某个特性，只增，不允许重复或者更改。

FEATURENAME：表示该特性的名称，内容用于方便阅读或配置该项特性，该字段不生成在bin文件中 。

NVID：表示该特性对应的NVID，与下面的START和LENGTH一起标识具体对应NV中哪个字段。

START：表示该特性对应NVID中字段的起始位置，单位是字节。如NVID中第一个字段的START=0，第二个字段的START=第一个字段的字节数 。

TYPE：表示该特性中包含的元素的数据类型，每条特性中的所有元素的数据类型都相同。目前一共支持5种TYPE的数据，分别是：uint8、uint16、uint32、char、bit，数据占用的空间分别为：1byte、2byte、4byte、1byte、1bit 。

LENGTH：表示该特性中包含元素的个数，如LENGTH=10，表示该特性一共包含了10个元素。但当TYPE=bit时比较特殊，LENGTH用于表示自START开始的bit类型的数目。如START="5"，TYPE=bit，LENGTH=32，表示从第5个字节开始，连续4个字节(32个bit)，都是bit类型的数据 。

BITPOS：仅在TYPE=bit的场景下使用，与LENGTH一起，表示当前特性对应的是第几bit位。如LENGTH=32，BITPOS=2，表示当前特性为32个bit中的第2bit。

DEFAULTVALUE：表示该特性的平台默认值。如果某特性在运营商的feature_list中没有配置取值，则自动将该运营商的该特性配置为平台默认值。

FORCEVALUE：表示该特性的平台强制值，不允许在运营商的feature_list中配置。

**运营商feature列表(feature_list.xml)** ：用于配置该运营商与feature_index中取值不同的特性的取值 

FEATUREINDEX：表示该特性的编号，用于索引index表中的对应特性 

FEATURENAME：表示该特性的名称，与index中的含义和作用相同。

VALUE：表示该特性在该运营商下特有的取值。能够覆盖index中的DEFAULTVALUE，但不能覆盖FORCEVALUE

编译规则：

如果feature索引表中，某一条feature的FORCE_VALUE字段有值配置，那么这个feature取值默认所有运营商均继承，切**不允许覆盖**。即运营商Feature列表中不允许配置该条feature。 

如果feature索引表中，某一条feature的DEFAULT_VALUE字段有值，那么这条feature的取值默认继承到所有运营商的NV配置中，但**可以覆盖**。即在运营商Feature列表没有配置的默认添加此配置，有配置的则使用运营商Feature列表中配置的值。

如果feature索引表中，某一条feature的DEFAULT_VALUE字段和FORCE_VALUE字段均未预置取值，则表示该feature完全取决于各运营商Feature列表中配置值。若在某运营商Feature列表中有配置则说明该运营商支持该特性，反之则说明不支持该特性。

如某条Feature在Feature索引表中找不到（Feature_index不存在），则编译报错。



NCFG_DIFF配置文件：

第一级：NCFG_CAT，代表产品维度

第二级：NCFG_VERSION，代表定制版本维度

















# 问题

![1532658481773](C:\Users\Z84108~1\AppData\Local\Temp\1532658481773.png)

