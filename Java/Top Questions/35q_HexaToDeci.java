// WAP print Hexa_Decimal to Decimal 


import java.util.Scanner;



class Hexa_Decimal{
    int num;
    void getVal(){
        System.out.println("Covert HexaDecimal To Decimal");
        Scanner sc= new Scanner(System.in);
        
        System.out.println("Enter HexaDecimal number  :- ");
        num = Integer.parseInt(sc.nextLine(), 16);
        sc.close();

    }

    void convert(){
        String decimal = Integer.toString(num);
        System.out.println("Decimal Value is:"+decimal);
    }
    
    public static void main(String args[]){
        Hexa_Decimal  obj = new Hexa_Decimal();
        obj.getVal();
        obj.convert();
    }
}