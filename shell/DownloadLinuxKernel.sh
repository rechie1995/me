#!/bin/bash
# author:rechie
# 用于实现linux-kernel的下载

mkdir linux-stable
cd linux-stable/
git init
git remote add origin git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
#git fetch
git pull
git branch -r
