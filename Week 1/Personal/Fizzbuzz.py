#Program Details:
#divisible by 3, print Fizz 
#divisible by 5, print buzz
#divisible by both 3 and 5, FizzBuzz
# if divisile by none, print the number as it is
#Solution 
#1. For nuber input, we use for loop 
#2. 4 conditional statement for checking divisibility 

for i in range(1,1000):
    #module operarator % = remainder
    if i % 5 == 0 and i % 3 == 0:
      print("Fizzbuzz")
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
            print("Buzz")
    else:
            print(i)

        
              