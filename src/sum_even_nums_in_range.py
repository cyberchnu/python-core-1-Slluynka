def sum_even_nums_in_range(start, stop):
  # Type your code
  sum=0
  for i in range(start, stop+1):
    if i%2 == 0:
      sum=sum+i
  return sum

#test
#print(f'Сума парних чисел = {sum_even_nums_in_range(2,6)}')