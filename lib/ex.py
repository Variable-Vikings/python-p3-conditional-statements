class A:
    def __init__(self):
        print("Constructor A")

    def a1(self):
        print("A a1")

    def a2(self):
        print("A a2")

f1 = A()

f1.a1()
f1.a2()

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor B")
     

    def b1(self):
        print("B b1")

    def a1(self):
        super().a1()

f2 = B()
f2.a1()

