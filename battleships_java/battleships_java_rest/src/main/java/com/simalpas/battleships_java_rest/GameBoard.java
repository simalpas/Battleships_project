package com.simalpas.battleships_java_rest;

import java.util.Arrays;

/**
 *
 * @author simal
 */
public class GameBoard
{

    private char[][] board; // gameboard declared as a 2 dimensional array
    private final int SIZE; // size of the gameboard

    /**
     * Constructor for a 2 dimensional gameboard representation.
     * Board will be square. If too small to fit ships defaults to 10x10.
     *
     * @param size width and height of board(square)
     */
    protected GameBoard(int size)
    {
        if (size < 5)
        {
            this.SIZE = 5;
        } else
        {
            this.SIZE = size;
        }
        this.board = new char[this.SIZE][this.SIZE];
        setupNewBoard();
    }
    
    protected int getSIZE()
    {
        return this.SIZE;
    }

    /**
     *
     * @return deep copy of the game board
     */
    protected char[][] getBoard()
    {
        char[][] copyOfBoard = new char[this.SIZE][this.SIZE];
        for (int i = 0; i < this.board.length; i++)
        {
            copyOfBoard[i] = this.board[i].clone();
        }
        return copyOfBoard;
    }

    /**
     *
     * @param x x coord of square to retrieve.
     * @param y y coord of square to retrieve.
     * @return char of symbol held at given coords.
     */
    protected char getSquare(Coord coord)
    {
        return this.board[coord.getY()][coord.getX()];
    }

    /**
     *
     * @param x x coord of square to retrieve.
     * @param y y coord of square to retrieve.
     * @param symbol char to set contents of cell to.
     */
    protected void setSquare(Coord coord, char symbol)
    {
        this.board[coord.getY()][coord.getX()] = symbol;
    }

    /**
     * initialises board to set every square to single empty space
     */
    private void setupNewBoard()
    {
        for (char[] row : this.board)
        {
            Arrays.fill(row, ' ');
        }
    }
/**
 * For testing purposes, allows visualisation of the gameboard state.
 * 
 * @return string representation of the GameBoard state.
 */
    @Override
    public String toString()
    {
        int yLabel = this.SIZE - 1;
        StringBuilder sb = new StringBuilder();
        // format top line of board
        sb.append("    ");
        //dynamically resizes based on the size of the board
        for (int i = this.SIZE - 1; i > 0; i--)
        {
            sb.append("____");
        }
        sb.append("___\n");
        //iterates through y axis, counting down to place origin at bottom left.
        for (int y = this.board.length - 1; y >= 0; y--)
        {
            // add an extra space for single digit row numbers
            if (yLabel < 10)
            {
                sb.append(' ');
            }
            sb.append(yLabel);
            // print contents of the cells with spacing and a vertical seperator.
            for (int x = 0; x < this.board[y].length; x++)
            {
                sb.append(" | ");
                sb.append(this.board[y][x]);
            }
            sb.append(" |\n");
            --yLabel;
        }
        // legend for x axis
        sb.append("     ");
        for (int i = 0; i < this.SIZE - 1; i++)
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
        sb.append(this.SIZE - 1);
        return sb.toString();
    }

}
