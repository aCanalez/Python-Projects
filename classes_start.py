#
#   Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method 1")

    def method2(self, someString):
        print("anotherClass method2 ")

class anotherClass3(anotherClass):
    def method1(self):
        anotherClass.method1(self)
        print("anotherClass method 1")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")

    c3 = anotherClass3()
    c3.method1()


if __name__ == "__main__":
    main()
