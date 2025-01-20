import sys
print(sys.path)

# To use reglar expresions
import re
text = 'Mi número de telefono es 300 233 2123, el código del pais es 57, mi número de la suerte es 5'
result = re.findall('[0-9]+', text)
print(result)

# Manejo de hora y fecha
import time
timestamp = time.time()
local = time.localtime()
human_format = time.asctime(local)
print(timestamp, local, human_format)

# Collections para manejar listas
import collections
import random
numbers = [random.randint(1, 20) for x in range(1, 20)]
print(numbers)
counter = collections.Counter(numbers)
print(counter)