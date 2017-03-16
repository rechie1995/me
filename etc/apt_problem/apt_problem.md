# 一些关于apt的问题
## 1、无法获得锁/var/lib/dpkg/lock - open(11:资源暂时不可用)  
终端提示：  
无法获得锁/var/lib/dpkg/lock - open(11:资源暂时不可用)  
E:无法锁定管理目录(/var/lib/dpkg/),是否用其他进程正在占用它？  
解决办法如下：  
1、终端输入ps -aux, 列出进程，找到含有apt的进程，直接sudo kill PID解决。  
2、强制解锁--命令：  
```  
sudo rm /var/cache/apt/archives/lock  
sudo rm /var/lib/dpkg/lock  
```
  
