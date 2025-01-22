import pkg
from pkg.mod_1 import func_1 as fnc1
from pkg.mod_1 import func_2 as fnc2
from pkg.mod_2 import func_3 as fnc3, func_4 as fnc4

print(fnc1(), fnc2(), fnc3(), fnc4())
print(pkg.URL)