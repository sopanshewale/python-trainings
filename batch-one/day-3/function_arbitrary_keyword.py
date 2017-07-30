def f(**kwargs):
    print(kwargs)
 
f()
f(de="German",en="English",fr="French")

def f2(a,b,x,y):
    print(a,b,x,y)


d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f2(**d)

