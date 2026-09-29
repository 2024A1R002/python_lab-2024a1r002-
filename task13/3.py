# wap in  python to show that tuple value cannot be changed directly , convert in to list,update it and convert it back into tuple
t = (1,6,7,8)
print("original tuple",t)
l = list(t)
l[1]= 50
t = tuple(l)
print("updated tuple",t)