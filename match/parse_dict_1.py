def parse_json(data):
    match data:
        case {'access': bool(access), 'data': list([date, *_])}:
            return access, date
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


test_case = [
    ({'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]},
     (False, '26.05.2023')),
    ({'id': 2, 'access': "False", 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]},
     (2, '1234')),
    ({'id': 2, 'access': "False", 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000]}, None),
    ({'id': 2, 'access': False, 'data': []}, None)
]

for i, (test, answer) in enumerate(test_case, 1):
    result = parse_json(test)
    assert result == answer, f'TEST №{i} - ERROR!\nERROR in: {test}\n{result} != {answer}'
    print(f'TEST №{i} - OK')
