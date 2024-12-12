// Q1. Find Largest and Smallest 

class LargeSmall{
    public static void main(String args[]){
        // arrays of 10 number random
        int numbers[] = new int[]{23,4,46,66,43,25,77,55,77};

        // assign first element of an arrays to largest and smallest 
        int smallest = numbers[0];
        int largest = numbers[0];

        for (int i=1; i<numbers.length; i++){
            if(numbers[i]>largest)      //check largest numbers
            largest = numbers[i];

            else if(numbers[i]< smallest)       //check smallest numbers
            smallest = numbers[i];
        }
        System.out.println("Largest Number is: "+largest);
        System.out.println("Smallest Number is: "+smallest);
    }
}