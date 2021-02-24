class MyClass:
    def __setattr__(self, attr, value):
        if attr == "width":
            self.__dict__[attr] = value
        else:
            print(f"Атрибут {attr} недопустим")


mc = MyClass()
mc.height = 40




