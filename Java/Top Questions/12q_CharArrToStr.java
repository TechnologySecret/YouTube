import java.util.*;

class CharArrayToString{
    public static void main(String args[]){
        char[] charArray =  new char[] {'J','a','v','a'};    // Character in Array Formate 

        // To convert char array to string in java,
        //  use String(Char[] ch) constructor of Java String class. 

        String str= new String(charArray);  // Convert 
        System.out.println("Character Array To Converted to String:- "+str); 
    }
}

