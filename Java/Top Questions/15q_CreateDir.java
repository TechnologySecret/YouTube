// Q1. Create a Directory In Java.

import java.util.*;
import java.io.File;
// In this example we are discuss about file I/O in Java 

class CreateDirectory{
    public static void main(String args[]){
    
     // Uncomment this for a test path
        File dir = new File("D://Learning File//BCA//BCA 3rd Sem//JAVA OOP//allpraque//DemoFile");

// OR LOCATION CHANGE
        // Example for Program Files (might require admin privileges)
        // File dir = new File("C://Program Files//Java//DemoFile");

        // Use mkdirs() to create directories along with parents
        boolean isDirectoryCreated = dir.mkdirs();

        if (isDirectoryCreated)
            System.out.println("Directory Created Successfully");
        else
            System.out.println("Directory Not Created! Error or Directory Already Exists.");
        }
}
