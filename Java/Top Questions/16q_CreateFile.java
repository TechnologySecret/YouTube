import java.io.File;
// import java.util.*;
import java.io.IOException;

class CreateFile{
    public static void main(String args[]){
        try{
            File file= new File("D://Learning File//BCA//BCA 3rd Sem//JAVA OOP//allpraque//DemoFile//DTest.txt");
            if(file.createNewFile()){
                System.out.println("Your File Successful Created........ ");
            }
            else
            {
            System.out.println("Error,File Already Exists...");
            }
        }
        catch(IOException ioe){
            ioe.printStackTrace();
        }
    }
}

