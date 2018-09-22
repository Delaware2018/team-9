import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;

public class EmailSystem{

    public static void main(String[] args){
        String csvFile = "/home/andrea/CodeForGood/Sample_data.csv"; // name of csv
        String line = ""; //each line being read
        Map<String,ArrayList<String>> cohorts = new HashMap<>();

        try(BufferedReader br = new BufferedReader(new FileReader(csvFile))){
            String first_line = br.readLine();
            
            while((line = br.readLine()) != null){ // reads each line
                String [] donor = line.split(","); //puts it into an array
                String zip = donor[11]; // zipcode location
                String email = donor[3];
                ArrayList<String> emailList = new ArrayList<String>();
                
                if (cohorts.containsKey(zip)){
                    ArrayList<String> copyEmails = cohorts.get(zip);
                    copyEmails.add(email);
                    cohorts.put(zip, copyEmails);
                }
                else{ 
                emailList.add(email);
                cohorts.put(zip, emailList);
                System.out.println(zip);
                }
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(cohorts);
    }


}


