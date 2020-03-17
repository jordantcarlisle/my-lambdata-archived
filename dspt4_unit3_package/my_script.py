
# dspt4_unit3_package/my_script.py

import pandas

from dspt4_unit3_package.my_mod import enlarge

print("Happy Tuesday Night!")

df = pandas.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df.head())


x = 5
print("Enlarge", x, "to", enlarge(x))
