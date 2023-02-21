num1=[1,2,3,4,4,3,2,1]
n =int(input())#take input in integer

num2 = []
num3 = []
num4 = []

#make list of first half
for i in range(0,int(n)):
    num2.append(num1[i])

#make list of second half
for j in range(int(n),len(num1)):
    num3.append(num1[j])

# append the element of first half and second half in num4 list.
for k in range(0,int(n)):
    num4.append(num2[k])
    num4.append(num3[k])
print(num4)