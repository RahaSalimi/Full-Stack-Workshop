input1=None
input2=None
while input1 is None:
    try :
        input1=float(input("Enter first number: "))
    except:
        print('enter integer or float')

while input2 is None:
    try :
        input2=float(input("Enter second number: "))
    except:
        print('enter integer or float')


inputs_sum= input1+input2
inputs_sub=input1-input2
inputs_multi=input1*input2
inputs_power=input1**input2
inputs_division=input1/input2

print("sum of inputs = ",inputs_sum)
print("sub of inputs = ",inputs_sub)
print("multiply of inputs = ",inputs_multi)
print("power of inputs = ", inputs_power)
print("division of inputs = ", inputs_division)


input3=None
while input3 is None:
    try:
        input3=float(input("Enter third number: "))
    except:
        print('enter integer or float')
   
print("sfinal sum is = ",float(inputs_sum)+input3)
print("sub of inputs = ",float(inputs_sub)-input3)
print("multiply of inputs = ",float(inputs_multi)*input3)
print("power of inputs = ", float(inputs_power)**input3)
print("division of inputs = ", float(inputs_division)/input3)
    
