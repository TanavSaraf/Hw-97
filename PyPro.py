import random
randomNo = random.randint(0, 10)
inputss = int(input("Enter a guess between 1-9:"))
chances = 5
if inputss < 10:
    if(inputss==randomNo):
        print("you won")
    else :
        print("4 chances more to change your destiny")
        inputss = int(input("Enter a guess between 1-9:"))
        chances=4
        if(inputss==randomNo):
            print("you won")
        else :    
                print("3 chances more to change your destiny")
                inputss = int(input("Enter a guess between 1-9:"))
                chances=3
                if(inputss==randomNo):
                    print("you won")
                else :    
                            print("2 chances more to change your destiny")
                            inputss = int(input("Enter a guess between 1-9:"))
                            chances=2
                            if(inputss==randomNo):
                                print("you won")
                            else :    
                                    print("1 chances more to change your destiny")
                                    inputss = int(input("Enter a guess between 1-9:"))
                                    chances=1
                                    if(inputss==randomNo):
                                        print("you won")  
                                    else :
                                        print("you successfully lost this game :-)")
                                        print()
                                        print("the answer was :",randomNo)
         
   
else:
    print("Can you not follow instructions!")
# elif (inputss!=randomNo and chances==4):
  #   print("3 chances more to change your destiny")
 #elif (inputss!=randomNo and chances==3):
   #  print("2 chances more to change your destiny")
 #elif (inputss!=randomNo and chances==2):
    # print("1 chances more to change your destiny")
 #elif (inputss!=randomNo and chances==1):
     #  print("YOU SHOULD HAVE BEEN CAREFUL ")    
 #else :
      #print("you won")
