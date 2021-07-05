WORK ON Battleships_python for the project. The Java version is a work in progress and pull requests will not be approved.

Python project to write a cli vesion of the classic game battleships. Uses classes. Plan is to also publish as an API, and freeze for linux and windows.
Features:
human player input to place ships (checks for valid ship placements)
auto populate boards for computer players
human readable boards
separate boards to record moves taken

This is the list of things that I think will end up with a reasonable working version of battleships. Please add to this list if you think of things that will be useful to the project. At the moment, I think it best to avoid new features until we have a working version with a front end that allows a user to play a single player game against a computer.

#TODO Separate the various classes into separate files and import them correctly so as to not need so refactor the methods.
#TODO Refactor the Battleships system class to respond to the various messages that the front end will need to call.
#TODO Ensure that any calls to return the player boards does not return the actual object but a copy of it to preserve encapsulation.
#TODO Write a new front end to play the game, possibly using django or some other python based framework?
#TODO Host poject on cloud server (to be done on simalpas.com/battleships)
#TODO Write unit tests for public methods

