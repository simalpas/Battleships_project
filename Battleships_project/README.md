Python project to write a cli version of the classic game battleships. Uses classes. Works as an API, called from a seperate file, only imports needed are the references. Started as a project to cement my knowledge of the MVC patten, python classes, OOP and parts of the python standard libaries.

Features:
  human player input to place ships (checks for valid ship placements)
  auto populate boards for computer players
  human readable boards
  separate boards to record moves taken

To work on this, fork it and set up your own branch to work on a particular issue. 

for example:
`git checkout -b yourBranchName`

If you want to work on something, add your name to the TODO and then start working on it. Try and aim for a pull request within 24hrs. If you think what you are working on will take longer than that, consider reducing the problem size or refactoring into smaller code chunks.

Once you are happy with your changes, and have commited to your branch, push your changes to your github.From your github account you can initiate a pull request for your code to be reviewed.

This is the list of things that I think will end up with a reasonable working version of battleships. Please add to this list if you think of things that will be useful to the project.

- [x] Separate the various classes into separate files and import them correctly so as to not need to refactor the methods.
- [x] Refactor the Battleships system class to respond to the various messages that the front end will need to call.| `JJJ
- [x] Ensure that any calls to return objects does not return the actual object but a copy of it to preserve encapsulation.
- [x] Write a new front end to play the game - done with cliBattleships.py
- [x] Add colors to front end, using references from the relevent class, could write colour changing methods to References?
- [x] Move functions to print the board, out of ship placement and into front end.
- [x] End reliance on toString method in GameBoard as this is a display component, not model.
- [x] Have ship placement done on an individual basis so that front end can control display of the board.
- [x] Refactor winner method so that take shot returns simpler results. Winner should only return the winner not moves made as well.
- [x] Refactor ships placement in Player.py so that placements are done via arguments passed from the controller.
- [x] Allow human player to auto place ships
- [x] Add a method to get the last shot taken by a player
- [x] Highlight last incoming shot when displaying player board in cli
- [ ] Implement unit tests for public methods
- [ ] Build a web front end
- [ ] Build a server implementation that provides the results of the API calls, possibly containerised
- [ ] Host server on cloud instance (using Oracle cloud free tier)

In the future I plan to rebuild this in c++, keeping for the command line.