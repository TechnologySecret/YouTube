// Q1. WAP where delete a directory from a drive
import java.util.*;
import java.io.File;

class DelFolder{
    public static void main(String args[]){
        File file = new File ("D://Learning File//BCA//BCA 3rd Sem//JAVA OOP//allpraque//DemoFile");  
         
        boolean folDeleted = file.delete();   // File and Folder delete methods uses .

        if(folDeleted){
            System.out.println("Folder Successfully Deleted ");
        }
        else{
            System.out.println("Not Found File !!!!");
        }
    }
}