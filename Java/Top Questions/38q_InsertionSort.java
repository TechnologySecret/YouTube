// Q1. WAP in Python Insertion Sort in Python.
import java.util.*;
import java.util.Scanner;

class InsertionSort{            // CLass InsertionSort
    public static void sort(int arr[]){ // Insertion Sort Function
        int N = arr.length;     // length of the array
        int i,j,temp;

        for(i =1; i < N; i++){      //Start from the second elements 
            j=i;
            temp=arr[i];        //store the current element 

//Shift larger the current elements 
            while(j > 0 && temp < arr[j - 1]){  
                arr[j] = arr[j-1];
                j= j-1;
            }
            arr[j] = temp;      //Place the element in the correct postion
        }
    }

// Main Methods 
    public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    System.out.println("Insertion Sort Test \n ");

 /* Accept Number of Elements */ 
    System.out.println("Enter Number of Interger elements:- ");   
    int num = sc.nextInt();

    // Declare and initialize the array  
    int[] arr = new int[num];

// Accept Elements
    System.out.println("\n Enter "+ num + " Interger elements:-");
    for(int i=0; i<num; i++){
        arr[i] = sc.nextInt();
    }
    sort(arr);          // Call Methods sort
    
    // print sorted Array
    System.out.println("\n  Elements after sorting :- ");
    for(int i=0; i<num; i++){
        System.out.print(arr[i]+" ");
    }
    System.out.println();
}
}

