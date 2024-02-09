def calculate_fuel(distance):
  # Type your code
  if distance<10:
    return 100
  fuel = distance*10
  return int(fuel)

#test
#print(calculate_fuel(10))