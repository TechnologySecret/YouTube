// Q1. Convert Decimal To HexaDecimal


import java.util.*;
class Decimal_Hexa{
    int num; 
    void getVal(){
        System.out.println("Decimal To HexaDecimal:-");
        Scanner sc = new Scanner(System.in);

        System.out.println("\n Enter The Number:-");
        num = Integer.parseInt(sc.nextLine()); 
    }
    void convert(){
        String hexa = Integer.toHexString(num);
        System.out.println("Hexa Decimal Value is:- "+hexa);
    }
    public static void main(String args[]){
        Decimal_Hexa obj = new Decimal_Hexa();
        obj.getVal();
        obj.convert();
  }
}
