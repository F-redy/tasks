# Превращаем вложенный словарь в плоский
# Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен.
# Ключами словаря на любом уровне могут быть только строки, значения - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
# (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _
#
# Для этого необходимо определить рекурсивную функцию flatten_dict.
# Она должна принимать вложенный словарь и возвращать плоский
#
# Ниже приведены несколько способов решения вышеуказанной задачи.
#
# nested = {'Germany': {'berlin': 7},
#           'Europe': {'italy': {'Rome': 3}},
#           'USA': {'washington': 1, 'New York': 4}}
#
# flatten_dict(nested) => {'Germany_berlin': 7,
#                          'Europe_italy_Rome': 3,
#                          'USA_washington': 1,
#                          'USA_New York': 4}
# nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
#
# flatten_dict(nested) => {'Q_w_E_r_T_y': 123}
# not_nested = {'a': 100, 'b': 200}
#
# flatten_dict(not_nested) => {'a': 100, 'b': 200}

def flatten_dict(dictionary: dict, parent_key: str = '', sep: str = '_') -> dict:
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}
assert flatten_dict({'Germany_berlin': 7,
                     'Europe_italy_Rome': 3,
                     'USA_washington': 1,
                     'USA_New York': 4}) == {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1,
                                             'USA_New York': 4}
assert flatten_dict({'a': 100, 'b': 200}) == {'a': 100, 'b': 200}
assert flatten_dict(
    {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}) == {
           'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
assert flatten_dict({"a": 1,
                     "b": {
                         "c": 2,
                         "d": 3,
                         "e": {
                             "f": 4,
                             '6': 100,
                             '5': {"g": 6},
                             "l": 1,
                         }
                     }}) == {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
