// Q1. WAP of student check pass or not


import java.util.*;
import java.util.Scanner;

class ifElse{
    public static void main(String args[]){
        int passingMark=40;
        Scanner sc = new Scanner(System.in);
            System.out.println("Enter Marks of Student:- ");
            int marksOb = sc.nextInt();

            if(marksOb >= passingMark){
                System.out.println("You are Passed this Exam:");
            }
            else{
                System.out.println("Oh Sorry!!, You are failed this Exam: Please try again ");
            }
    }
}
