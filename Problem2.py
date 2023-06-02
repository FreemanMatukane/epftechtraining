
num1 = 1
num2 = 0
sum = 1
even_Value =0
while sum <4000000:
#for i in range(33):
    sum= num1 + num2
    #print(sum)
    num1=num2
    num2=sum
    sum= num1 + num2
    if sum%2==0:
        #print(sum)
        even_Value+=sum
print(even_Value)