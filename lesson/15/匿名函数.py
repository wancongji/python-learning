print((lambda :0)())

print((lambda x,y:x+y)(3,4))

print((lambda x,y=3:x+y)(3))

print((lambda x,*,y=3:x+y)(3,y=4))

print((lambda *args:[x+1 for x in args])(*range(5)))

print((lambda *args:{x+1 for x in args})(*range(5)))

print([x for x in (lambda *args:map(lambda x:x+1, args))(*range(5))])

print([x for x in (lambda *args:map(lambda x:(x+1, args), args))(*range(5))])