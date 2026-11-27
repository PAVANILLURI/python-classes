
print(" assining multipul values to multipul varibles")

num1,num2,num3=10,20,30
print("number 1 value",num1,"number 2 value",num2,"number 2 value",num3)
print("all variables refferences are ", id(num1),id(num2),id(num3))


print("assining single value to multipul variables")
num1=num2=num3=10
print("number 1 value",num1,"number 2 value",num2,"number 2 value",num3)
print("all variables refferences are ", id(num1),id(num2),id(num3))


print(" check the memory location above 255 ")
#print("assining single value to multipul variables")
num1=num2=num3=287
print("number 1 value",num1,"number 2 value",num2,"number 2 value",num3)
print("all variables refferences are ", id(num1),id(num2),id(num3))


print("swaping two numbers ")
a,b=10,20
print("variables refferences are",a,b,id(a),id(b))
a,b=b,a
print("variables refferences are",a,b,id(a),id(b))








