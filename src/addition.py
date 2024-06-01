# app.py
# This is a test commit
def add(a, b):
    c=a+b
    print(c)
    return c

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
