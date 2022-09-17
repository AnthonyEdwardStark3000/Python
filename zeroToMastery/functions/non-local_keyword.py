def outer_loop():
    name = 'Suresh Babu'
    print(f'Outer loop says {name}')

    def inner_loop():
        nonlocal name
        name = 'Mr.Stark'
        print(f'Inner loop says {name}', end=' ')
        return 'Love you 3000'
    return inner_loop()


print(outer_loop())
