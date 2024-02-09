def int_within_bounds(number, lower_bound, upper_bound):
  # Type your code
  if type(number) is float:
    return False
  elif number>lower_bound and number<upper_bound:
    return True
  else:
    return False
#test
#print(int_within_bounds(5.0,100,20))