#Pseudocode For Question 1

#the age range is between 1 to 80
#first of all collect the two ages of the father and son
#then if the father age is twice more or more than twice the son age
#we can get the year the father turned twice the age of son by multiplying the age of son by 2 then minus it from father age it will give us the exact year the father became twice as old as the son age

print("Enter age between 1 to 80")

current_father_age = int(input("enter father age: "))

current_son_age = int(input("enter father age: "))

print("Father was twice old",current_father_age-current_son_age*2,"years ago" )

print("Father will be twice old in the next ",(current_son_age*2)-current_father_age,"years" )
