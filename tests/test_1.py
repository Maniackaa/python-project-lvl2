from gendiff.generate_diff import generate_diff


def test_answer():
    a = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    b = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

    result = generate_diff(a, b)

    assert result == "{\n - follow: False,\n   host: hexlet.io,\n - proxy: 123.234.53.22,\n - timeout: 50,\n + timeout: 20,\n + verbose: True\n}"
