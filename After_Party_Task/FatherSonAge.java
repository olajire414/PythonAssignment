//Pseudocode For Question 1
//
//the age range is between 1 to 80
//first of all collect the two ages of the father and son
//then if the father age is 
//twice more or more than twice the sonagewe can get the year the 
//father turned twice the age of 
//son by multiplying the age of son by 2 
//then minus it from father age it will give  
//the exact year the father became twice as old asthe son age

import java.util.Scanner;
public class FatherSonAge{
public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    

        System.out.println("Enter age between 1 to 80");
        
        System.out.print("Enter father age ");
        int fatherAge = input.nextInt();
        
        System.out.print("Enter son age ");
        int sonAge = input.nextInt();
        
   System.out.printf("Father was twice old: %d%n%s%n",fatherAge-(sonAge*2),"years ago");
        
   System.out.printf("Father will be twice old in the next: %d%n%s%n",(sonAge*2)-fatherAge,"years" );
}
}
