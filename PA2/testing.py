a = 58
b = 73

mySet1 = set(range(2,18))


print("my prime: ",a)
mySet2 = set([value for value in range(a,b+1)])

print("my Set2: ",mySet2)

set1 = set(range(1,11))
set2 = set(range(5,11))
print("my set final: ",set1-set2)


myPrimt = 2
myPrimeSet = set([myPrimt*value for value in range(a,b) if (myPrimt*value <= b)])

print("my Prime Set: ",myPrimeSet)