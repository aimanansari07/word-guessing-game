letters = [
    ['h', 'o', 'l', 'i', 'd', 'a', 'y'],
    ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'],
    ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],
    ['f', 'l', 'o', 'w', 'c', 'h', 'a', 'r', 't'],
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p', 'e', 's']]

words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping", "pong", "pram", "prom", "ramp"],
    ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "mop", "act", "bat", "camp", "comb", "boom", "pact",
     "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow", "fowl", "wolf", "crow",
     "half"],
    ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape", "cope", "crap", "crew",
     "crop", "pace"]]

level = 0
lives = 5
Score=0
count=0


while level<len(letters):
    if lives>0:
        print("level 1")
        print("create three word using given letters ")
    
        for letter in letters[0]:
         print(letter,end=" ")
        print()
        
        while count<3:
           word=input("Enter a word ").lower()
           
           if word in words[0]:
              count+=1
              Score+=1
              level+=1
              
           else:
              print('wrong guess')
              Score-=1
              lives-=1
              print("your remaining lives are ",lives)
             
              if lives==0:
               break
        else:
                 choice=print('you want to continue (y/n)'.lower())
                 if(choice=='y'):
                  level+=1
                 else:
                  print("thanks for playing your score is ",Score)
                 break
    else:
       print("Game Over your score is  ",Score)
       break

if level==5:
 if lives > 0:
       print("Congratulations! You have completed all levels!")
       print(f"Your Score is : {Score}")
           


              
               
             




   
    



 


