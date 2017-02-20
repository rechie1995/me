#!/bin/sh
# 如何正确安装搜狗拼音 

cd ~/Downloads
sudo apt install libopencc1 fcitx-libs fcitx-libs-qt fonts-droid-fallback
sudo dpkg -i sogoupinyin_2.1.0.0082_amd64.deb
