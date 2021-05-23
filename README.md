# Package code to a python package

A simple demo - Only has setup.py
setup.py
```
from setuptools import find_packages, setup

setup(
    name="lisa",
    version="0.1.0",
    description="Hi~~~",
    packages=find_packages(),
)
```


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
