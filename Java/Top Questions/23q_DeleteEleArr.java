// Q1. Write a program where Delete an element from a Array

class DeleteArray{
    public static void main(String args[]){
        int arrlist[] = {4,5,6,7,8,9};
        int position  = 3 ; 


// Print a array list
        for(int k=0; k<arrlist.length; k++){            
            System.out.println(arrlist[k]);
        }


// Create a Loop delete element from a list of array .
        for(int i =0; i<arrlist.length; i++){
            if(position == i){
                for(int j=i+1; i<arrlist.length -1; j++){
                    arrlist[i] = arrlist[j];
                    i++;
                }
            }
        }
                System.out.println("The Output of Array After Delete Elements: "+position+" is not in list now.");
        for(int i =0; i<arrlist.length-1; i++){
            System.out.println(arrlist[i]);
        }

    }
}