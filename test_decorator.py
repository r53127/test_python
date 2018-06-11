#例题
def log(text):
    print('准备调用decorator',text)
    def decorator(func):
        print('准备调用wrapper',text,func.__name__)
        def wrapper(*args, **kw):
            print('准备调用func,参数是',args,kw)
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now(a):
    print(a)
    print('2015-3-25')
now('a')

#作业1
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        _start=time.time()
        _n=fn(*args,**kw)
        _end=time.time()
        print('%s executed in %s ms' % (fn.__name__, _end-_start))
        return _n
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')

#作业2
import functools
def testcall(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call ')
        func(*args,**kw)
        print('end call \n ')
        return
    return wrapper

@testcall
def f():
    print('execute f(),作业2 结束。')
f()

#作业3
import functools
def log(text):
    if isinstance(text,str):
        print('有参数的情况准备调用，参数是',text)
        def decorator(func):
            print('准备调用wrapper,参数和函数名分别是：',text,func.__name__)
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('准备调用func,参数是',args,kw)
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('没有参数的情况被call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper

@log
def test1():
    print('test1 is runing...')

test1()

@log('fucking')
def test2():
    print('test2 is runing...')
test2()

import logging
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args)
    return wrapper
@use_logging
def foo():
    print("i am foo")

@use_logging
def bar():
    print("i am bar")

bar()
foo()

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')
@Foo
def bar():
    print ('bar')

bar()