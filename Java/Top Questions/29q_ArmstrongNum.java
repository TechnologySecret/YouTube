// Q1. Write a program find Armstrong Number in Java.


// NOte:  153: This is an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.   


import java.util.Scanner;
import java.util.*;

import java.util.Scanner;

class ArmstrongNumber {
    public static void main(String arg[]) {
        int num, sum = 0, temp, remainder, digits = 0;

        Scanner in = new Scanner(System.in);
        System.out.println("Input a Number to check if it is an Armstrong Number: ");
        num = in.nextInt();
        in.close();

        temp = num; 

        // Count number of digits
        while (temp != 0) {
            digits++;
            temp = temp / 10;
        }
        temp = num;

        while (temp != 0) {
            remainder = temp % 10;
            sum = sum + power(remainder, digits);
            temp = temp / 10;
        }

        if (num == sum) {
            System.out.println(num + " is an Armstrong Number.");
        } else {
            System.out.println(num + " is not an Armstrong Number.");
        }
    }

    static int power(int num, int r) {
        int c, p = 1; 
        for (c = 1; c <= r; c++) { 
            p = p * num;
        }
        return p;
    }
}

