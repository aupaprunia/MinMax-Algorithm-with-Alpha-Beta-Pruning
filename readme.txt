Name - Aditya Umesh Paprunia
UTA ID - 1002154940
Programming language - Python (3.9.6)

Code Structure:

    * Class Node-
    Used to represent a node in a minmax algorithm

    * def generate_tree()-
    Generates a MinMax tree structure based on the number of remaining
    red and blue marbles as well as gives each node an eval score.
    Uses the Node class to create all possible states. Also applies
    alpha-beta pruning while creating a Node. Therefore, does not
    generate a Node if it violates the properties of alpha-beta pruning
    (returns None). So the tree generated is already pruned.
    If depth is provided, then gives eval score acoording to the eval
    function described. (eval_function.txt)

    * def humanMove()-
    Called when it is the human's turn. Asks for the user's input.

    * def computerMove()-
    Called when it is the computer's turn. Uses the generate_tree function
    to decide it's action

    * def main()-
    Main function. Checks the user's initial input and starts the game.
    Displays the final results of the game.

Running instructions - python3 red_blue_nim.py 2 2 misere human