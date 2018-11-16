print("===========>welcome in  calculator v1.0 <============")
n1 = int(input("please enter the first numer:"))
n2 = int(input("plaece eter the second number:"))

total=0
menu =input("please chose form the menu \n1)[+]\n2)[-]\n3)[*]\n4)[/]\n")
if menu is '1':
    total=n1 + n2
    print("Reasul is=",total)
elif menu is '2':
    total=n1 - n2
    print("Reasul is=",total)
elif menu is '3':
    total=n1 * n2
    print("Reasul is=",total)
elif menu is '4':
  while n1!=0 and n2!=0:
      total= n1 / n2
      print("Reasul is=",total)
      break;
  else:
      print("you can't divide by zero ")
else:
    print("Error,the character dose not exit")