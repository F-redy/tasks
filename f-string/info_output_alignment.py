# нужно красиво и ровно вывести информацию.

print(f'Число\t\tКвадрат\t\t\tКуб')
for x in range(1, 11):
    print(f'{x:2d}\t\t\t\t{x * x:3d}\t\t\t{x * x * x:4d}')
