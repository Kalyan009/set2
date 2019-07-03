num=int(input())
if num>0:
  for i in range(2,num):
    if(num%i)==0:
      print("no")
      exit
    else:
      print("yes")
      exit
else:
  print("invalid")
  exit
