# ppt
一个友好的类jq的json print，带有简洁的json路径过滤功能，支持dict keys()、values()、items()方法，以及全功能字符串、列表切片。
支持 Python2、Python3

[![Build status](https://travis-ci.org/rq/rq.svg?branch=master)](https://secure.travis-ci.org/rq/rq)
[![PyPI](https://img.shields.io/pypi/pyversions/rq.svg)](https://pypi.python.org/pypi/rq)

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

## 示例
```python
from ppt import ppt
test = '{"a": [1, 3, 4, 9, 10, 0, 5, 3, 7], "c": [{"h": 1, "d": [{"e": ["f", "g"]}]}], "b": "1234567890", "d": null}'
ppt(test)
```

输出格式化的json，且key按字母顺序排序：
```python
{
    "a": [
        1,
        3,
        4,
        9,
        10,
        0,
        5,
        3,
        7
    ],
    "b": "1234567890",
    "c": [
        {
            "d": [
                {
                    "e": [
                        "f",
                        "g"
                    ]
                }
            ],
            "h": 1
        }
    ],
    "d": null
}
```

过滤：
```python
ppt(test, '.a.::2', normal_path_print=True)
```
```python
[
    1,
    4,
    10,
    5,
    7
]
get it normally with: <obj>["a"][::2]
```

函数过滤：
```python
ppt(test, '.c.0.keys()', normal_path_print=True)
```
```python
[
    "h",
    "d"
]
get it normally with: <obj>["c"][0].keys()
```

切片：
```python
ppt(test, 'a.1:-2:2', normal_path_print=True)
```
```python
[
    3,
    9,
    0
]
get it normally with: <obj>["a"][1:-2:2]
```