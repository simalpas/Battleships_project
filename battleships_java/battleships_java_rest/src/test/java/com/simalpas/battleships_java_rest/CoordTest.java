package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author simal
 */
public class CoordTest
{
    
    public CoordTest()
    {
    }

    @Test
    public void testGetCoord()
    {
        Coord c = new Coord(0,0);
        int[] result = c.getCoord();
        int[] expResult = {0,0};
        assertArrayEquals("coord not stored correctly", result, expResult);
    }
    
    @Test
    public void testGetCoord2()
    {
        Coord c = new Coord(1,9);
        int[] result = c.getCoord();
        int[] expResult = {1,9};
        assertArrayEquals("Coords in wrong order", result, expResult);
    }
    
    @Test
    public void testGetX()
    {
        Coord c = new Coord(3,4);
        int result = c.getX();
        int expResult = 3;
        assertEquals("Gets wrong coord", result, expResult);
    }
    
    @Test
    public void testGetY()
    {
        Coord c = new Coord(7,8);
        int result = c.getY();
        int expResult = 8;
        assertEquals("Gets wrong coord", result, expResult);
    }

    @Test
    public void testEquals()
    {
        Coord a = new Coord(1,2);
        Coord b = new Coord(1,2);
        boolean result = a.equals(b);
        assertTrue("Comparison not working", result);
    }

    @Test
    public void testEquals2()
    {
        Coord a = new Coord(1,2);
        boolean result = a.equals(a);
        assertTrue("Comparison of same object failure", result);
    }
    
    @Test
    public void testEquals3()
    {
        Coord a = new Coord(1,2);
        Coord b = new Coord(2,1);
        boolean result = a.equals(b);
        assertFalse("Unequal comparison failure", result);
    }
    @Test
    public void testHashCode()
    {
        Coord a = new Coord(0,1);
        Coord b = new Coord(1,0);
        int hashA = a.hashCode();
        int hashB = b.hashCode();
        assertFalse("Reversed coords return the same hashcode", hashA == hashB);
    }
    
}
