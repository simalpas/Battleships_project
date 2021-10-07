package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author simal
 */
public class ReferencesTest
{

    public ReferencesTest()
    {
    }

    @Test
    public void testSHPS1()
    {
        int result = References.SHIPS.get("Aircraft Carrier");
        int expResult = 5;
        assertEquals("Map not properly populated", result, expResult);
    }

    @Test
    public void testSHIPS2()
    {
        int result = References.SHIPS.get("Destroyer");
        int expResult = 2;
        assertEquals("Map not populated to the end", result, expResult);
    }

    @Test
    public void testGetShipName1()
    {
        String result = References.getShipName('A');
        String expResult = "Aircraft Carrier";
        assertEquals("Map not properly populated", result, expResult);
    }

    @Test
    public void testGetShipName2()
    {
        String result = References.getShipName('#');
        String expResult = "Sunk";
        assertEquals("Map not properly populated", result, expResult);
    }

    @Test
    public void testGetSymbol1()
    {
        char result = References.getSymbol("Miss");
        char expResult = 'o';
        assertEquals("Map not properly populated", result, expResult);
    }
    
    @Test
    public void testGetSymbol2()
    {
        char result = References.getSymbol("Destroyer");
        char expResult = 'D';
        assertEquals("Map not properly populated", result, expResult);
    }

    @Test
    public void testSetSIZE1()
    {
        References.setSIZE(10);
        assertEquals("Does not set SIZE variable correctly", References.getSIZE(), 10);
    }

    @Test
    public void testSetSIZE2()
    {
        References.setSIZE(10);
        References.setSIZE(25);
        assertEquals("Does not set SIZE variable correctly", References.getSIZE(), 10);
    }

    @Test
    public void testANSICOLOURS1()
    {
        String result = References.resetColour;
        String expResult = "\033[0m";
        assertEquals("Map ref not working", result, expResult);
    }

    @Test
    public void testANSICOLOURS()
    {
        String result = References.highlightColour;
        String expResult = "\33[35;1m";
        assertEquals("Map ref not working", result, expResult);
    }
}
