package com.simalpas.battleships_java_rest;

import java.util.*;
import java.lang.Math;

/**
 * Object that represents a Player of the game Battleships.
 *
 * @author Simon Malpas
 */
public class Player
{

    private final GameBoard boardPrimary;
    private final GameBoard boardTracking;
    // the size of each ship remaining along with remaining ships
    private final Map<String, Integer> fleetSize;
    // the coordinates of the placed ships
    private final Map<String, List<Coord>> fleetLocation;
    // shotsTaken could not be used, instead the gameboard could be checked
    // to see if there has been a shot taken at that location. However whilst
    // this is slightly less memory efficient, it is simpler and a little faster
    private List<Coord> shotsTaken;
    private Coord latestShot;
    private int movesMade;
    private final boolean autoPlayer;
    private Ai aiBrain;

    /**
     * Constructor for a player
     *
     * @param auto is this player computer controlled
     * @param aiLevel 0=random, 1=random with shiptracking
     */
    protected Player(boolean auto, int aiLevel, int size)
    {
        // get out the boards
        boardPrimary = new GameBoard(size);
        boardTracking = new GameBoard(size);

        fleetSize = new HashMap<String, Integer>();

        this.fleetSize.put("A", 5);
        this.fleetSize.put("B", 4);
        this.fleetSize.put("C", 3);
        this.fleetSize.put("S", 3);
        this.fleetSize.put("D", 2);
        this.fleetSize.put("shipsRemaining", 5);

        fleetLocation = new HashMap<>();
        this.fleetLocation.put("Aircraft Carrier", new ArrayList<>());
        this.fleetLocation.put("Battleship", new ArrayList<>());
        this.fleetLocation.put("Cruiser", new ArrayList<>());
        this.fleetLocation.put("Submarine", new ArrayList<>());
        this.fleetLocation.put("Destroyer", new ArrayList<>());

        this.autoPlayer = auto;
        if (auto)
        {
            this.aiBrain = new Ai(aiLevel, this.boardPrimary);
//          Automatically setup any computer player boards
            this.setFleetLocation();
        }
    }

    /**
     * to allow testing
     *
     * @return
     */
    protected int getFleetSize(String shipSymbol)
    {
        return fleetSize.get(shipSymbol);
    }

    /**
     * to allow testing
     *
     * @return
     */
    protected Map<String, List<Coord>> getFleetLocation()
    {
        return fleetLocation;
    }

    protected char[][] getBoardPrimary()
    {
        return boardPrimary.getBoard();
    }

    protected char[][] getBoardTracking()
    {
        return boardTracking.getBoard();
    }

    protected int getMovesMade()
    {
        return movesMade;
    }

    protected boolean isAutoPlayer()
    {
        return autoPlayer;
    }

    protected Coord getLatestShot()
    {
        return this.latestShot;
    }

    /**
     *
     * @param x
     * @param y
     * @return single item map, key = result of shot/shipName if sunk value =
     * list of coordinates in the form of int arrays. single coord return is
     * shot just taken, multiple list entries if ship is sunk. Updates primary
     * board
     */
    protected Result incoming(Coord coord)
    {
        //conver char held on gameboard to String to match types in utility maps.
        String squareContents = String.valueOf(this.boardPrimary.getSquare(coord));

        // build map for return, input coords not used if ship is sunk
        // all this return faff is so that the AI player knows when it has
        // sunk a ship.
        Result result;

        // Shot misses
        if (squareContents.charAt(0) == ' ')
        {
            this.boardPrimary.setSquare(coord, References.getSymbol("Miss"));

            result = new Result("Miss", coord);
            return result;
        } // Shot sinks a ship
        else if (fleetSize.get(squareContents) == 1)
        {
            //reduce the size of the ship to 0
            fleetSize.put(squareContents, fleetSize.get(squareContents) - 1);
            // reduce the number of ships remaining by 1
            fleetSize.put("shipsRemaining", fleetSize.get("shipsRemaining") - 1);
            //find the name of the ship
            String shipName = References.getShipName(squareContents.charAt(0));

            // return the name of the ship and the locations of each part of
            // of the ship, first entry in list of coords in Result object is
            // incoming shot
            List<Coord> coords = new ArrayList<>();
            coords.add(coord);
            for (Coord eachLocation : fleetLocation.get(squareContents))
            {
                coords.add(eachLocation);
            }
            result = new Result(shipName, coords);
            // change the symbols on the board to sunk
            this.sinkShip(result, this.boardPrimary);

            return result;
        } else

        {
            result = new Result("Hit", coord);
        }
        return result;
    }

    private void sinkShip(Result inputResult, GameBoard gb)
    {
        //loop through fleetLocation to sink ship
        for (Coord eachCoord : inputResult.getAllCoords())
        {
            gb.setSquare(eachCoord, References.getSymbol("Sunk"));
        }
    }

    /**
     * Overloaded method No input coords required if ai player.
     * records the aiBrain's shot attempt
     *
     * @param target Player object to shoot at
     * @return
     */
    protected Result takeShot(Player target)
    {
        Result result;
        if (autoPlayer)
        {
            // aiBrain will not return a duplicate coord, no need to check
            Coord coords = aiBrain.takeShot();
            this.latestShot = coords;
            result = target.incoming(coords);
            this.recordShotTaken(result);
            return result;
        }
        result = new Result();
        return result;
    }

    /**
     * Overloaded method Covers the case where coordinates are provided, either
     * human player or external ai brain. checks it is a valid shot. finds out
     * the result of the shot. records coords of shot taken. updates tracking
     * board (sinking if necessary). increases moves made.
     *
     *
     * @param result
     * @param x x coordinate for shot
     * @param y y coordinate for shot
     * @return single entry map with shipName/outcome, list of int arrays with
     * either locations of sunken ship or shot just taken
     */
    protected Result takeShot(Player target, Coord coords)
    {
        Result result;
        // contains method uses overridden equals method to compare coords
        if (this.shotsTaken.contains(coords))
        {
            result = new Result("invalid", coords);
            return result;
        }
        //find results of shot
        // 1st coord in result is latest shot
        result = target.incoming(coords);
        String resultName = result.getResultName();
        // update tracking board and metrics
        this.recordShotTaken(result);
        return result;
    }

    /**
     * Utility method. lets the aiBrain know whats going on so it can track
     * unsunk ships Updates tracking board, updates latest shot,
     *
     * @param inputResult information on what happened.
     */
    private void recordShotTaken(Result inputResult)
    {
        if (this.autoPlayer)
        {
            this.aiBrain.recordShot(inputResult);
        }
        String resultName = inputResult.getResultName();
        Coord shot = inputResult.get1stCoord();
        // check if a ship was sunk
        if (References.SHIPS.containsKey(resultName))
        {
            //if it was update the tracking board
            this.sinkShip(inputResult, this.boardTracking);
        } // if not: hit or miss
        else
        {
            this.boardTracking.setSquare(shot, References.getSymbol(resultName));
        }
        this.latestShot = shot;
        this.shotsTaken.add(shot);
    }

    /**
     * Sets the board according to ship location, and records the coords.
     *
     * @param coords origin of the ship
     * @param direction 0=horizontal 1=vertical
     * @param shipName which ship to place
     */
    private void writeShip(Coord coords, int direction, String shipName)
    {
        // unpack coords
        int x = coords.getX();
        int y = coords.getY();
        // iterate for the length of the ship
        for (int i = References.SHIPS.get(shipName); i > 0; i--)
        {
            // set the square
            Coord eachCoord = new Coord(x, y);
            this.boardPrimary.setSquare(eachCoord, References.getSymbol(shipName));
            // record the coords in fleetLocation
            this.fleetLocation.get(shipName).add(eachCoord);
            // increment the appropriate coordinate according to direction
            if (direction == 0)
            {
                x++;
            } else if (direction == 1)
            {
                y++;
            }
        }
        // exit loop and increment ships remaining
        this.fleetSize.put("shipsRemaining", this.fleetSize.get("shipsRemaining") + 1);
    }

    /**
     * Ensures coordinates are in range, and there is no overlap.
     *
     * @param coords origin point of the ship
     * @param direction 0/1 the direction the ship will be placed horz/vert
     * @param shipName the name of the ship being checked
     * @return if placement is valid
     */
    private boolean checkPlacement(Coord coords, int direction, String shipName)
    {
        int x = coords.getX();
        int y = coords.getY();
        if ((x + References.SHIPS.get(shipName) > 10)
                || (y + References.SHIPS.get(shipName) > 10))
        {
            return false;
        }
        Coord tempCoord;
        for (int i = References.SHIPS.get(shipName); i > 0; i--)
        {
            tempCoord = new Coord(x, y);
            if (this.boardPrimary.getSquare(tempCoord) != ' ')
            {
                return false;
            }
            if (direction == 0)
            {
                x++;
            }
            if (direction == 1)
            {
                y++;
            }
        }
        return true;
    }

    /**
     * Check proposed placement, and writes the location if valid
     *
     * @param coords origin of the ship
     * @param direction 0=horizontal 1=vertical
     * @param shipName name of the ship being placed
     * @return successful or not
     */
    private boolean placeShip(Coord coords, int direction, String shipName)
    {
        if (this.checkPlacement(coords, direction, shipName))
        {
            this.writeShip(coords, direction, shipName);
            return true;
        }
        return false;
    }

    /**
     * Zero arg call places ships at random in valid positions
     *
     * @return successful or not
     */
    protected boolean setFleetLocation()
    {
        return this.randomPlacement();
    }

    /**
     * Sets the fleet if valid
     *
     * @param proposedFleet Map made up of ShipName, list of Integers in the
     * following order - OriginXCoord, OriginYCoord, direction (0/1). Where
     * 0=horiz, 1=vert.
     */
    protected boolean setFleetLocation(Map<String, Integer[]> proposedFleet)
    {
        // iterate through Map proposedFleet
        for (Map.Entry<String, Integer[]> eachEntry : proposedFleet.entrySet())
        {
            // check ship hasn't been placed already
            if (this.fleetLocation.get(eachEntry.getKey()).size() > 0)
            {
                return false;
            }
            // unpack values to pass to placeShip
            int tempX = eachEntry.getValue()[0];
            int tempY = eachEntry.getValue()[1];
            int tempDirection = eachEntry.getValue()[2];
            String tempShipName = eachEntry.getKey();
            Coord tempCoord = new Coord(tempX, tempY);
            // try and place the ship, returning false if not possible
            return this.placeShip(tempCoord, tempDirection, tempShipName);
        }
        return false;
    }

    /**
     * Places ships at random for a fast setup
     *
     * @return successful or not
     */
    private boolean randomPlacement()
    {
        // iterate through all ships in References.SHIPS
        for (Map.Entry<String, Integer> eachShip : References.SHIPS.entrySet())
        {
            // check the ship hasn't already been placed
            if (this.fleetLocation.get(eachShip.getKey()).size() > 0)
            {
                // do nothing
            } else
            {
                boolean placed = false;
                // loop whilst the ship isn't placed
                while (!placed)
                {
                    // pick random coordinates and direction
                    // casting to int rounds down
                    int x = (int) (Math.random() * this.boardPrimary.getSIZE());
                    int y = (int) (Math.random() * this.boardPrimary.getSIZE());
                    int direction = (int) (Math.random() * 2);
                    Coord tempCoord = new Coord(x,y);
                    // check if it is a valid origin, and place it if so.
                    // update loop var to exit if successful
                    placed = this.placeShip(tempCoord, direction, eachShip.getKey());
//                    {
//                        // increase the number of shipsRemaining
//                        this.fleetSize.put("shipsRemaining", this.fleetSize.get("shipsRemaining")+1);
//                        // update placed to exit loop
//                        placed =true;
//                    }
                }
            }
        }
        // return whether the shipsRemaining == 5
        return (this.fleetSize.get("shipsRemaining") == 5);
    }
}
