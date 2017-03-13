from confdir import load_conf

test_confdir = 'test_confdir'

def test_load_conf():
    assert load_conf(test_confdir) == {
        'BOOL': True,
        'DICT': {'one': 1, 'three': 3, 'two': 2},
        'DICT_OF_DICTS': {
            'A': {'one': 1, 'three': 3, 'two': 2},
            'B': {'one': 1, 'three': 3, 'two': 2},
        },
        'LIST': ['A', 'B', 'C'],
        'NUMBER': 42,
        'SET': {'A', 'B', 'C'},
        'STRING': 'Hello World!',
        'TUPLE': ('A', 'B', 'C'),
    }
