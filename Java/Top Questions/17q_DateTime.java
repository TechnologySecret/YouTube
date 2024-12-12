import java.util.*;

class CurrentDateTime{

    public static void main(String args[]){
        int day, month, year;
        int sec, min, hour;

        GregorianCalendar date = new GregorianCalendar();

        day = date.get(Calendar.DAY_OF_MONTH);
        month = date.get(Calendar.MONTH);
        year = date.get(Calendar.YEAR);

        sec = date.get(Calendar.SECOND);
        min = date.get(Calendar.MINUTE);
        hour = date.get(Calendar.HOUR);

        System.out.println("Current Date is:- " + day+ "/"+(month+1)+"/"+ year);
        System.out.println("Current Time is:- " + hour+ ":"+min+":"+ sec);   
    }
}
