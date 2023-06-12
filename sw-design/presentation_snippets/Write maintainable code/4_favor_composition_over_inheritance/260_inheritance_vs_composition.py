# Inheritance

"""
TODO for Francois:
- do Mermaid diagrams
- actually don't use this code snippet. It's too simple and theoretical. I want something also simple and short
  but that looks more like production /real-life example. 
""" 

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



