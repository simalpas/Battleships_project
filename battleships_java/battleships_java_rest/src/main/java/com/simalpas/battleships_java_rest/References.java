package com.simalpas.battleships_java_rest;

import java.util.*;

/**
 *
 * @author simal
 */
public class References
{

    // Ship names and their lengths
    public static final Map<String, Integer> SHIPS = new HashMap<>();

    static
    {
        SHIPS.put(
                "Aircraft Carrier", 5);
        SHIPS.put(
                "Battleship", 4);
        SHIPS.put(
                "Cruiser", 3);
        SHIPS.put(
                "Submarine", 3);
        SHIPS.put(
                "Destroyer", 2);
    }

    // Translate ship name to symbol
    private static final Map<String, Character> SYMBOLS = new HashMap<>();

    static
    {
        SYMBOLS.put("Aircraft Carrier", 'A');
        SYMBOLS.put("Battleship", 'B');
        SYMBOLS.put("Cruiser", 'C');
        SYMBOLS.put("Submarine", 'S');
        SYMBOLS.put("Destroyer", 'D');
        SYMBOLS.put("Hit", 'X');
        SYMBOLS.put("Miss", 'o');
        SYMBOLS.put("Empty", ' ');
        SYMBOLS.put("Sunk", '#');
    }

    // reverse lookup of map
    public static String getShipName(char symbol)
    {
        for (Map.Entry<String, Character> eachSymbol : References.SYMBOLS.entrySet())
        {
            if (eachSymbol.getValue() == symbol)
            {
                return eachSymbol.getKey();
            }
        }
        return null;
    }
    
    public static char getSymbol(String shipName)
    {
        return SYMBOLS.get(shipName);
    }
    
    private static int SIZE;

    public static void setSIZE(int size)
    {
        if (SIZE != 0)
        {
        } else
        {
            SIZE = size;
        }
    }
    
    /**
     * testing purposes only
     */
    public static void resetSIZE()
    {
        SIZE = 0;
    }

    public static int getSIZE()
    {
        return SIZE;
    }

    public static String[] validInputs =
    {
        "y", "yes", "Y", "Yes", "YES", "ok", "OK", "Ok", "o"
    };

    public static final Map<String, String> ANSICOLOURS = new HashMap<>();

    static
    {
        ANSICOLOURS.put("black", "\033[30m");
        ANSICOLOURS.put("boldBlack", "\033[30;1m");
        ANSICOLOURS.put("red", "\033[31m");
        ANSICOLOURS.put("boldRed", "\033[31;1m");
        ANSICOLOURS.put("green", "\033[32m");
        ANSICOLOURS.put("boldGreen", "\033[32;1m");
        ANSICOLOURS.put("yellow", "\033[33m");
        ANSICOLOURS.put("boldYellow", "\033[33;1m");
        ANSICOLOURS.put("blue", "\033[34m");
        ANSICOLOURS.put("boldBlue", "\033[34;1m");
        ANSICOLOURS.put("magenta", "\033[35m");
        ANSICOLOURS.put("boldMagenta", "\033[35;1m");
        ANSICOLOURS.put("cyan", "\033[36m");
        ANSICOLOURS.put("boldCyan", "\033[36;1m");
        ANSICOLOURS.put("white", "\033[37m");
        ANSICOLOURS.put("boldWhite", "\033[37;1m");
        ANSICOLOURS.put("reset", "\033[0m");
    }

    public static String resetColour = ANSICOLOURS.get("reset");
    public static String boardColour = ANSICOLOURS.get("blue");
    public static String yLabelColour = ANSICOLOURS.get("boldWhite");
    public static String xLabelColour = ANSICOLOURS.get("boldWhite");
    public static String shipColour = ANSICOLOURS.get("yellow");
    public static String missColour = ANSICOLOURS.get("cyan");
    public static String hitColour = ANSICOLOURS.get("boldRed");
    public static String sunkColour = ANSICOLOURS.get("red");
    public static String highlightColour = ANSICOLOURS.get("boldMagenta");

}
