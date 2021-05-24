#Package code to a python package
[tutorial](https://docs.python.org/3/distutils/setupscript.html)

A simple demo - Only has setup.py

install :
```
pip install .
```

And you can call package like this:
```
import package_a
package_a.hello()
# output : Hi~~~
```

## setup.py


#### packages 資訊
```
name='lisa',
version="1(不向下相容).0(向下相容).0(不改動功能的更正次數)",

description="簡短的描述",
long_description="詳細的描述",
long_description_content_type='text/markdown',

author="...",
author_email="...",

url="http://...",
```
#### packages 設定
* packages: 內指定全部的 package
```
#1 手動指定
packages=['package_a', 'package_a.package_in_a']
#2 自動找
packages=find_packages() #找全部的
## ['package_a', 'package_a.package_in_a']
#3 自動找,排除特定路徑
packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"])
#4 自動找指定路徑
packages=find_packages(include=["package_a"])
```
* package_dir: 替換package路徑設定
```
package_dir={"": "src"},  
# 用""(root)取代src
# src.a => a
```

#### 設定requires
* 限定python版本
```
python_requires=">=3.6"
# 版本需為 3.3.x
python_requires='~=3.3',
# 版本需為 >=2.6 但不為3.0.*
python_requires=">=2.6, !=3.0.*"
```
* install_requires: 需要一起安裝的requires
```
install_requires = ["requests"]
```
* extras_require: 特殊功能，正常使用不會用到，不會主動安裝
```
extras_require={
    'test': ['coverage'],
}
```
* tests_require: 測試時要安裝的套件
```
tests_require=[
      'pytest>=3.3.1',
      'pytest-cov>=2.5.1',
],
```
執行下面cmd時才會安裝
```
python setup.py test
```
* dependency_links: 額外下載(沒有在pipy)上的links, 一般安裝時不會自動裝，見[教學](https://blog.zengrong.net/post/using-dependenty_links-in-setuptools/#requirements)
#### scripts
[scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument)
```
>>> import package_a as p
>>> p.cmdline.script1_entry_point()
Hi~~Lisa~~Script1~~
```

#### Other
* include_package_data: 是否要打包其他資料 True/False，設為 True 可在 MANIFEST.in 設定
* classifiers: 指定額外的metadata
* cmdclass: 自訂自己的cmd

####\_\_init\_\_.py
* __init__.py 的作用是將該資料夾下作為一個模組
* 再匯入一個package時,會先匯入該package的__init__.py
* 會有一個__all__ value ,包含全部的modual
````
# __init__.py
__all__ = ['mod1']
# test
from package import *
````

#### classifiers
[classifiers-lists](https://pypi.org/classifiers/)
提供一些metadata資訊

#### version 命名規則
[軟體版本號命名規則](https://www.slmt.tw/blog/2015/07/19/version-number-naming-convention/)
