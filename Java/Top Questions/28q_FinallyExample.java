// Q. Write a program in java where find finally example 
import java.util.*;

// class FinallyExample{
//     public static void main(String args[]){
//         try{
//             int[] numbers = {1,2,3,4};
//             System.out.println(numbers[6]);     //Error Index OutOfBound Exceptions
//         } catch (ArrayIndexOutOfBoundsException e){
//             System.out.println("Exception Caught:"+ e.getMessage());
//         } finally {
//             System.out.println("This will always be excuted");
//         }
//         System.out.println("Program Continues............ ");
//     }
// }



// Q2. Print a Random Object in Java using finally keywords
class FinallyExample {
    public static void main(String args[]) {
        new FinallyExample().doTheWork();
    }
    public void doTheWork() {
        Object o = null;
        for (int i = 0; i < 10; i++) { // Assuming the loop should run 10 times
            try {
                o = makeObj(i);
            } catch (IllegalArgumentException e) {
                System.out.println("Error:(" + e.getMessage() + ").");
                return;
            } finally {
                System.out.println("All Done");
                if (o == null) {
                    System.out.println(0);
                }
            }
        }
    }
    
    public Object makeObj(int type) throws IllegalArgumentException {
        if (type == 1) {
            throw new IllegalArgumentException("Don't like type " + type);
        }
        return new Object();
    }
}

