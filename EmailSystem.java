import java.util.*;
import java.io.*;

public class EmailSystem{

    public static void main(String[] args){
        String csvFile = "/home/andrea/CodeForGood/team-9"; // name of csv
        String line = ""; //each line being read
        Map<String,String> cohorts = new HashMap<>();

        try(BufferedReader br = new BufferedReader(new FileReader(csvFile))){
            String first_line = br.readLine();
            while((line = br.readLine()) != null){ // reads each line
                String [] donor = line.split(","); //puts it into an array
                String zip = donor[11]; // zipcode location
                String email = donor[3];
                
                cohorts.put(zip, email);
    
            }
        }
        System.out.println(cohorts);
    }

}


