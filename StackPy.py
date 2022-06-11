# python program to implement stack as a list
def push(stk,item):
    stk.append(item)
    print("Element Pushed Successfully")
def pop(stk):
  if stk==[]:
      print("Underflow-No item in stack for deletion")
  else:
          item=stk.pop()
          print("Popped Element is ",item) 
def display(stk):
    if stk==[]:
        print("stack is empty")
    else:
     for a in range(len(stk)-1,-1,-1):
         print(stk[a],'  ',end=' ')
stack=[]
while True:
  print("\nStack Operations")
  print("1.Push")
  print("2.Pop")
  print("3.Display")
  print("4.Exit")  
  ch=int(input("Enter your choice(1-4)"))
  if ch==1:
    item=int(input("Enter item:"))
    push(stack,item)
  elif ch==2 :
    item=pop(stack)
  elif ch==3:
        display(stack)
  elif ch==4 :
        break
  else:
        print('Invalid Choice')
