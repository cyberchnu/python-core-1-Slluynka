def mean(number):
  # Type your code
  sum=0
  mystr=str(number)
  for i in (mystr):
    inti=int(i)
    sum=sum+inti
  average=sum/len(mystr)
  return average

#test
#print(mean(426))
