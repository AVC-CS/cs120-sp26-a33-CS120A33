import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # C=20 -> F=68.00
    content = open('result1.txt').read()
    print(content)
    regex_test([r'68\.00'], content)

@pytest.mark.T2
def test_main_2():
    # C=90 -> F=194.00
    content = open('result2.txt').read()
    print(content)
    regex_test([r'194\.00'], content)

@pytest.mark.T3
def test_main_3():
    # C=0 -> F=32.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'32\.00'], content)

@pytest.mark.T4
def test_main_4():
    # C=100 -> F=212.00
    content = open('result4.txt').read()
    print(content)
    regex_test([r'212\.00'], content)
