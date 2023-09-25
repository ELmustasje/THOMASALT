import java.net.*;
import java.io.*;

class app{
    public static void main(String[] args) {
        try {
            URL oracle = new URL("http://www.oracle.com/");
            BufferedReader in = new BufferedReader(new InputStreamReader((oracle.openStream()))); 
             String inputline;
        while ((inputline = in.readLine())!=null)
            System.out.println((inputline));
        } catch (MalformedURLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

       
    }
}   

    
