// Q6. WAP where use SUm of Average numbers

class ArrayArray{
    public static void main(String arg[]){
        // define an array
        int[] numbers = new int [] {10,20,30,40,50};

        // calculate sum of all array elements
        int sum =0; 
        
        for (int i= 0; i< numbers.length; i++){
            sum = sum + numbers[i];
        }

        // calculate average value
        double average = sum/numbers.length;

        System.out.println("Average value of array elements is:"+average);
    }
}

