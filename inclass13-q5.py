class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)


class Class4(Class1):
    def m(self):
        print("In Class4")
        Class1.m(self)


c4 = Class4()
c3 = Class3()
c2 = Class2()
c1 = Class1()

ls = [c1, c2, c3, c4]
for c in ls:
    print(c.m())