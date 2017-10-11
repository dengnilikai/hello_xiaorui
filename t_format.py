'''
format使用范例。
'''

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def __str__(self):
        return "this guy is {self.name}, is {self.age} years old".format(self=self)

if __name__=='__main__':
    print(str(Person(29,"Shawn")))
