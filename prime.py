num=int(input())
if num>0:
  for i in range(2,num):
    if(num%i)==0:
      printf("no")
    else:
      printf("yes")
else:
  print("invalid")
