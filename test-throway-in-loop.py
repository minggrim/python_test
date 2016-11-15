def test(a):
    z = 1
    for _ in a:
        z += 1
    return z

print test(['a', 'b', 'c', 'd'])
