def ruler(a):
  line1 = ""
  line2 = ""
  index=1
  for i in range(1,a+1):
    if i%10==0:
      line1=line1+""+str(index)
      index=index+1
    else:
      line1=line1+" "
    line2=line2+str(i%10)