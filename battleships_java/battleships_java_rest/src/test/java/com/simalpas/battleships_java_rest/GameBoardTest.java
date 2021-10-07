package com.simalpas.battleships_java_rest;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author simal
 */
public class GameBoardTest
{

    public GameBoardTest()
    {
    }

    @Test
    public void testGameBoard1()
    {
        // tests if board is correctly initalised with whiteapsce char
        System.out.println("GameBoard1");
        int size = 10;
        GameBoard result = new GameBoard(size);
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
        assertArrayEquals("Gameboard not correctly initialised", expResult, result.getBoard());
    }

    @Test
    public void testGameBoard2()
    {
        // tests if board with too small a size is defaulted to 10
        System.out.println("GameBoard2");
        int size = 0;
        GameBoard resultGameBoard = new GameBoard(size);
        int[] result;
        int xSize = resultGameBoard.getBoard()[0].length;
        int ySize = resultGameBoard.getBoard().length;
        assertEquals("xSize is wrong", 5, xSize);
        assertEquals("ySize is wrong", 5, ySize);
    }

    @Test
    public void testGetSquare1()
    {
        System.out.println("getSquare1");
        Coord c = new Coord(0,0);
        int size = 10;
        GameBoard instance = new GameBoard(size);
        char expResult = ' ';
        char result = instance.getSquare(c);
        assertEquals("Square at 0,0 not retrieved", expResult, result);
    }

    @Test
    public void testGetSquare2()
    {
        System.out.println("getSquare2");
        Coord c = new Coord(9,9);
        int size = 10;
        GameBoard instance = new GameBoard(size);
        char expResult = ' ';
        char result = instance.getSquare(c);
        assertEquals("Square at 9,9 not retrieved", expResult, result);
    }

    @Test
    public void testSetSquare1()
    {
        System.out.println("setSquare1");
        int size = 10;
        Coord c = new Coord(0,0);
        char symbol = 'a';
        GameBoard instance = new GameBoard(size);
        instance.setSquare(c, symbol);
        char result = instance.getSquare(c);
        char expResult = 'a';
        assertEquals(expResult, result);
    }

    @Test
    public void testSetSquare2()
    {
        // changes all squares to 'a'
        System.out.println("setSquare2");
        int size = 10;
        GameBoard instance = new GameBoard(size);
        Coord c;
        for (int y = 0; y < size; y++)
        {
            for (int x = 0; x < size; x++)
            {
                c = new Coord(x, y);
                instance.setSquare(c, 'a');
            }
        }
        char[][] result = instance.getBoard();
        char[][] expResult =
        {
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            },
            {
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
            }
        };
        assertArrayEquals("Changing all squares failed", expResult, result);
    }

    @Test
    public void testSetSquare3()
    {
        System.out.println("setSquare3");
        int size = 10;
        Coord c = new Coord(0,9);
        char symbol = 'a';
        GameBoard instance = new GameBoard(size);
        instance.setSquare(c, symbol);
        char result = instance.getSquare(c);
        char expResult = 'a';
        assertEquals(expResult, result);
    }

    @Test
    public void testprintBoard1()
    {
        System.out.println("printBoard1");
        int size = 10;
        GameBoard instance = new GameBoard(size);
        String expResult
                = "    _______________________________________\n"
                + " 9 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 8 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 7 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 6 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 5 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 4 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 3 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 2 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 1 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 0 |   |   |   |   |   |   |   |   |   |   |\n"
                + "     0   1   2   3   4   5   6   7   8   9";
        System.out.println(instance.toString());
        String result = instance.toString();
        assertEquals(expResult, result);
//        fail("lets see the board");
    }

    @Test
    public void testprintBoard2()
    {
        System.out.println("printBoard2");
        int size = 10;
        GameBoard instance = new GameBoard(size);
        // set (0,5),(4,0),(4,9),(5,0),(5,9),(9,5) to 'a'
        Coord[] coords =
        {
                new Coord(0, 5),
                new Coord(4, 1),
                new Coord(4, 9),
                new Coord(5, 1),
                new Coord(5, 9),
                new Coord(9, 5),
                new Coord(4, 4),
                new Coord(5, 5)
        };
        for (Coord eachCoord : coords)
        {
            instance.setSquare(eachCoord, 'a');
        }
        String result = instance.toString();
        String expResult
                = "    _______________________________________\n"
                + " 9 |   |   |   |   | a | a |   |   |   |   |\n"
                + " 8 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 7 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 6 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 5 | a |   |   |   |   | a |   |   |   | a |\n"
                + " 4 |   |   |   |   | a |   |   |   |   |   |\n"
                + " 3 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 2 |   |   |   |   |   |   |   |   |   |   |\n"
                + " 1 |   |   |   |   | a | a |   |   |   |   |\n"
                + " 0 |   |   |   |   |   |   |   |   |   |   |\n"
                + "     0   1   2   3   4   5   6   7   8   9";
        System.out.println("actual:\n" + result);
        System.out.println("expected:\n" + expResult);
        assertEquals("Results not in the right place", expResult, result);
    }


    @Test
    public void testprintBoard3()
    {
        System.out.println("printBoard3 - board size = 5");
        References.resetSIZE();
        int size = 5;
        GameBoard instance = new GameBoard(size);
        String expResult
                = "    ___________________\n"
                + " 4 |   |   |   |   |   |\n"
                + " 3 |   |   |   |   |   |\n"
                + " 2 |   |   |   |   |   |\n"
                + " 1 |   |   |   |   |   |\n"
                + " 0 |   |   |   |   |   |\n"
                + "     0   1   2   3   4";
        System.out.println("expected\n" + expResult);
        System.out.println("actual\n" + instance.toString());
        String result = instance.toString();
        assertEquals("Unable to print smaller board", expResult, result);
        References.resetSIZE();
    }
    
//    @After
//    public void teardown()
//    {
//        References.resetSIZE();
//    }

}
