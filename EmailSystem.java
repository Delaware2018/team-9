import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;


class Person{
    private String name;
    private String emailAddr;
    private String phoneNum;
    private String university;


    public Person(String name1, String emailAddr1, String phoneNum1, String university1){
        this.name = name1;
        this.emailAddr = emailAddr1;
        this.phoneNum = phoneNum1;
        this.university = university1;
    }

    public String getName(){
        return name;
    }

    public String getEmail(){
        return emailAddr;
    }
    
    public String getPhoneNum(){
        return phoneNum;
    }
    
    public String getUniversity(){
        return university;
    }

    public void printInfo(){
        System.out.println("Name: " + name + "\nEmail: " + emailAddr + "\nPhone Number: " +  phoneNum + "\nUniversity: ");
    }

}
public class EmailSystem{

    public static void main(String[] args){
        String csvFile = "/home/andrea/CodeForGood/team-9/Sample_data.csv"; // name of csv
        String line = ""; //each line being read
        Map<String,ArrayList<Person>> cohorts = new HashMap<>();

        try(BufferedReader br = new BufferedReader(new FileReader(csvFile))){
            String first_line = br.readLine();
            
            while((line = br.readLine()) != null){ // reads each line
                String [] donor = line.split(","); //puts it into an array
                String zip = donor[11]; // zipcode location
                String email = donor[3];
                String name = donor[1] + donor[2];
                String phone = donor[4];
                String uni = donor[6];

                ArrayList<Person> emailList = new ArrayList<Person>();
                
                if (cohorts.containsKey(zip)){
                    ArrayList<Person> copyEmails = cohorts.get(zip);
                    copyEmails.add(new Person(name, email, phone, uni));
                    cohorts.put(zip, copyEmails);
                }
                else{ 
                emailList.add(new Person(name, email, phone, uni));
                cohorts.put(zip, emailList);
                
                }
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(cohorts);
    }


}


