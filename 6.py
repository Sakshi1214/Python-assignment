def NumGenerator():
    for i in range(limit):
        if i%5==0 and i%7==0:
           yield i

s=""         
limit =int(input("enter number"))
for NumGenerator in NumGenerator():
    s=s+(str(NumGenerator)+",")
print (s)
