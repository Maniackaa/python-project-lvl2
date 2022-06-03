from gendiff.generate_diff_temp import generate_diff
from gendiff.scripts.gendiff import main


def test_answer():
    a = {'host': 'hexlet.io', 'timeout': 50,
         'proxy': '123.234.53.22', 'follow': False}
    b = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

    result = generate_diff(a, b)

    assert result == "{\n - follow: False,\n   host: hexlet.io,\
\n - proxy: 123.234.53.22,\n - timeout: 50,\n + timeout: 20,\
\n + verbose: True\n}"


# def test_gendiff():
#     import json
#     with open('tests/fixtures/file1.json') as file:
#         data1 = file.read()
#         print(data1)
#     with open('tests/fixtures/file2.json') as file:
#         data2 = file.read()
#         print(data2)
#     with open('tests/fixtures/output.json') as file:
#         data3 = file.read()
#         print(data3)
#     f1 = json.loads(data1)
#     f2 = json.loads(data2)
#     result = generate_diff(f1, f2)
#     print(result)
#     assert result == data3

def test_arse():
    main
