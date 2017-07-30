# 安装FFmpeg和编码器

## 第一步先安装编码器

```
git clone git://git.videolan.org/x264
cd x264
./configure
make
sudo make install
```

## 第二步再安装ffmpeg
```
git clone git://source.ffmpeg.org/ffmpeg.git
cd ffmpeg
./configure
make
sudo make install
```

## 第三步 修改ld.so.conf文件
```
vi /etc/ld.so.conf
```
添加/usr/local/x264/lib,如下
```
include ld.so.conf.d/*.conf
/usr/local/x264/lib
```
:wq退出ld.so.conf文件
执行`ldconfig`
