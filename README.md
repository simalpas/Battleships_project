Python project to write a cli version of the classic game battleships. Uses classes. Works as an API, called from a seperate file, only imports needed are the references. Started as a project to cement my knowledge of the MVC patten, python classes, OOP and parts of the python standard libaries.

Features:
  human player input to place ships (checks for valid ship placements)
  auto populate boards for computer players
  human readable boards
  separate boards to record moves taken
  cheat mode to see the computer player's board

  To use the CLI front end, and play the game, install the module, then simply run
   `Battleships_api.CLIBattleships`
   eg.
   `py -m Battleships.CLIBattleships`

This is the list of things that I think will end up with a reasonable working version of battleships. Please add to this list if you think of things that will be useful to the project.

- Documentation for the API!!
- Unittests
- Separate the various classes into separate files and import them correctly so as to not need to refactor the methods.
- Refactor the Battleships system class to respond to the various messages that the front end will need to call.| `JJJ
- Ensure that any calls to return objects does not return the actual object but a copy of it to preserve encapsulation.
- Write a new front end to play the game - done with cliBattleships.py
- Add colors to front end, using references from the relevent class, could write colour changing methods to References?
- Move functions to print the board, out of ship placement and into front end.
- End reliance on toString method in GameBoard as this is a display component, not model.
- Have ship placement done on an individual basis so that front end can control display of the board.
- Refactor winner method so that take shot returns simpler results. Winner should only return the winner not moves made as well.
- Refactor ships placement in Player.py so that placements are done via arguments passed from the controller.
- Allow human player to auto place ships
- Add a method to get the last shot taken by a player
- Highlight last incoming shot when displaying player board in cli
- Implement unit tests for public methods
- Build a web front end
- Use a framework such as Flask to make calls to the api according to GET and POST requests.

In the future I plan to rebuild this in c++ for the command line, and possibly Java to run as a back end to a web app.