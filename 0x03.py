import math

def prime(number):
    li = [True for i in range(0,number+1)]
    li[0]= False
    li[1]= False

    for i in range(2,int(math.sqrt(number)+1)):
        for num in range(i+1,number+1):
            if num%i == 0:
                li[num]= False

    for index in range(len(li)):
        if li[index]==True:
            print(index,end=" ")

    return None

prime(5)