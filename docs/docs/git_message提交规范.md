# Commit Message 规范

以 angular 规范为例，格式如下：

```git
type(scope): subject    # head 必填，其中 type 和 subject 必填
                        # 空行
72-character wrapped    # body 选填
                        # 空行
BREAKING CHANGE: msg    # footer 选填
```

## head部分

### **type**（只允许下列7个标识）：

- feat：新功能（feature）
- fix：修补bug
- docs：文档（documentation）
- style： 格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
- test：增加测试
- chore：构建过程或辅助工具的变动

**注意**：feat 和 fix 类型的 commit 将出现在 Change log 中。

### **scope（选填）：**

此次提交的影响范围，如数据层、控制层、视图层等，多个可以用 * 代替，必须在type 之后、小括号之内。

### **subject（必填）：**

此次提交的简要描述，必须在 type 之后的冒号之后的一个空格之后，结尾没有句号。

### ***body 部分（选填）:***

此次提交的详细描述，应包含变动描述、变动理由等内容，使用第一人称现在时描述。
必须和 head 部分间隔一个空行，每超过72的字符必须换一行。

### ***foot 部分（选填）:***

包含两种情况：

1. 当前代码不兼容上一个版本，BREAKING CHANGE冒号空格，后跟变动描述、变动理由和迁移方法；2.关闭 Issue，Closes #234 。
1. 特殊情况：当前 commit 用于撤销之前的 commit，revert冒号空格，后跟要撤销的 commit 的 head。

参考资料：

<https://blog.csdn.net/qq_28387069/article/details/84025476>
