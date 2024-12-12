// Q9. Write a Program find additon of two number using bitwise operators. 

import java.util.*;

class AddBitwise{
    static int add(int a, int b){
        int carry;
        while( b!=0){
            carry = a&b;  //Calculate carry
            a= a^b;       // Sum without carry
            b= carry<<1;   // Shift carry to the left
        }
        return a;

    }
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the Number to be added:");
        
        int a= input.nextInt();
        int b= input.nextInt();

        System.out.println("The Sum of Both Number:"+add(a,b));

        input.close();
    }
}
