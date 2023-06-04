# Inheritance

# do a Mermaid diagram

class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Child(Parent):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


# Composition

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class B:
    def __init__(self, a: A, z):
        self.a = a
        self.z = z



