def outer_loop():
    name="Suresh"
    def inner_loop():
        nonlocal name
        name = "Mr.Stark"
        print(name)
    print("Printing from inner loop")
    inner_loop()
    print("Printing from outer loop")
    print(name)
outer_loop()