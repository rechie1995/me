# 用virtualenv建立Python独立开发环境  
  
&emsp;&emsp;不同的人喜欢用不同的方式建立自己的开发环境，所以需要有一个工具来提供一个独立的开发环境。在Python的开发环境中最常使用的是virtualenv包。virtualenv是一个来创造独立的Python环境的包。  
&emsp;&emsp;简单得说，你将为每个项目安装所有需要的软件包到它们各自独立的环境中。  
## 安装virtualenv  
安装virtualenv很简单  
` pip install virtualenv`  

## 使用virtualenv  
第一步，创建目录：
```
$ mkdir myproject  
$ cd myproject/
```  
第二步，创建一个独立的Python运行环境，命名为`venv`:  
```
$ virtualenv --no-site-packages venv
```  
命令`virtualenv`就可以创建一个独立的Python运行环境，我们还加上了参数`--no-site-packages`，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，我们就得到了一个不带任何第三方包的Python运行环境。  
  
第三步，进入`venv`环境
```
$ source venv/bin/activate
```  
会注意到命令提示符变了，有个`(venv)`前缀，表示当前环境是一个名为`vnev`的Python环境。  
后续正常安装各种第三方包，并运行Python命令。  
在`venv`环境下，用`pip`安装的包都被安装到`venv`这个环境下，系统Python环境不受任何影响。也就是说，`venv`环境是专门针对`myproject`这个应用创建的。  
  
第四步，退出`venv`环境
```
$ deactivate
```  
此时就回到了正常的环境，现在pip和Python都是在系统Python环境下执行。