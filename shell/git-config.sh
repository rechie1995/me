#!/bin/sh

git config --global user.name "rechie"
git config --global user.email "502117806@qq.com"
git config --global core.editor vim
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"

