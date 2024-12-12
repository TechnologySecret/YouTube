// Q1. WAP find a Leap Year in Java

import java.util.*;
import java.util.Scanner;

class LeapYr{
    public static void main(String args[]){

        // Enter Year we want to check
        System.out.println("Enter Random Year Check for Leap:- ");
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();

        // if year is divisible by 4, it is a leap year.

        if((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0))){
            System.out.println("Year " + year + " is a leap Year");
        }
        else{
            System.out.println("Year " + year + " is a not leap Year");
        }

        
    }
}