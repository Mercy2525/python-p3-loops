#!/usr/bin/env python3

def happy_new_year():
    count=11
    while count>=2:
        count -= 1
        print(count)
        if count==1:
            print("Happy New Year!")

def square_integers(int_list):
    # list=[num**2 for num in int_list]
    # return list

    #or
    new_list=[]
    for num in int_list:
        new_list.append(num**2)
    return new_list

def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz") 
        elif i%3==0:
            print("Fizz") 
        else:
            print(i)          
fizzbuzz()