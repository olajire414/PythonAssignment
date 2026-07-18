total_score = 0
average = 0
counter = 0
    
       
while counter < 3:
 
    print ("Enter score between 1 and 100")

    score =int(input("Enter score: " ))

    total_score = total_score + score
  
    if 90 <= score <= 100:
        print("You got A")
  
    elif 80 <= score <= 90:
        print("You got B")
  
    elif 70 <= score <= 80:
        print("You got C")
 
    elif 60 <= score <=70:
        print("You got D")
 
    elif 0 <= score <= 60:
        print("You got F") 
    else:
        print("Bring your parent")
    counter +=1    
 
 

average = total_score / 3;
print("Total score is : ", total_score)
print("Average score is : ", average)





