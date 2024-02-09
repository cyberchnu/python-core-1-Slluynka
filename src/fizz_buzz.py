def fizz_buzz(number):
  #Type your code here

  if number % 3 == 0 and number % 5 == 0:
    result = "FizzBuzz"
  elif number % 3 == 0:
    result = "Fizz"
  elif number % 5 == 0:
    result = "Buzz"
  else:
    result= str(number)
  print(result)
  return (result)
