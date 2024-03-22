import math

myvalue = (1.75+1j)
# theta = math.cos(math.atan2(myvalue.imag,myvalue.real))
a = myvalue.real
b = myvalue.imag

z = math.sqrt((a)**2 + (b)**2)

print("my z: ",round(z))
tau = math.pi/2
# a = math.sqrt(3)
# b = -1
theta = round(math.atan2(b,a),2)
print("atan: ",math.atan2(a,b))

print("\nadd value for rotate:",end=" ")
new_theta = tau + theta
print(new_theta)

#change to complex representation

trigcos = round(z*math.cos(new_theta),2)
trigsin = round(z*math.sin(new_theta),2)

print(complex(trigcos,trigsin))






