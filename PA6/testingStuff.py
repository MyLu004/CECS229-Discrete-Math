
val1 = ['1','2','3']
val2 = ['4','8']

mulVal = 1
mySum = 0

if len(val1) != len(val2):
    bigger = max(len(val1),len(val2))
    smaller = min(len(val1),len(val2))

    remaining_length = bigger - smaller

    if len(val1) < len(val2):
        val1 = ['0'] * remaining_length + val1

    else:
        val2 = ['0'] * remaining_length + val2

# print('val1: ',val1)
# print("val2: ",val2)

for i in range(len(val1)-1,-1,-1):
    print("i: ",i, "val1: ", val1[i])
    print("i: ",i, "val2: ", val2[i])
    # print(val2[i])
    # val1[i] *= mulVal
    for j in range(int(val2[i])):
        for k in range(len(val1)-1,-1,-1):
            mySum += int(val1[k])
        mulVal *= 10


print("my sum: ",mySum)