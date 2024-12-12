
// Q1:  WAP copy a array number from A1 to A2 . 

class ArrayCopy {
    public static void main(String args[]) {
        int A1[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int A2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        
        System.out.println("The first Array is: -");
        for (int i = 0; i < A1.length; i++) {  // Changed <= to <
            System.out.print(A1[i] + " ");
        }

        System.out.println("\nThe Second Array is:- ");
        for (int i = 0; i < A2.length; i++) {  // Changed <= to <
            System.out.print(A2[i] + " ");
        }

        // Copy last 5 elements of A1 to A2 starting at index 5
        System.arraycopy(A1, 5, A2, 5, 5);

        System.out.println("\nThe Second Array after calling arraycopy(): ");
        for (int i = 0; i < A2.length; i++) {  // Changed <= to <
            System.out.print(A2[i] + " ");
        }
    }
}
