class Student():
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender=gender

bart = Student('Bart', 'male')
if bart.get_gender() == 'male':
    print('测试失败!')

bart.set_gender('female')
if bart.get_gender() != 'female':
    print('测试失败!')
else:
    print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)


m=5
x=[1,3,5,6,7]
print(id(m),id(5),id(x),id(x[0]),x,id(x[1]))
def test(m,x):
    print(id(m))
    n=m
    x[0]=10000
    print(id(n),id(x),id(x[0]),x,id(x[1]))
    return n,x
k,x=test(m,x)
print(id(m),id(k),id(x),id(x[0]),id(x[1]))


def bar(a):
    print(id(a))
    a.append(7)
    print(a)
a=[]
for _ in range(5):
    bar(a)


class Student(object):
    def __init__(self, name):
        self.name = name
c1 = Student('Bob')
c1.score = 90
print(c1.score, c1.name)

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败1!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败2!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

