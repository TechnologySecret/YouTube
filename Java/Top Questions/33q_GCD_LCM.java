// Q1. Find a program the formulas and examples for calculating the Greatest Common Divisor (GCD) and Least Common Multiple (LCM).

// GCD: Formula
// For two numbers a and b, the GCD is calculated as follows: 

// Formula: GCD(a,b) = GCD(b,a%b)

// LCM: Formula
// For two numbers a and b, the LCM is calculated using their GCD as follows:

// Formula: LCM(a,b) = |a,b} /GCD(a,b)

import java.util.*;

class gcd_Lcm{
    static int gcd(int x, int y){
        int r = 0;
        int a = (x > y) ? x:y;    // a is greated number of b 
        int b = (x < y) ? x:y;    // b is greated number of a

        r = b; 
        while (a % b != 0){
            r= a %b;
            a= b;
            b= r;
        } 
        return r;
    }

    static int lcm(int x, int y){
        int a;
        a = (x>y) ? x: y;   // a is grater number
        while (true){
            if(a % x  == 0 && a % y ==0 )
            return a;
            ++a;
        }
    }

    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the two numbers: ");
        
        int x = sc.nextInt();
        int y = sc.nextInt();

        System.out.println("The GCD of two number:- " + gcd(x, y));
        System.out.println("The LCM of two number:- " + lcm(x, y));    
   }
}

