import java.util.*;

class LargestNum{
    public static void main(String args[]){
        int x,y,z;

        System.out.println("Enter Three Num Integer: ");
        Scanner sc= new Scanner(System.in);

        x= sc.nextInt();
        y= sc.nextInt();
        z= sc.nextInt();

        if(x > y && x > z){
            System.out.println("1st is Largest Numbers");
        }
        else if(y > x && y > z){
            System.out.println("2nd is Largest Numbers");
        }
        else if(z > x && z > y){
            System.out.println("3rd is Largest Numbers");
        }
        else{
            System.out.println("Entered numbers are not distinct.");
        }
    }
}