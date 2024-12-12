import java.util.*;

interface Info{
    static final String language = "Java";
    public void display();
}

class Simple implements Info{
    public static void main(String args[]){
        Simple obj = new Simple();
        obj.display();
    }
    // Defining Methods declared in Interface

    public void display(){
        System.out.println(language + " is awesome");
    }
}

