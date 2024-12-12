// Q1. In this Questions we are disccuss here a important example of continue Statements. 

class ContinueS{
    public static void main(String args[]){

// In this example we are used for skip one words and 
// the particular iteration print of the example

int intArray[] = new int[]{1,2,3,4,5};  
System.out.println("All numbers exact for 3 are: -");
for (int i=0; i<intArray.length; i++){
    if(intArray[i] == 3)
    continue; 
    else
    System.out.println(intArray[i]);
    }
    }
}

