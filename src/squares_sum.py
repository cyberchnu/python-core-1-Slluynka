def squares_sum(n):
  # Type your code

  result=0
  for i in range (1,n+1):
    result=result+i**2
  return result

#TEST
#print(squares_sum(3))
''' sum=0
i=5
while i<=50:
  sum=sum+i
  i += 1
print(sum)

sum=0
for i in range (5,51):
  sum = sum + i
print(sum)'''
