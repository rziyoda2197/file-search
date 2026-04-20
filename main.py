import os

def file_search(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

directory = input("Kiritilgan faylni qidirish uchun direktoriya kiriting: ")
filename = input("Qidirilayotgan fayl nomi kiriting: ")

result = file_search(directory, filename)

if result:
    print(f"Fayl topildi: {result}")
else:
    print("Fayl topilmadi.")
```

```python
import re

def file_search(directory, filename):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(filename, file, re.IGNORECASE):
                return os.path.join(root, file)
    return None

directory = input("Kiritilgan faylni qidirish uchun direktoriya kiriting: ")
filename = input("Qidirilayotgan fayl nomi kiriting: ")

result = file_search(directory, filename)

if result:
    print(f"Fayl topildi: {result}")
else:
    print("Fayl topilmadi.")
