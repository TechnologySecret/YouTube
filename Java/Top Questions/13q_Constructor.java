// Q1. In this Post we are find an example of constructor. 

class Constructor1{
    Constructor1(){
        System.out.println("Constructor Methods Called");
    }
    public static void main(String args[]){
        System.out.println("This is Example of Constructor ");
    }
    Constructor1 object = new Constructor1();         //creating object
}

PS D:\Learning File\BCA\BCA 3rd Sem\JAVA OOP\allpraque> java Constructor1
This is Example of Constructor 

// Q2.  We have created the a student details where student class that have two parameters, 
// We can have  any numbers of parameters in the constructor

class Student4{
    int id; 
    String name; 
    Student4(int i, String n){
        id = i;
        name = n;
    }

    void display(){
        System.out.println("Your Roll No is :-"+id+" and Name is "+ name);
    }
    public static void main(String args[]){
        Student4 s1= new Student4(111,"Shailesh");
        Student4 s2= new Student4(369,"Anshu");
        s1.display();
        s2.display();
    }
}

