// Q1. Print a simple example of for loop 
import java.util.Scanner;

class forLoop{
    public static void main(String args[]){

// Step 1:
        // for (int i=1; i< 100; i++){
        //     System.out.print(i +",");
        // }

// Step 2: Get Last Input User
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter Last Input Number:- ");
    int num = sc.nextInt();

      for (int i=1; i<= num; i++){
            System.out.print(i + " ");
        }


    }
}