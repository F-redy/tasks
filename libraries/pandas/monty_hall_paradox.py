from random import choice, seed

import matplotlib.pyplot as plt
import pandas as pd

attempts = int(input('enter number of attempts: '))

play = pd.DataFrame('-', index=range(attempts), columns=['Door_1', 'Door_2', 'Door_3'])
seed(1)
for i in range(len(play)):
    play.iat[i, choice([0, 1, 2])] = 'Price'
print(play)
print((play == 'Price').sum())

seed(3)
play['First_choice'] = pd.Series([choice([0, 1, 2]) for _ in range(attempts)])
print(play)
print((play == 'First_choice').sum())
play['Not_changed'] = play.apply(lambda x: ('Win' if x.iat[x['First_choice']] == 'Price' else 'loss'), axis=1)
print(play)

plt.figure(figsize=(10, 10))
val_counts = pd.DataFrame(play['Not_changed'].value_counts()).sort_index()
plt.pie(val_counts['Not_changed'], labels=val_counts.index, colors=['green', 'red'], autopct='%.0f%%',
        textprops={'fontsize': 20, 'color': 'blue'})
title_obj = plt.title('Not change decisions in all rounds', )
plt.setp(title_obj, color='w')
plt.setp(title_obj, fontsize='20')
plt.show()
play.drop('Not_changed', axis=1, inplace=True)
print(play)
seed(5)


def open_empty_door(play: pd.Series):
    doors = {0, 1, 2}
    doors.discard(play['First_choice'])
    idx_car = list(play['Door_1': 'Door_3'] == 'Price').index(True)
    doors.discard(idx_car)
    return doors.pop() if len(doors) == 1 else choice(list(doors))


play['Empty_door'] = play.apply(open_empty_door, axis=1)
print(play)
play['Changed_choice'] = 3 - play['Empty_door'] - play['First_choice']
print(play)
play['Changed'] = play.apply(lambda x: ('Win' if x.iat[x['Changed_choice']] == 'Price' else 'loss'), axis=1)
print(play)

plt.figure(figsize=(10, 10))
val_counts = pd.DataFrame(play['Changed'].value_counts()).sort_index()
plt.pie(val_counts['Changed'], labels=val_counts.index, colors=['green', 'red'], autopct='%.0f%%',
        textprops={'fontsize': 20, 'color': 'blue'})
title_obj = plt.title('change decisions in all rounds', )
plt.setp(title_obj, color='w')
plt.setp(title_obj, fontsize='20')
plt.show()
