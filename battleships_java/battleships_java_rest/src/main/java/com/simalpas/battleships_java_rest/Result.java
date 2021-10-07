package com.simalpas.battleships_java_rest;
import java.util.*;

/**
 * Records a single result
 * @author simal
 */
public class Result
{
    private final String resultName;
    private final List<Coord> coords;
    
    protected Result(String resultName, List<Coord> coords)
    {
        this.resultName = resultName;
        this.coords = coords;
    }
    
    protected Result(String resultName, Coord coord)
    {
        this.resultName = resultName;
        this.coords = new ArrayList<>();
        this.coords.add(coord);
    }
    
    /**
     * zero arg for returning when a method fails
     */
    protected Result()
    {
        this.resultName = "null";
        this.coords = new ArrayList<>();
    }
    
    protected String getResultName()
    {
        return this.resultName;
    }
    
    protected Coord get1stCoord()
    {
        return coords.get(0);
    }
    
    protected List<Coord> getRestOfCoords()
    {        
        List<Coord> result = new ArrayList<Coord>();
        if (this.coords.size() == 1)
        {
            return result;
        }
        for (int i = this.coords.size() -1 ; i > 0; i--)
        {
            result.add(coords.get(i));
        }
        return result;
    }
    
    protected List<Coord> getAllCoords()
    {
        return coords;
    }
    
    protected Map<String, List<Integer[]>> unpack()
    {
        // create an empty hashmap
        Map<String, List<Integer[]>> result = new HashMap<>();
        // create an entry of an empty list of arrays
        result.put(resultName, new ArrayList<Integer[]>());
        // iterate through the coords, convert to an array
        for (Coord each : coords)
        {
            result.get(resultName).add(each.toArray());
        }
        return result;
    }
    
    @Override
    public String toString()
    {
        String str = "resultName = "
                   + this.resultName
                   + " -> ";
        for (Coord each : coords)
        {
            str += each.toString() + ", ";
        }
        return str;
    }
}
