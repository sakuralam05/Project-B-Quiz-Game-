print("Welcome to Sakura's computer quiz")

playing=input("Do you want to play? ")
score=0
if playing.lower() !="yes":
    quit()
    
print("Okay! Let's Play!")

answer= input("How old is Sakura? ")

if answer.lower()=="19":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
    
answer= input("Which JC did Sakura attend? ")

if answer.lower()=="CJ":
    print("correct!")
    score+=1
else: 
    print("Incorrect!")
    
answer= input("What is my favourute food? ")

if answer.lower()=="Potato Salad ":
      print("Correct!")
      score+=1
else:
    print("Incorrect!")
    
print("You got "+ str(score)+"questions correct!")