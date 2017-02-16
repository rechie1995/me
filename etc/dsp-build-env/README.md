# 跟踪板Linux编译环境搭建
跟踪板部分程序需要在Linux上进行编译。  
下面介绍如何搭建Linux编译环境。  
可以选用的Linux系统众多，笔者使用的是Ubuntu 16.04 64位系统
## 一、SEED DVS6446 SDK套件的安装  
SEED DVS6446 SDK套件中提供了Linux内核、ARM v5t交叉编译器、DSP端开发工具，ARM编解码程序源码，DSPLINK、CMEM源码、CODEC ENGINE例程源码等。  
SEED DVS6446 SDK 的安装建议按照以下步骤与路径进行配置，以简化后续各种配置的繁琐，安装过程以root账号登陆Linux开发主机，且一直以root权限进行所有操作，开发过程也以root权限进行开发。  
* 复制  
将DaVinci开发套件SEED-DVS6446_SDK.tar.gz复制到Linux开发主机的/opt目录下；  
* 安装  
在Linux开发主机上打开终端，进入到/opt目录下，进行解压安装操作，使用命令：  
```  
# cd /opt/  
# tar -zvxf SEED-DVS6446_SDK.tar.gz  
```  
该过程将所需要的软件安装到/opt根目录下，安装过程需要5-10分钟，请等待完成。  
SEED DVS6446 SDK安装完成后，将在/opt下创建如下目录：  
**dvevm_1_20**:该目录下为DVEVM与DVSDK套件，包括各种cmem、dsplink、frame component、codec engine、demo源码及dspbios、xdctools、cgtools等dsp端编译器等资源；  
**mv_pro_4.0**:该目录下为ARM端的armv5t交叉编译，linux内核以及目标文件系统；  
**nfs**:该目录为配置完毕的NFS文件系统；  
## 二、SEED DVS6446 SDK配置
SEED-SDK安装完毕仅需对其进行简单的配置即可以使用，进行demo等程序的编译等操作。  
\> 配置ARM v5t交叉编译器PATH  
1.以root操作，编辑/etc/environment文件：
```
# gedit /etc/environment  
```  
2.在PATH值末尾加入如下内容：  
“：/opt/mv_pro_4.0/montavista/pro/devkit/arm/v5t_le/bin:/opt/mv_pro_4.0/montavista/pro/bin:/opt/mv_pro_4.0/montavista/common/bin”  
保存退出即可 （需要重启才能生效）  
3.因为我使用的Ubuntu是64位系统，在使用arm_v5t编译器之前需要添加32位运行库才能正常使用；  
添加32位运行库的命令为：  
```  
sudo apt install lib32ncurses5 lib32z1  
```  
4. 测试：
用户可以通过以下方式测试arm_v5t编译器是否可以使用，在Ubuntu终端输入如下命令：  
```  
# arm_v5t_le-gcc  
```  
显示如下信息时，表示安装正常：  
```  
arm_v5t_le-gcc: no input files
```  
\>配置NFS文件系统服务
详见  
>Ubuntu搭建nfs和tftp服务器.html

以上完成了SEED-SDK的安装与配置，下面将介绍各文件包的编译位置及编译命令。  
## 三、跟踪板各文件包在Linux的编译方法 
以下命令均以需编译板的文件夹在linux上的路径为操作根路径。如：  
`/mnt/hgfs/share_DM6446/2016双目跟踪源码/tec`   
1.在编译各文件包之前需要将ividenc.h文件放置到正确位置，不然后续的编译都会出错。   
```
# mv /opt/dvevm_1_20/xdais_5_10/packages/ti/xdais/dm/ividenc.h /root/  
# cp ividenc.h /opt/dvevm_1_20/xdais_5_10/packages/ti/xdais/dm/
```  
上述命令将SDK中原本存在的ividenc.h备份在/root文件夹下，随后将文件包内的ividenc.h文件复制进相对应的文件夹下。  
2.将codec文件夹下的MotionDetect文件夹复制到相应文件夹  
```  
# cd codec/  
# cp -R -a MotionDetect/ /opt/dvevm_1_20/codec_engine_1_10_01/examples/codecs/  
```  
进入到相应文件夹下，执行编译命令。  
```  
# cd /opt/dvevm_1_20/codec_engine_1_10_01/examples/codecs/MotionDetect/  
# make clean  
# make 
# make backup  
```  
3.将sever文件夹下的MotionDetect文件夹复制到相应文件夹   
```  
# cd server
# cp -R -a MotionDetect/ /opt/dvevm_1_20/codec_engine_1_10_01/examples/servers/  
```  
进入相应文件夹下，执行编译命令：  
```  
# cd /opt/dvevm_1_20/codec_engine_1_10_01/examples/servers/MotionDetect/  
# make clean  
# make  
# make tar
# make backup  
```  
4.将app文件夹下的MotionDetect_app文件夹复制到相应文件夹  
```  
# cd app/
# cp -R -a MotionDetect_app/ /opt/dvevm_1_20/demos/  
```  
进入相应文件夹下，执行编译命令：
``` 
# cd /opt/dvevm_1_20/demos/MotionDetect_app/
# make clean  
# make 
# make tar
# make backup
```  

## 参考资料  
---
>1.SEED-DVS6446 Development Software User's Guide.pdf  
>2.SEED-DTK6446 实验手册.pdf  
>3.Ubuntu搭建nfs和tftp服务器.html
