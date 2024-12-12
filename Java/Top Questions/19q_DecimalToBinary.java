import java.util.*;

class DecimalToBinary{
    public String toBinary(int n){
        if(n ==0){
            return "0";
        }
        String binary =" ";
        while (n>0){
            int rem = n%2;
            binary = rem + binary; 
            n = n/2;
        }
        return binary;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Number :- ");
        int decimal  = sc.nextInt();


        DecimalToBinary dtb = new DecimalToBinary ();
        String binary = dtb.toBinary(decimal);
        System.out.println("The Binary To Decimal Value:- "+binary);
    }
}