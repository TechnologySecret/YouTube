
// Q1. WAP find Garbage value in Memory 

import java.util.*;

class GarbageCollection{

    public static void main(String args[]) throws Exception{
        Runtime rs = Runtime.getRuntime();
        System.out.println("Free Memory in JVM before Garbage Collection = "+rs.freeMemory());
        rs.gc();
        System.out.println("Free Memory in JVM after Garbage Collection = "+rs.freeMemory());
    }
}

