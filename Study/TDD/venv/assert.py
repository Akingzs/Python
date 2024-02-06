def soma (x, y):
    assert isinstance(x, (int, float)), 'x must be an integer or float'
    return x + y


print(soma('3',5))
print(soma(4,5))

