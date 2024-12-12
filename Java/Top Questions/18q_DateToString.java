import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.*;

class DateToString{
    public static void main(String arg[]){
        Date date = new Date();

        // To Conver java.util.Date to String.use SimpleDateFormat class

        DateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");

        // to Convert Date to String, use formate method of SimpleDateFormat class

        String strDate = dateFormat.format(date);

        System.out.println("Date Converted to String:" + strDate);

    }

}