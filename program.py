# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
# loop from 1 to 32 so the end range needs to be 1 more
for myNumber in range(1, 33):
  if myNumber % 15 == 0:
    result = str(result) + str('FizzBuzz') + "\n"
  elif myNumber % 5 == 0:
    result = str(result) + str('Buzz') + "\n"
  elif myNumber % 3 == 0:
    result = str(result) + str('Fizz') + "\n"
  else:
    result = str(result) + str(myNumber) + "\n"

print(result)
