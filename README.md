# dspt4_unit3_package

## Installation

````sh

pip install -i https://test.pypi.org/simple/ dspt4-unit3-package

```

## Usage

from dspt4_unit3_package.my_mod import enlarge

print("Happy Tuesday Night!")

df = pandas.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
print(df.head())


x = 5
print("Enlarge", x, "to", enlarge(x))
