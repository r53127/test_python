
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w

    def speak(self):
        print('enter people class')
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
        print('exit people class')

# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print('emter student_class')
        super().speak()
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
        print('exit student class')


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print('enter speaker class')
        print("1我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
        print('exit speaker class')


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

    def speak(self):
        print('enter sample class')
        super().speak()
        print("2%s 说: 我 %d 岁了，体重 %d ，我在读 %d 年级,我是一个演说家，我演讲的主题是 %s" % (
        self.name, self.age, self.weight, self.grade, self.topic))
        print('exit sample class')


s = sample("Tim", 25, 80, 4, "Python")
print('sample class的mro表为：',sample.mro())
s.speak()
super(sample, s).speak()
super(speaker, s).speak()
super(student, s).speak()
