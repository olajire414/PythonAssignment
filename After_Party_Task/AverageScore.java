import java.util.Scanner;
public class AverageScore{
public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    
    int totalScore = 0;
    int average = 0;
    
       
   
    for ( int counter =1; counter <= 3;counter++ ){ 
    System.out.println("Enter score");
          int score = input.nextInt();
          totalScore = totalScore + score;
          
          if (score>=90){
          
          System.out.println("You got A");
          }
          else if(score>=80){
           System.out.println("You got B");
          
          }
         else if(score>=70){
          System.out.println("You got C");
         
         }
         else if(score>=60 ){
          System.out.println("You got D");
         
         }
         
         else if(score<=60 ){
          System.out.println("You got F");
         
         }
          else{
          System.out.println("Bring your parent");
         
         }
         
         
    }
    average = totalScore/3;
    System.out.printf("Total score is : %d%n", totalScore);
     System.out.printf("Average score is : %d%n", average);
    
    
    
    }
    }
