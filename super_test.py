from enum import Enum

a = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in a.__members__.items():
    print(name)
    print(member)
    print(a.__members__)
    print(name, '=>', member, ',', member.value)
    print((member))