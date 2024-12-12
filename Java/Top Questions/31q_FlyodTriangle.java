// Q1. Write a program in Java find Patten of trinagle size

import java.util.Scanner;

class FloydTrangle{
    public static void main(String arg[]){

        int num =1 ; 
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of rows of flyod's trinagle you want:");
        int number = sc.nextInt();

        System.out.println("Flyod's trinagle: - ");

        for(int i= 1; i <=number; i++ ){
            for(int j = 1; j<=i; j++){
                System.out.print(num+" ");   //Print Numeric Number
                // System.out.print("*");      //Print Stick Pattern
                num++;
            } 
            System.out.println();
            
        }
    }
}



