m=3
n=2
func_dict={}
def register(operator):
  def wrap(func):
      func_dict[operator]=func
      print('test')
      return func
  return wrap
@register(operator="+")
def add(a,b):
  return a+b
@register(operator="-")
def sub(a,b):
  return a-b
@register(operator="*")
def mul(a,b):
  return a*b
@register(operator="/")
def div(a,b):
  return a/b

a=input('请输入 + - * / 中的任意一个\n')
for i in range(len(func_dict)):
    print(func_dict)
c=func_dict[a](m,n)
print(c)