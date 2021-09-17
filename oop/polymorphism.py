class MyClass:
    def __str__(self):
        return "MyClassの__str__"


various_types = [1, "1", True, [1, 2, 3], (1,), {'1': 1}, {1}]
for elem in various_types:
    print(elem)
