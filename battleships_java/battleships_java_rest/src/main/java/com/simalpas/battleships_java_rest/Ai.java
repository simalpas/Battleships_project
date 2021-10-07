package com.simalpas.battleships_java_rest;

import java.util.*;

/**
 *
 * @author simal
 */
public class Ai
{

    // instance variables
    private int aiLevel;
    // All shots that can still be taken
    private List<Coord> possibleShots = new ArrayList<>();
    // allows the brain to track which ships have been sunk
    // may be useless
    private Map<String, Integer> shipTracking = new HashMap<>();
    // allows the brain to remember which squares have been hit but not sunk
    private List<Coord> unsunk = new ArrayList<>();
    // Save a reference to the board to get information
    private GameBoard myGB;

    /**
     * Constructor, must have a reference to the gameboard so as to
     * check the size for possible shots.
     * @param aiLevel
     * @param gb 
     */
    protected Ai(int aiLevel, GameBoard gb)
    {
        this.aiLevel = aiLevel;
        this.myGB = gb;
        this.initPossibleShots();
//        populate shipTracking
        this.shipTracking.put("Aircraft Carrier", 0);
        this.shipTracking.put("Battleship", 0);
        this.shipTracking.put("Cruiser", 0);
        this.shipTracking.put("Submarine", 0);
        this.shipTracking.put("Destroyer", 0);

    }

    private void initPossibleShots()
    {
        // loop through size of board writing a pair of coords as an integer
        // array to the List for every combination possible.
        for (int x = this.myGB.getSIZE() - 1; x >= 0; x--)
        {
            for (int y = this.myGB.getSIZE() - 1; y >= 0; y--)
            {
                this.possibleShots.add(new Coord(x, y));
            }
        }
    }

    /**
     * Generate coordinates for a valid shot. Calls different methods dependent
     * on aiLevel
     *
     * @return array of 2 integers - x, y for shot attempt.
     */
    protected Coord takeShot()
    {
        Coord chosenShot;
        switch (this.aiLevel)
        {
            case 0:
                chosenShot = this.randomShot();
                break;
            case 1:
                chosenShot = this.randomWithTracking();
                break;
            default:
                chosenShot = this.randomWithTracking();
                break;
        }
        // remove guess from possible shots
        this.possibleShots.remove(chosenShot);

        return chosenShot;
    }

    /**
     *
     * @param inputResult
     */
    protected void recordShot(Result inputResult)
    {
        // get sent single entry map with shipName/result as key, Coord(s)
        // as Value
        Coord shot = inputResult.get1stCoord();
        String resultName = inputResult.getResultName();
        // is the resultKey a Hit? if so shipTracking
        if (resultName.equals("Hit"))
        {
            this.unsunk.add(shot);
        }
        // if it is a sunken ship, remove all the locations from the unsunk list
        if (References.SHIPS.containsKey(resultName))
        {
            for (Coord eachHit : inputResult.getRestOfCoords())
            {
                // won't error if the coord is not present.
                // important as the last location hit will not be in unsunk
                this.unsunk.remove(eachHit);
            }
            this.shipTracking.put(resultName, 1);
        }
    }

    /**
     * @return a random shot from the possible shots remaining
     */
    private Coord randomShot()
    {
        return this.getRandomCoord(possibleShots);
    }

    /**
     * Generates a list of good guesses, then picks one
     *
     * @return returns a random possible shot, unless an a ship has been hit and
     * not sunk, in which case makes best guesses at next shot for a hit.
     */
    private Coord randomWithTracking()
    {
        if (this.unsunk.size() > 0)
        {
            return this.shipTrackingAlgorithm();
        }
        return this.randomShot();
    }

    /**
     * @return best guess for next hit based on previous registered hits that
     * have not yet sunk a ship.
     */
    private Coord shipTrackingAlgorithm()
    {
        // initialised to stop warnings
        List<Coord> bestGuesses = new ArrayList<>();
        Coord chosenShot;
        int direction;
        // no need to check if any unsunk, as in contract
        if (this.unsunk.size() == 1)
        {
            // generate potential shots and sanitise
            bestGuesses = this.generatePotentialShots(this.unsunk.get(0), 2);

        } else if (this.unsunk.size() > 1)
        {
            // compare x coords of 1st 2 in list, if the same direction is 
            // horizontal
            if (this.unsunk.get(0).getX() == this.unsunk.get(1).getX())
            {
                direction = 0;
            } else
            {
                direction = 1;
            }
            for (Coord eachCoord : this.unsunk)
            {
                bestGuesses.addAll(
                        this.generatePotentialShots(eachCoord, direction));
            }
            // if no shots possible, switch direction and generate again.
            if (bestGuesses.size() == 0)
            {
                // if direction = 0 make it 1 & vise versa.
                direction = direction == 0 ? 1 : 0;
                for (Coord eachCoord : this.unsunk)
                {
                    bestGuesses.addAll(
                            this.generatePotentialShots(eachCoord, direction));
                }
            }
        }
        return this.getRandomCoord(bestGuesses);
    }

    /**
     * @param knownHit Coord of a known hit
     * @param direction 0=horiz 1=vert 2=orthagonal
     * @return List of possible next ship locations based on hits. only valid
     * possible shots returned
     */
    private List<Coord> generatePotentialShots(Coord knownHit, int direction)
    {
        int[] coordChange =
        {
            -1, 1
        };
        Coord generatedCoord;
        List<Coord> bestGuesses = new ArrayList<>();
        if ((direction == 0) || (direction == 2))
        {
            for (int i : coordChange)
            {
                bestGuesses.add(new Coord(knownHit.getX() + i, knownHit.getY()));
            }
        }
        if (direction > 0)
        {
            for (int i : coordChange)
            {
                bestGuesses.add(new Coord(knownHit.getY() + i, knownHit.getY()));
            }
        }
        this.sanitiseShots(bestGuesses);
        return bestGuesses;
    }

    /**
     * @return list of coordinates with taken shots removed. Duplicates
     * retained as no impact on validity (could be more likely)
     */
    private List<Coord> sanitiseShots(List<Coord> potentialShots)
    {
        List<Coord> bestGuesses = new ArrayList<>();
//        // cast to a set to remove dupes
//        Set<Coord> coordsSet = new HashSet<>();
//        coordsSet.addAll(potentialShots);
        // only add to the bestGuesses if a possible shot
        for (Coord eachCoord : potentialShots)
        {
            if (this.possibleShots.contains(eachCoord))
            {
                bestGuesses.add(eachCoord);
            }
        }
        return bestGuesses;
    }

    /**
     * @param list to select from
     * @return single random item from that list
     */
    private Coord getRandomCoord(List<Coord> c)
    {
        Random rand = new Random();
        return c.get(rand.nextInt(c.size()));
    }

    /**
     * Testing methods CAN BE DELETED FOR PROD
     */
    protected List<Coord> getPossibleShots()
    {
        return this.possibleShots;
    }
}
