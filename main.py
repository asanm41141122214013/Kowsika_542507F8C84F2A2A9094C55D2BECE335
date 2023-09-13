#python pattern programs
n=5
px=n
py=n
for  x in range (1,n+1):
  for y in range (1,n*2):
    if y==px or y==py or x==n:
      print("*",end=""):
    else:
      print("",end=""):
  py=1
  px+=1
  print()
