class Myclass:
    class_attribute = "I am global"
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def method(self):
        return self.attr1

    def method_ind():
        return  "Hello"



# obj = Myclass("parm1", "parm2")

# print(obj.class_attribute)

# Inheritance

class ParentClass:
    def __init__(self, attr1):
        self.attr1 = attr1
    def method(self):
        return self.attr1

# class ChildClass(ParentClass):
#     pass

# Method overriding

class SecondChildClass(ParentClass):
    def __init__(self, attr1, attr2):
        super().__init__(attr1)
        self.attr2 = attr2
    def method(self):
        return self.attr2

# child_obj = SecondChildClass("par1", "par2")

# print(child_obj.method())


class MyClass2:
    #class attributes
    glob_attr = "I am global"

    @classmethod
    def class_method(cls):
        return cls.glob_attr


    @staticmethod
    def static_method():
        return "I am static"




obj2 = MyClass2()

# print(obj2.class_methdd("Hello"))
# print(obj2.static_method())

class Employ():
    raise_amount = 30
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @classmethod
    def set_raise_method(cls,amount):
        cls.raise_amount = amount
    
    def apply_raise(self):
        self.salary *= self.raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

object1 = Employ('abc', 'def', 200)

object2 = Employ('hello', 'hi', 100)


import datetime

my_date = datetime.date(2024, 1, 8)
# print(Employ.is_workday(my_date))

# print(object1.raise_amount)
# print(object2.raise_amount)


# Employ.set_raise_method(40)


# print(object1.raise_amount)
# print(object2.raise_amount)

# object1.apply_raise()
# print(object1.salary)


class MyClass3:
    def __init__(self, attribute):
        self._attribute = attribute
    
    @property
    def attribute(self):
        return self._attribute
    
    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @attribute.deleter
    def attribute(self):
        del self._attribute


# Getter
obj = MyClass3(10)
print(obj.attribute)

# Setter
obj.attribute = 20
print(obj.attribute)

#deleter
del obj.attribute

def Practice():
    message = 'Hello'
    def __init__(self,attribute,attribute2):
        self.attribute = attribute
        self.attribute2 = attribute2
    @classmethod
    def get_message(cls,self):
        cls.message = message


