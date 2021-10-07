package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

/**
 *
 * @author simal
 */
public class AiTest
{
    
    public AiTest()
    {
    }

    @Test
    public void testConstructor1()
    {
        System.out.println("testConstructor1");
        GameBoard gb = new GameBoard(5);
        Ai a = new Ai(1, gb);
//        System.out.println(a.getPossibleShots());
        String result = a.getPossibleShots().toString();
        String expResult = "[(4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]";
        assertEquals("Not initialising possible shots", expResult, result);
    }
    @Test
    public void testTakeShot()
    {
    }
    
}
