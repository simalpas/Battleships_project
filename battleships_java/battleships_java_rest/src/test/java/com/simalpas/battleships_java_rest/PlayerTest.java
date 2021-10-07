package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

/**
 *
 * @author simal
 */
public class PlayerTest
{

    public PlayerTest()
    {
    }

//    @Before
//    public void setup()
//    {
//        Player tp = new Player(false, 1);
//    }
//    
//    
//    public void teardown()
//    {
//        tp = null;
//    }
    @Test
    public void testConstructor1()
    {
        Player tp = new Player(false, 1, 10);
        char[][] result = tp.getBoardPrimary();
        char[][] expResult =
        {
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
        };
        assertArrayEquals("Gameboard not correctly initialised", expResult, result);
    }

    @Test
    public void testConstructor2()
    {
        Player tp = new Player(false, 1, 10);
        char[][] result = tp.getBoardTracking();
        char[][] expResult =
        {
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
        };
        assertArrayEquals("Gameboard not correctly initialised", expResult, result);
    }

    @Test
    public void testConstructor3()
    {
        Player tp = new Player(false, 1, 10);
        int result = tp.getFleetSize("A");
        int expResult = 5;
        assertEquals("Gameboard not correctly initialised", expResult, result);
    }

    @Test
    public void testConstructor4()
    {
        Player tp = new Player(false, 1, 10);
        int result = tp.getFleetSize("shipsRemaining");
        int expResult = 5;
        assertEquals("Gameboard not correctly initialised", expResult, result);
    }

    @Test
    public void testConstructor5()
    {
        Player tp = new Player(false, 1, 10);
        int result = tp.getFleetSize("A");
        int expResult = 5;
        assertEquals("Gameboard not correctly initialised", expResult, result);
    }
    
    @Test
    public void testSinkShip()
    {
        Player tp = new Player(false, 1, 10);
        //setup - use setup method to set a ship at (0,0),(1,0)

        // take shots to sink the ship
        
        char[][] result = tp.getBoardPrimary();
        char[][] expResult =
        {
            {
                '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
            {
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            },
        };
//        assertArrayEquals("Didn't sink the ship", expResult, result);
    }
    
    @Test
    public void testShotsTaken()
    {
        // something to test
        Coord a = new Coord(0,0);
        Coord b = new Coord(0,0);
        List<Coord> coordsA = new ArrayList<>();
        coordsA.add(a);
        assertTrue("different objects", coordsA.contains(b));
    }
    
    private String boardToString(char[][] board)
    {
        int yLabel = board.length - 1;
        StringBuilder sb = new StringBuilder();
        // format top line of board
        sb.append("    ");
        //dynamically resizes based on the size of the board
        for (int i = board.length - 1; i > 0; i--)
        {
            sb.append("____");
        }
        sb.append("___\n");
        //iterates through y axis, counting down to place origin at bottom left.
        for (int y = board.length - 1; y >= 0; y--)
        {
            // add an extra space for single digit row numbers
            if (yLabel < 10)
            {
                sb.append(' ');
            }
            sb.append(yLabel);
            // print contents of the cells with spacing and a vertical seperator.
            for (int x = 0; x < board[y].length; x++)
            {
                sb.append(" | ");
                sb.append(board[y][x]);
            }
            sb.append(" |\n");
            --yLabel;
        }
        // legend for x axis
        sb.append("     ");
        for (int i = 0; i < board.length - 1; i++)
        {
            sb.append(i);
            // extra space for single digit columns.
            if (i < 10)
            {
                sb.append(' ');
            }
            sb.append("  ");
        }
        // no extra white space at the end of the string
        sb.append(board.length - 1);
        return sb.toString();
    }
    
    @Test
    public void testRandomPlacement()
    {
        // visually check if a board has been set and is different every time
        Player p = new Player(true, 1, 10);
        p.setFleetLocation();
        System.out.println(this.boardToString(p.getBoardPrimary()));
    }
    
}