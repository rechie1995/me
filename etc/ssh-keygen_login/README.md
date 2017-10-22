# Linux下使用ssh-keygen设置ssh无密码登陆

A为本地主机(即用于控制其他主机的机器)

B为远程主机(即被控制的机器Server), 假如ip为172.24.253.2
A和B的系统都是Linux

在A上的命令:

`# ssh-keygen -t rsa` (连续三次回车,即在本地生成了公钥和私钥,不设置密码)

`# ssh root@172.24.253.2 "mkdir .ssh;chmod 0700 .ssh"`(需要输入密码， 注:必须将.ssh的权限设为700)

`# scp ~/.ssh/id_rsa.pub root@172.24.253.2:.ssh/id_rsa.pub` (需要输入密码)

在B上的命令:

`# touch /root/.ssh/authorized_keys` (如果已经存在这个文件, 跳过这条)

`# chmod 600 ~/.ssh/authorized_keys`  (# 注意： 必须将~/.ssh/authorized_keys的权限改为600, 该文件用于保存ssh客户端生成的公钥，可以修改服务器的ssh服务端配置文件/etc/ssh/sshd_config来指定其他文件名）

`# cat /root/.ssh/id_rsa.pub  >> /root/.ssh/authorized_keys` (将id_rsa.pub的内容追加到 authorized_keys 中, 注意不要用 > ，否则会清空原有的内容，使其他人无法使用原有的密钥登录)

回到A机器:

`# ssh root@172.24.253.2` (不需要密码, 登录成功)