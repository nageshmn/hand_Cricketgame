import random #Hand Cricket Game 
sum=0
count=0
count6=0
count_4=0
l=[]
i=0
while True:
  computer_score=random.randint(1,6)
  #2
  gamer=int(input('score your Run! inbetween 1 to 6 '))
  l.append(gamer)
  i+=1
  if gamer>6:
    print('sorry! game has been ended since u scored more than 6 run')
    break
  if i>3:     #'Consecutive last three runs are same
    if l[-1]==l[-2]==l[-3]:
      computer_score=gamer
  
  if computer_score!=gamer:
    if gamer==6:
     count6+=1
    if gamer==4:
     count_4+=1
    sum=sum+gamer
    count+=1
    print(f'till now u have scored {sum} runs')
    
    
  else:
    count+=1
    print(f'OUT! u r score is {sum} in {count} balls! boundaries 6 X{count6} times ! 4 X{count_4} times')
    break
