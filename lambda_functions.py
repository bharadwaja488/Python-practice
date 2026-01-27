'''x = lambda a,b,c : a+b+c
print("Result:",x(5,2,1))'''

l1=[12,34,5,6,8]
l2=[]
for i in l1:
    t=lambda a : a+1
    l2.append(t(i))
print(l2)


