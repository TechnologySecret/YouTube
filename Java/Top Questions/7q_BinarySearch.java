import java.util.*;   

class BinarySearch{
    public static void main(String args[]){
        int c, first, last, middle, n, search, array[];

        Scanner in = new Scanner(System.in);
        System.out.println("Enter Number of Elements:");
        n= in.nextInt();

        array= new int[n];

        System.out.println("Enter "+ n+ "Intergers:");

        for(c =0; c<n; c++){
            array[c]= in.nextInt();
        }

        System.out.println("Enter Value to find");
        search = in.nextInt();

        first= 0;
        last = n-1;
        middle = (first +last)/2;

        while(first <= last){
            if(array[middle]<search){
                first= middle +1;
            }
            else if (array[middle]== search){
                System.out.println(search +"found at location"+ (middle+1)+" ");
                break;
            }
            else
            last = middle-1;

            middle = (first+ last)/2;
            }
            if(first>last)
            System.out.print(search +" is not present in the list: \n ");
            
    }
}