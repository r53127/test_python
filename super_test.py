class Base(object):


    def __init__(self):


        print("enter Base")


        print("leaveBase")





class A(Base):


    def __init__(self):


        print("enterA")


        super(A,self).__init__()


        print("leaveA")





class B(Base):


    def __init__(self):


        print("enterB")


        super(B,self).__init__()


        print("leaveB")





class C(A,B):


    def __init__(self):


        print("enterC")


        super(C,self).__init__()


        print("leave C")
