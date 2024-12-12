// Q. Write a program simple find factorial of a random number get input

import java.util.*;
import java.util.Scanner;

class factorialNum{
    public static void main(String arg[]){
        int num,i,factNum=1;          //Declaration of all variable
        
        System.out.println("Enter a Number for Factorial: ");
        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();
        if(num <= 0)
            System.out.println("Number Should be neagtive.");
        else
        {
        for (i=1; i<=num; i++)
        factNum *= i;           //this is only logic for factorial down

        System.out.println("Factorial of "+num+ " is :"+factNum);
        }
        sc.close();

    }
}

