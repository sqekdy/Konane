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
        return position.calculate_sef(), record_coordinate_of_move



    if maximizingPlayer:

        maxEval = float("-inf")

        for child in position.possible_play:

            _r = _c = _dr = _dc = None

            # Implement the play on the board
            for k, v in child.items():
                r, c = k
                dr, dc = v

                _r, _c, _dr, _dc = r, c, dr, dc
                position.update_board(dr, dc, r, c)
                break

            evaluation, coord = minimax(copy.copy(position), depth-1, alpha, beta, False)

            if evaluation > maxEval:
                record_coordinate_of_move['final'] = [_r, _c, _dr, _dc]

            maxEval= max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return maxEval, record_coordinate_of_move

    else:

        minEval= float("inf")

        for child in position.possible_play:

            _r = _c = _dr = _dc = None

            for k, v in child.items():
                r, c = k
                dr, dc = v

                _r, _c, _dr, _dc = r, c, dr, dc
                position.update_board(dr, dc, r, c)

                break

            evaluation, coord = minimax(copy.copy(position), depth-1, alpha, beta, True)

            if evaluation < minEval:
                record_coordinate_of_move['final'] = [_r, _c, _dr, _dc]

            minEval = min(minEval, evaluation)

            beta = min(beta, evaluation)
            if beta <= alpha:
                break

        return minEval, record_coordinate_of_move

#minimax(currentposition, 3 , -infi, true)
