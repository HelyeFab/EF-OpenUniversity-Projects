
/**
 * Write a description of class Heater here.
 *
 * @author EFabiani
 * @version 01_16_10_2024
 */
public class Heater
{
    //instance variables- replace the example below with your own
    private double temperature;
   

    /**
     * Constructor for objects of class Heater
     */
    public Heater()
    {
        // initialise instance variables
        temperature=15.0;
       
    }
    
    public void makeWarmer(){
        temperature +=5.0;

    }
    
    public void makeCooler(){
        temperature -= 5.0;
    
    }
    
    public double getTemperature(){
        return temperature;
    }
}
