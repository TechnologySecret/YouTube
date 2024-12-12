// Q1. Covert Decimal to OCtal Number

import java.util.*;
class Decimal_Octal{
    int num; 
    void getVal(){
        System.out.println("Decimal To Octal:-");
        Scanner sc = new Scanner(System.in);

        System.out.println("\n Enter The Number:-");
        num = Integer.parseInt(sc.nextLine()); 
    }
    void convert(){
        String octal = Integer.toOctalString(num);
        System.out.println("OCtal Decimal Value is:- "+octal);
    }
    public static void main(String args[]){
        Decimal_Octal obj = new Decimal_Octal();
        obj.getVal();
        obj.convert();
  }
}
