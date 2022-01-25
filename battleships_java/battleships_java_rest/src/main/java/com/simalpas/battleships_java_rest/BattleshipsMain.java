package com.simalpas.battleships_java_rest;

import java.util.*;

/**
 * Single instance per game.
 *
 * @author simal
 */
public class BattleshipsMain
{

    // instance variables
    private Player p1;
    private Player p2;

    /**
     * Main class for the game.
     *
     * @param p1auto computer player or not (true/false)
     * @param p2auto computer player or not (true/false)
     * @param p1AiLevel 0=random, 1=tracking
     * @param p2AiLevel 0=random, 1=tracking
     * @param boardSize 5 - 99. best with 10
     */
    public BattleshipsMain(
            boolean p1auto,
            boolean p2auto,
            int p1AiLevel,
            int p2AiLevel,
            int boardSize)
    {
        // initalise the game
        this.p1 = new Player(p1auto, p1AiLevel, boardSize);
        this.p2 = new Player(p2auto, p2AiLevel, boardSize);
    }

    /**
     * Zero arg constructor for comp vs comp with auto setup.
     */
    public BattleshipsMain()
    {
        this.p1 = new Player(true, 1, 10);
        this.p2 = new Player(true, 1, 10);
    }

    /**
     * for computer players
     *
     * @param activePlayer
     * @param target
     * @return
     */
    public Map<String, List<Integer[]>> takeShot(
            String activePlayer,
            String target)
    {
        Player activeActual = this.getPlayer(activePlayer);
        Player targetActual = this.getPlayer(target);
        Result result = activeActual.takeShot(targetActual);
        // unpack the result to a map using class method
        return result.unpack();
    }

    /**
     *
     * @param activePlayer
     * @param target
     * @param x
     * @param y
     * @return if invalid coords, Map will have a single key "invalid"
     */
    public Map<String, List<Integer[]>> takeShot(
            String activePlayer,
            String target,
            int x,
            int y)
    {
        Player activeActual = this.getPlayer(activePlayer);
        Player targetActual = this.getPlayer(target);
        Coord shootAt = new Coord(x, y);
        Result result = activeActual.takeShot(targetActual, shootAt);
        return result.unpack();
    }

    /**
     * Place fleet according to passed list
     *
     * @param activePlayer
     * @param locations [x, y, direction] where direction 0=horiz 1=vert.
     * @return
     */
    public boolean setFleetLocation(
            String activePlayer,
            Map<String, Integer[]> locations)
    {
        return this.getPlayer(activePlayer).setFleetLocation(locations);
    }

    /**
     * Random placement of all ships
     *
     * @param activePlayer
     * @return
     */
    public boolean setFleetLocation(String activePlayer)
    {
        return this.getPlayer(activePlayer).setFleetLocation();
    }

    /**
     *
     * @param player
     * @param tracking
     * @return
     */
    public char[][] getPlayerBoard(String player, boolean tracking)
    {
        if (tracking)
        {
            return this.getPlayer(player).getBoardTracking();
        }
        return this.getPlayer(player).getBoardPrimary();
    }

    /**
     *
     * @param player
     * @return
     */
    public boolean getAutoPlayer(String player)
    {
        return this.getPlayer(player).isAutoPlayer();
    }

    /**
     *
     * @param player
     * @return
     */
    public int[] getLatestShot(String player)
    {
        Coord latest = this.getPlayer(player).getLatestShot();
        int[] result =
        {
            latest.getX(), latest.getY()
        };
        return result;
    }

    /**
     *
     * @param player
     * @return
     */
    public int getMovesMade(String player)
    {
        return this.getPlayer(player).getMovesMade();
    }

    /**
     *
     * @return
     */
    public String getWinner()
    {
        if (this.p2.getFleetSize("shipsRemaining") == 0)
        {
            return "p1";
        } else if (this.p1.getFleetSize("shipsRemaining") == 0)
        {
            return "p2";
        }
        return "";
    }

    /**
     *
     * @param player
     * @return
     */
    private Player getPlayer(String player)
    {
        if (player.equals("p1"))
        {
            return this.p1;
        } else if (player.equals("p2"))
        {
            return this.p2;
        }
        return new Player(true, 1, 10);
    }
}
