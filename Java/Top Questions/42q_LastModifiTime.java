// Q1. WAP in Java Find LAst LastModification Time in Java
import java.io.File;
import java.util.Date;
class GetLastMod{
    public static void main(String args[]){
        File file = new File("D://Learning File//BCA//BCA 3rd Sem//JAVA OOP//allpraque//DemoFile");
        
        long lastModified = file.lastModified();
        
        System.out.println("File was modified at :- " + new Date(lastModified));
    }
}
