// Q2. Write a Program Sum of 2 Number. 

import java.util.*;
class Add{
    public static void main(String args[]){
        System.out.println("Enter 1st Number:");
        Scanner in = new Scanner(System.in);
        int num1 = in.nextInt();

        System.out.println("Enter 2nd Number:");
        int  num2 = in.nextInt();

        int sum=  num1+num2;
        System.out.print("Two Number sum is :"+ sum);

    }
}

