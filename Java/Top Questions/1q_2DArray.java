// Q4. Write a Program  print 2DArray 
// Program |Code                                                       

import java.util.*;                                                   //import :- java labaries file from java server.   
class TwoDArray{                                                      // class : This is a keyword declare in java it is complasarry. 
    public static void main(String args[]){                           // public : is a access modifier and 
                                                                     // "static" : is also a keyword but static method executed by JVM and save memory. 
                                                                     // " void"  : is return type of method, it means it doesn't return any value 
                                                                    //  "main" :  it is entry point of pragram, start program from here and it is called by runtime system. 
                                                                    // "String arg[]" : it is used to command line argument.  
        int twoD[][]= new int[4][5];
        int k = 0, i, j;
        for (i = 0;  i< 4; i++)
        for (j = 0;  j< 5; j++){
            twoD[i][j] = k; 
            k++;
        }

        for(i =0; i< 4; i++){
            for(j =0; j<5; j++)
            System.out.print(twoD[i][j]+" ");                 
            System.out.println();                                   // System.out.Println():  it is used to print statement. 
        }
    }
}

