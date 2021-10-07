package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

/**
 *
 * @author simal
 */
public class ResultTest
{

    public ResultTest()
    {
    }

    @Test
    public void testResult_String_List1()
    {
        Coord a = new Coord(0, 1);
        Coord b = new Coord(1, 2);
        List<Coord> coords = new ArrayList<>();
        coords.add(a);
        coords.add(b);
        Result r = new Result("anEntry", coords);
        assertEquals("not initialised correctly", r.getResultName(), "anEntry");
    }

    @Test
    public void testResult_String_List2()
    {
        Coord a = new Coord(0, 1);
        Coord b = new Coord(1, 2);
        List<Coord> coords = new ArrayList<>();
        coords.add(a);
        coords.add(b);
        Result r = new Result("anEntry", coords);
        assertArrayEquals("not initialised correctly",
                r.getAllCoords().toArray(),
                coords.toArray());
    }

    @Test
    public void testResult_String_Coord()
    {
        Coord a = new Coord(0, 1);
        Result r = new Result("anEntry", a);
        assertEquals("not initialised correctly",
                r.get1stCoord(),
                a);
    }

    @Test
    public void testGetRestOfCoords()
    {
        Coord a = new Coord(0, 1);
        Coord b = new Coord(1, 2);
        Coord c = new Coord(2, 2);
        List<Coord> coords = new ArrayList<>();
        coords.add(a);
        coords.add(b);
        coords.add(c);
        Result r = new Result("anEntry", coords);
        // method in Result class returns in reverse order
        Coord[] expResult = {c, b};
        assertArrayEquals("retrieving wrong number of values",
                r.getRestOfCoords().toArray(),
                expResult);
    }
    
//    // tested in constructor
//    @Test
//    public void testGetResultName()
//    {
//    }

    @Test
    public void testGet1stCoord()
    {
        Coord a = new Coord(0, 1);
        Coord b = new Coord(1, 2);
        List<Coord> coords = new ArrayList<>();
        coords.add(a);
        coords.add(b);
        Result r = new Result("anEntry", coords);
        assertEquals("Doesn't get first coord", r.get1stCoord(), a);
    }

    @Test
    public void testToString()
    {
        System.out.println("testToString");
        Coord a = new Coord(0, 1);
        Coord b = new Coord(1, 2);
        List<Coord> coords = new ArrayList<>();
        coords.add(a);
        coords.add(b);
        Result r = new Result("anEntry", coords);
        String expResult = "resultName = anEntry -> (0,1), (1,2), ";
        System.out.println(r.toString());
        assertEquals("to string not correct", r.toString(), expResult);
    }

}
