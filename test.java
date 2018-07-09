import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL; 
import java.util.*;

public class test
{
	public String restConsume() 
	{
          Scanner t=new Scanner(System.in);
		  String str=t.nextLine();
          String output = null;

          String s="";

            try

            {
           
                URL url = new URL("https://mcs-gse00011723.mobileenv.us2.oraclecloud.com/mobile/custom/XXJET_SRC_ASSETS_LIST_PKG/XXJET_QUALITY_IN_PRO?P_USRNAME=James&P_PASSWORD=welcome&P_CHARACTER1="+str+"&P_ASSET_NUMBER=FL1010");

                      HttpURLConnection conn = (HttpURLConnection)url.openConnection();

                      conn.setRequestMethod("GET");

                      conn.setRequestProperty("Oracle-Mobile-Backend-Id", "1782f463-6cb2-4c9b-83bf-bccae08fd32c"); 

					  conn.setRequestProperty("authorization","Basic R1NFMDAwMTE3MjNfTUNTX01PQklMRV9BTk9OWU1PVVNfQVBQSUQ6bzRvdW5neURxLmpsMG0=");

                      conn.setDoOutput(true);     
						if (conn.getResponseCode() != 200) 
						{
                          throw new RuntimeException("Failed : HTTP error code : " +conn.getResponseCode());
                        }
						
                      BufferedReader br =  new BufferedReader(new InputStreamReader((conn.getInputStream())));

                      while ((output = br.readLine()) != null) 
					  {
                          System.out.println("---dfjf--"+output);
                      }           

                         conn.disconnect();

            } 

            catch (MalformedURLException e) 
			{
                      e.printStackTrace();

            } 
			catch (IOException e) 
			{
                      e.printStackTrace();
            }

        return s;

    }  
	public static void main (String args[])
	{
		test t=new test();
		t.restConsume();
	}
}