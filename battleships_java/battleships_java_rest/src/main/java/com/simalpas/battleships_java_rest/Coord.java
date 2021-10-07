package com.simalpas.battleships_java_rest;

/**
 *
 * @author simal
 */
public class Coord
{
    private int x;
    private int y;
    
    protected Coord(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    
    protected int[] getCoord()
    {
        int[] result = {x, y};
        return result;
    }
    
    protected int getX()
    {
        return this.x;
    }
    
    protected int getY()
    {
        return this.y;
    }
    
    public Integer[] toArray()
    {
        Integer[] r = {this.getX(), this.getY()};
        return r;
    }
    
    @Override
    public boolean equals(Object o)
    {
        // check if it is the same object
        if (o == this)
        {
            return true;
        }
        // check if it is even a Coord object
        if (!(o instanceof Coord))
        {
            return false;
        }
        //cast to Coord
        Coord c = (Coord)o;
        // compare the coordinates
        return (c.getCoord()[0] == this.x)
                && (c.getCoord()[1] == this.y);
    }

    @Override
    public int hashCode()
    {
        int hash = 3;
        hash = 97 * hash + this.x;
        hash = 97 * hash + this.y;
        return hash;
    }
    
    @Override
    public String toString()
    {
        String str = "(" + this.x + ", " + this.y + ")";
        return str;
    }
}
