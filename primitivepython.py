# Import the 'namedtuple' function from the 'collections' module
from collections import namedtuple
# Set the tuple
#tuple je v podstate object
ovocie = namedtuple("Nazov_identifikacia", "name size expiry")
#typ1 <class '__main__.Nazov_identifikacia'>
#"nazov_identifikacia" je vlastne CLASSNAME

t1 = ovocie(name="Banana", size=25, expiry=7) 
t2 = ovocie(name="Jahoda", size=2, expiry=3)
t3 = ovocie(name="Melon", size=38, expiry=6)
print("typ1",type(t1))

print(t1[0],t1.size)
#mozes zavolat poradovym cislom, ale aj nazvom (je to predsa namedTuple a to sme chceli)



tuples = (t1,t2,t3)

for i in tuples:
    print(i.name)
    print(i.size)

# s tuples sa asi blbo countuje !!!
#a = tuples.count(ovocie)
#print(a)
print("Yes") if 5 > 2 else print("No")
#bez dvojbodky !!!
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  #else sa da pouzit aj vo while!!!

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
#
print(mydoubler(11))
print(mytripler(11))
