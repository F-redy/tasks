def parse_json(data):
    match data:
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
            return login, email
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return login, ids

    return None


test_tase = [
    ({'id': 1, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]},
     ('1234', 'xxx@mail.com')),
    ({'id': 2, 'access': True, 'data': ('26.05.2023', {'login': '5678', 'email': 'xxx@mail.com'}, 2000, 56.4)},
     ('5678', 'xxx@mail.com')),
    ({'id': 3, 'access': False, 'data': ['26.05.2023', 2000, 56.4]},
     None),
    ({'id': 4, 'access': 'True', 'data': ('26.05.2023', {'login': '9123', 'email': 'xxx@mail.com'}, 2000, 56.4)},
     ('9123', 4)),
    ({'id': 5, 'access': 123, 'data': ['26.05.2023', {'login': '4567', 'email': 'xxx@mail.com'}, 2000, 56.4]},
     ('4567', 5)),
    ({'id': 6, 'access': 1, 'data': ('26.05.2023', {'login': '8521', 'email': 'xxx@mail.com'}, 2000, 56.4)},
     ('8521', 6)),
    ({'id': 7, 'access': 0, 'data': ['26.05.2023', {'login': '7396', 'email': 'xxx@mail.com'}, 2000, 56.4]},
     ('7396', 7))
]

for i, (test_json_data, answer) in enumerate(test_tase, 1):
    result = parse_json(test_json_data)
    assert result == answer, f'TEST №{i} - ERROR!\nERROR in {test_json_data}\n{result} != {answer}'
    print(f'TEST №{i} - OK')
