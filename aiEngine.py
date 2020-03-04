import copy

def minimax(position, depth, alpha, beta, maximizingPlayer):
    """

    :param position: current Board object
    :param depth: number of subtrees to look forward, automatically decreased by 1 by this recursive funtion.
    :param alpha: minimum cutoff for alpha-beta pruning
    :param beta:  maximum cutoff for alpha beta pruning
    :param maximizingPlayer: boolean value that determines whether it's black turn or white turn
    :return: static evaluation value for the best possible move
    """

    game_over, winner = position.is_game_over()
    record_coordinate_of_move = dict()

    if depth == 0 or game_over:
        return position.calculate_sef()



    if maximizingPlayer:

        maxEval = float("-inf")

        for child in position.possible_play:
            # Implement the play on the board
            for k, v in child.items():
                r, c = k
                dr, dc = v
                record_coordinate_of_move['final'] = [r, c, dr, dc]
                position.update_board(dr, dc, r, c)
                break


            eval= minimax(copy.copy(position), depth-1, alpha, beta, False)
            maxEval= max(maxEval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break

        return maxEval

    else:

        minEval= float("inf")

        for child in position.possible_play:

            for k, v in child.items():
                r, c = k
                dr, dc = v
                position.update_board(dr, dc, r, c)
                record_coordinate_of_move['final'] = [r, c, dr, dc]
                break

            eval= minimax(copy.copy(position), depth-1, alpha, beta, True)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break

        return minEval

#minimax(currentposition, 3 , -infi, true)
