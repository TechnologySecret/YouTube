// Q4 : FInd area of rectangle value ( Formal : Area= width*length)

import java.io.BufferedReader;
import java.io.IOException; 
import java.io.InputStreamReader;

class AreaR{
    public static void main(String[] args){ 
        int width = 0; 
        int length = 0;
    
    try {
        // read the length from console

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Please enter length of a rectangle: -");
            width = Integer.parseInt(br.readLine());

            System.out.print("Please enter width of a rectangle: -");
            length = Integer.parseInt(br.readLine());


    }
    // if Invailed value was entered

    catch(NumberFormatException ne){
            System.out.println("Invailed value" + ne);
            System.exit(0);

    }
    catch(IOException ioe){
            System.out.println("IO Error: "+ ioe);
            System.exit(0);
    }
        int area = length*width;
        System.out.println("Area of Rectangle value is:" + area);


    }
}

