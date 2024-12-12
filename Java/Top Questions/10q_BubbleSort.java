import java.util.*; 
import java.util.Random;


class Bubble_Sort{

    static int[] sort(int[] sequence ){
        // Bubble_Sort Proccesure Start

        for (int i = 0; i<sequence.length; i++){
            for (int j = 0; j<sequence.length-1; j++){
                if(sequence [j] > sequence[j+1]){
                    sequence[j]= sequence[j]+sequence[j+1];
                    sequence[j+1] = sequence [j] -sequence[j+1];
                    sequence[j]  = sequence[j] -sequence[j+1];
                }
            }
        }
        return sequence;
    }
    static void printSequn(int[] sorted_sequence){
        for (int i= 0; i<sorted_sequence.length;i++){
            System.out.println(sorted_sequence[i] + " ");
        } 
    }

// Random Number Genrated Program
    public static void main(String args[]){
        System.out.println("Sorting of randomly generatd numbers using BUBBLE SORT");

        Random random = new Random();
        int N = 10;
        int[] sequence = new int[N];
        for(int i=0; i< N; i++ ){
            sequence[i]= Math.abs(random.nextInt(1000));
        }

        System.out.println("\n Orginal Sequence:");
        printSequn(sequence);
        System.out.println("\n Sorted Sequence: ");
        printSequn(sort(sequence));
    }
}
