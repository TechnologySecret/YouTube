// Q8. In this Program discuss about , How to convert Binary to Decimal Number.

import java.util.*;
class Binary_Decimal{
    Scanner scan;
    int num;
    void getVal() {  // This function gets the value of the binary number
        System.out.println("Binary to Decimal:");
        scan = new Scanner(System.in);

        System.out.println("\nEnter the binary number:");
        num = Integer.parseInt(scan.nextLine(), 2);  // Correct method name and usage
    }

    void convert() {  // Converts the binary value to decimal and prints it
        System.out.println("Decimal Value is: " + num);
    }

    public static void main(String args[]) {
        Binary_Decimal obj = new Binary_Decimal();
        obj.getVal();   // Correct placement of function calls
        obj.convert();
    }
}

