// Q. Write a Program find Factorial of Number but using recursion methods in Java

import java.io.IOException;         // This line for find error 
import java.io.BufferedReader;      
import java.io.InputStreamReader;   // This line for Accept Input

class factRecursion{
    public static void main(String arg[])throws
    NumberFormatException,IOException{
        System.out.print("Enter an Integer to calculate it's factorial: ");

// Get Input from the User  
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

// Call the recursive funtions to generate factorial 
        int result = fact(num);


        System.out.println(" \nFactorial of " +num+ " is:- "+result);
    }

// function of factorial 
    static int fact(int f){
        if(f <= 1){         //If the number is 1 return 1
            return 1;
        }
        else{
            return f * fact(f-1);       // else call the same function with the value -1
        }  
    }
}
