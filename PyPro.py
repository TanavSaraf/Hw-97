import random 
randomNo=random.randint(0,10)
inputss=int(input("Enter a guess between 1-9:"))
chances=5
if inputss<10 : 
    
   
    if(inputss!=randomNo and chances==5):
        print("4 chances more to change your destiny")
        
    elif (inputss!=randomNo and chances==4):
        print("3 chances more to change your destiny")
    elif (inputss!=randomNo and chances==3):
        print("2 chances more to change your destiny")
    elif (inputss!=randomNo and chances==2):
        print("1 chances more to change your destiny")
    elif (inputss!=randomNo and chances==1):
          print("YOU SHOULD HAVE BEEN CAREFUL ")    
    else :
         print("you won")
        
        
else :
    print("Can you not follow instructions!")