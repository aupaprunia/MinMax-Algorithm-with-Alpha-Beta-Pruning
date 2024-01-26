import argparse

class Node:
    def __init__(self, isMax, red_marbles, blue_marbles, removeRed, removeBlue, eval_score) -> None:
        self.isMax = isMax
        self.red_marbles = red_marbles # Current count of red marbles
        self.blue_marbles = blue_marbles # Current conut of blue marbles
        self.removeRed = removeRed # Remove one red marble, equivalent to left branch
        self.removeBlue = removeBlue # Remove one blue marble, equivalent to right branch
        self.eval_score = eval_score # Eval score of that node after minmax algorithm

def generate_tree(red_marbles, blue_marbles, player, alpha, beta, version, depth = None):
    player_oppo = "human"
    
    if player == "computer":
        isMax = True
    else:
        isMax = False
        player_oppo = "computer"
    
    if red_marbles != 0 and blue_marbles != 0:

        if depth is None:
            removeRed = generate_tree(red_marbles-1, blue_marbles, player_oppo, alpha, beta, version)
            removeBlue = generate_tree(red_marbles, blue_marbles-1, player_oppo, alpha, beta, version)

            if removeRed and removeBlue:
                if isMax:
                    eval_score = max(removeRed.eval_score, removeBlue.eval_score)
                    alpha = max(alpha, eval_score)
                else:
                    eval_score = min(removeRed.eval_score, removeBlue.eval_score)
                    beta = min(beta, eval_score)
            
            elif not removeRed:
                if isMax:
                    eval_score = removeBlue.eval_score
                    alpha = max(alpha, eval_score)
                else:
                    eval_score = removeBlue.eval_score
                    beta = min(beta, eval_score)
            else:
                if isMax:
                    eval_score = removeRed.eval_score
                    alpha = max(alpha, eval_score)
                else:
                    eval_score = removeRed.eval_score
                    beta = min(beta, eval_score)
        
        else:
            if depth < final_depth:
                removeRed = generate_tree(red_marbles-1, blue_marbles, player_oppo, alpha, beta, version, depth+1)
                removeBlue = generate_tree(red_marbles, blue_marbles-1, player_oppo, alpha, beta, version, depth+1)

                if removeRed and removeBlue:
                    if isMax:
                        eval_score = max(removeRed.eval_score, removeBlue.eval_score)
                        alpha = max(alpha, eval_score)
                    else:
                        eval_score = min(removeRed.eval_score, removeBlue.eval_score)
                        beta = min(beta, eval_score)
                
                elif not removeRed:
                    if isMax:
                        eval_score = removeBlue.eval_score
                        alpha = max(alpha, eval_score)
                    else:
                        eval_score = removeBlue.eval_score
                        beta = min(beta, eval_score)
                else:
                    if isMax:
                        eval_score = removeRed.eval_score
                        alpha = max(alpha, eval_score)
                    else:
                        eval_score = removeRed.eval_score
                        beta = min(beta, eval_score)
            
            elif depth == final_depth:
                removeBlue = None
                removeRed = None
                eval_score = 3*blue_marbles + 2*red_marbles
                
                if (version == "standard" and isMax) or (version == "misere" and not isMax):
                    eval_score = -eval_score


    elif red_marbles == 0 or blue_marbles == 0:
        removeBlue = None
        removeRed = None
        if red_marbles == 0:
            eval_score = 3*blue_marbles
        else:
            eval_score = 2*red_marbles
        
        if (version == "standard" and isMax) or (version == "misere" and not isMax):
            eval_score = -eval_score
    
    if beta > alpha:
            return Node(isMax, red_marbles, blue_marbles, removeRed, removeBlue, eval_score)
    
    return None

def humanMove(red_marbles, blue_marbles):
    choice = int(input("Enter which marble you would like to remove:\nPress 1 for Red\nPress 2 for Blue\n"))
    
    if choice == 1:
        return red_marbles-1, blue_marbles, "remove red marble"
    return red_marbles, blue_marbles-1, "remove blue marble"

def computerMove(red_marbles, blue_marbles, version, depth):
    root = generate_tree(red_marbles, blue_marbles, "computer", -9999999, 9999999, version, depth)
    if root.removeRed and root.removeBlue:
        if root.removeRed.eval_score > root.removeBlue.eval_score:
            return red_marbles-1, blue_marbles, "remove red marble"
        else:
            return red_marbles, blue_marbles-1, "remove blue marble"
    



def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('num_red')
    parser.add_argument('num_blue')
    parser.add_argument('version', default="standard", nargs='?')
    parser.add_argument('first_player', default="computer", nargs='?')
    parser.add_argument('depth', default=None, nargs='?')

    args = parser.parse_args()

    num_red = int(args.num_red)
    num_blue = int(args.num_blue)
    version = args.version
    first_player = args.first_player
    global final_depth
    final_depth = args.depth

    depth = None

    if final_depth:
        final_depth = int(final_depth)
        depth = -1

    red_marbles = num_red
    blue_marbles = num_blue
    isHuman = False
    

    print("Let's start the game!")
    print(f"First player will be {first_player}\n")
    
    if first_player == "human":
        isHuman = True

    while red_marbles != 0 and blue_marbles != 0:
        if depth is not None and depth == final_depth:
            break
        if isHuman:
            red_marbles, blue_marbles, action_taken = humanMove(red_marbles, blue_marbles)
            print(f"\nHuman chose to {action_taken}")
            print(f"Current Tally: Red Marbles {red_marbles} - {blue_marbles} Blue Marbles\n")
        else:
            red_marbles, blue_marbles, action_taken = computerMove(red_marbles, blue_marbles, version, depth)
            print(f"\nComputer chose to {action_taken}")
            print(f"Current Tally: Red Marbles {red_marbles} - {blue_marbles} Blue Marbles\n")
        
        if depth is not None:
            depth += 1
        isHuman = not(isHuman)
    
    if red_marbles == 0:
            final_score = blue_marbles * 3
    else:
        final_score = red_marbles * 2
    
    if version == "standard":
        if isHuman:
            print(f"Human lost by {final_score} points")
        
        else:
            print(f"Computer lost by {final_score} points")
    
    else:
        if isHuman:
            print(f"Huamn won by {final_score} points")
        
        else:
            print(f"Computer won by {final_score} points")


if __name__ == "__main__":
    main()