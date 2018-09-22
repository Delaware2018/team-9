import java.util.*;
import java.io.*;

public class CSVReader{

    public static void main(String[] args){
        String csvFile = "";
        String line = "";

        try(BufferedReader br = new BufferedReader(new FileReader(csvFile))){
        
            while((line = br.readLine()) != null){
                String [] donor = line.split(",");
                int output = donor[9];

                
            }
        }
    }

}


