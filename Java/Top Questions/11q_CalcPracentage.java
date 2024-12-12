// Q1. WAP where PrecentageCalculator of two Numbers. 

import java.util.*; 

class PrecentageCalculator{
    public static void main(String args[]){
        
        double x, y=0; 

        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the Current Amount of Product (x):-");
        x =sc.nextDouble();
        System.out.println("Enter Precentage How Many Amount of add (y):-");
        y =sc.nextDouble();


//  PrecentageCalculator Formula ****************
        double result = (x / 100) * y;
// PrecentageCalculator ****************

        System.out.println("\nCalculating Precentage: (x % of y): -");
        System.out.println(x + " % of " + y + " is disccount " + result);
        System.out.println();
    }
}


PS D:\Learning File\BCA\BCA 3rd Sem\JAVA OOP\allpraque> java PrecentageCalculator
Enter the Current Amount of Product (x):-
100
Enter Precentage How Many Amount of add (y):-
20

Calculating Precentage: (x % of y): -
100.0 % of 20.0is disccount 20.0
