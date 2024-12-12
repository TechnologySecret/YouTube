// Q3. Write a Program Area of Circle ? 
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// Hack1. 
/** * 
class CircleArea{
    public static void main(String arg[]){
        int raduis = 0; 
        System.out.println("Please Enter Raduis of a Circle: ");
        try{
            // get the raduis from console
            BufferedReader br= new
            BufferedReader(new InputStreamReader(System.in));
            raduis = Integer.parseInt(br.readLine());
        }

        // if invailed value was entered 
        catch(NumberFormatException ne){
            System.out.println("Invailed raduis value"+ne); 
            System.exit(0);
        }
        catch(IOException ioe){
            System.out.println("IO Error: "+ ioe);
            System.exit(0);
        }
        double area = Math.PI * raduis* raduis;
        System.out.println("Area of Circle is:"+ area);
    }
}

***/

// Hack 2:

class CircleArea1{
    public static void main(String arg[]){
        int raduis;

        System.out.println("Please Enter Raduis of a Circle: ");
        Scanner in = new Scanner(System.in); 
        raduis = in.nextInt();

        double area = 3.14 * raduis*raduis; 
        System.out.println("Area of Circle is :"+ area);
    } 
}
