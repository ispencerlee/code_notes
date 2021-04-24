# How to use markdown 

# 个人简介
## 基本信息

**姓名**：毕小烦  **年龄**：32岁      **职业**：攻城狮

**爱好：**

- 看电影，听音乐，喝咖啡
- ~~抽烟~~, 喝酒，~~烫头~~(*头发没了*)

## 星号

***

* * * 

### 插入图片
！[图片文字](./head.png)

### 文字链接
[链接文字](链接地址)

eg:   
[google](www.google.com)

常用网站链接：  
[google],[youtube],[github] 

[google]: https://google.com
[youtube]: https://youtube.com 
[github]: https://github.com 

### 网页链接
<www.youtube.com>

### 代码
`public class`

```
public class

```

```shell
$ echo "test"
test
```
### 转义字符
\
\\


### 删除线

~~被删除的文字~~


### 表情符号

:表情代码

: smile

### 标准链接

在标准语法中由<>包裹的URL地址被识别并解析为超链接
如：

<www.google.com>

使用GFM拓展语法可以不使用<>包裹
如：
www.google.com

注意：GFM只自动识别www或http://开头的链接


### 表格

|标头1 | 标头2 | 标头3 | 
|:------|:-------:|-------:|
|内容1 | 内容2 | 内容3 | 

注意：块级元素（代码块，引用区块）不能插入表格中

人物列表
- [ ] 未勾选
- [x] 已勾选

### 围栏代码块

```python
def test_print()
    pass  
```

### 锚点

锚点,也称书签,用来标记特定文档的位置，使用锚点可以跳转到当前文档或其他文档中指定的标记位置。

[锚点描述](#锚点名)

语法说明：
1）锚点名建议使用字母和数字，当然中文也支持
2）锚点名区分大小写
3）在锚点名中不能包含有空格，也不能含有特殊字符

eg:
目录
* [第01章](#第01章)
* [第02章](#第02章)

## 第01章
ba la ba la 

## 第02章
ba la ba la ba la 
