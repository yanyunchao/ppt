# ppt
一个友好的类jq的json print，带有简洁的json路径过滤功能，支持dict keys()、values()、items()方法，以及全功能字符串、列表切片。
支持 Python2、Python3

## API
ppt(obj, filter='.', with_print=True, normal_path_print=False)

* obj: 输入对象，dict、list、string
* filter：过滤字符串
* with_print: 是否格式化打印输出过滤结果
* normal_path_print: 是否输出过滤器反解后的正常查找方式


支持过滤方式：

* dict key过滤      .key

* dict key列表      .keys()

* dict value列表    .values()

* dict key,value对  .iterms()

* list过滤     .3    或 .[3]

* list负索引    .-2  或 .[-2]

* list切片1    .2:6  或 .[2:6]

* list切片2    .2:   或 .[2:]

* list切片3    .:6   或 .[:6]

* list step1   .1:6:2  或 .[1:6:2]

* list step2   .1::2   或 .[1::2]

* list step3   .::2    或 .[::2]

* string过滤..与list相同

* string切片..与list相同

* string 切片 step..与list相同