def details(**info):
    for key, value in info.items():
        print(key, ":", value)

details(name="shravan", age=21, city="Mumbai")