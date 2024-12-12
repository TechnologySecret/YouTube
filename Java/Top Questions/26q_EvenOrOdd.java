// Q1. Write a program in where find enter number is even ot odd
import java.util.*;


class  EvenOdd{
    public static void main(String arg[]){
        // int num; 
        System.out.println("Enter a Random Number Find Even Or Odd:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        if(num %2==0){
            System.out.println("This is Even Number");
        }
        else{
            System.out.println("This is Odd Number");
        }
    }
}

