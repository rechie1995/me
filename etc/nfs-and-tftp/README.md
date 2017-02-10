# Ubuntu搭建nfs和tftp服务器
## nfs服务器
### 1、安装Ubuntu nfs 服务器
Ubuntu上默认是没有安装Ubuntu nfs 服务器的，因此我们首先安装Ubuntu nfs服务器端：  
  
``` $ sudo apt install nfs-kernel-server ```  
  
### 2、配置/etc/exports  
Ubuntu nfs允许挂载的目录及权限在文件/etc/exports中进行了定义。  
例如，我们要将根目录下的rootfs目录共享出来，那么我们需要在/etc/exports文件末尾添加如下一行：  
  
```/rootfs    *(rw,sync,no_root_squash) ```  
  
**其中：/rootfs是要共享的目录，*代表允许所有的网络段访问，rw是可读写权限，sync是资料同步写入内存和硬盘，no_root_squash是Ubuntu nfs客户端分享目录使用者的权限，如果客户端使用的是root用户，那么对于该共享目录而言，该客户端就具有root权限**  
  
SEED SDK nfs 的配置如下：  
  
```/opt/nfs    *(rw,sync,no_root_squash,no_all_squash) ```  
  
**在使用之前请将挂载的目录权限全部设置成777，即执行 `$ sudo chmod 777 /opt/nfs`**  

**rw sync 等之间是不能有空格的，否则报exportfs:/etc/exports:1:syntax error:bad option list**  
### 3、Ubuntu nfs重启服务
```  
$ sudo service portmap restart  
$ sudo service nfs-kernel-server restart  
```  
如果出现如下错误：  
mount:wrong fs type,bad option, bad superblock on xxxxxx,  
missing codepage or helper program, or other error  
(for several filesystem(e.g.nfs, cifs) you might  
need a/sbin/mount.helper program)  
In some cases useful info is found in syslog -try
dmesg|tail or so  
  
解决方法：  
```  
$ sudo apt install nfs-common  
```  
### 4、测试Ubuntu nfs
此时可以运行以下命令来显示一下共享出来的目录：  
```  
$ showmount -e  
```  
或者可以使用以下命令把它挂载在本地磁盘上，例如将/rootfs挂载到/mnt下:  
```  
$ sudo mount -t nfs localhost:/rootfs /mnt  
```  
可以运行df命令查看是否挂载成功。查看后以后可以使用以下命令卸载：  
```  
$ sudo umount /mnt  
```  
## tftp服务器
### 1、安装相关的软件包：  
```  
$ sudo apt install tftpd-hpa tftp-hpa  
```  
### 2、修改配置
配置文件在/etc/default/tftpd-hpa，内容如下：  
  
\# /etc/default/tftpd-hpa  

TFTP_USERNAME="tftp"  
TFTP_DIRECTORY="/home/rechie/tftpboot"  
TFTP_ADDRESS="[::]:69"  
TFTP_OPTIONS="--secure"  
  
/tftpboot为tftp服务的目录，如果事先不存在的话，我们需要创建它  
```$ sudo mkdir /home/rechie/tftpboot ```  
### 3、重新启动TFTP服务
```$ sudo service tftpd-hpa restart ```  
### 4、测试
```  
$ cd /tftpboot  
$ echo "hello tftp service">>a.txt  
$ tftp localhost  
tftp> get a.txt  
```  
如果这一步执行成功的话说明从tftp服务器下载东西已经成功！  
**注意：tftp-hpa有一个问题，就是每次开机使用之前都需要重启一下服务**