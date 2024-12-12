// Q1. Write a Program in DSA Linear Search in Java. 

import java.util.Scanner;

class LinearSearch{
    public static void main(String args[]){

        int i, num, search, array[];

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number of Elements: ");
        num = sc.nextInt();

        array = new int[num];

        System.out.print("Enter "+ num + " Integers:- ");

        for( i= 0; i<num; i++){
            array[i] = sc.nextInt();
        }
        System.out.println("Enter Value to find:- ");
        search = sc.nextInt();

        for(i=0; i<num; i++){
            if(array[i] == search){          /* Searching element is present*/ 
            System.out.println(search + " is present at location " +(i+1)+ ".");
            break;
            }
        }
        if(i == num){       //Searching element is absent
            System.out.println(search +  "is not present in array.");
        }
    }
}