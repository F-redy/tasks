# Изменить отображение целых чисел.

# 12345 - добавить незачищен нули и проблемы

# 00012345   #    12345
# 0012345    #   12345
# 012345     #  12345
# 12345      # 12345
# 12345      # 12345

n = 12345
# нули
print(f'{n:08d}')
print(f'{n:07d}')
print(f'{n:06d}')
print(f'{n:05d}')
print(f'{n:04d}')

# знаки пробелов
print(f'{n:8d}')
print(f'{n:7d}')
print(f'{n:6d}')
print(f'{n:5d}')
print(f'{n:4d}')
