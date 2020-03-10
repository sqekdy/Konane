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

            is_updated = False

            # Implement the play on the board
            for k, v in child.items():
                r, c = k
                dr, dc = v

                for _player in position.player_list:
                     ai_player=_player.return_player(r,c)
                     if ai_player is not None and ai_player.player_type == position.ai_type:
                        _r, _c, _dr, _dc = r, c, dr, dc
                        position.update_board(dr, dc, r, c)
                        is_updated=True
                        break
                break                           # dictionary has one one move

            if not is_updated:
                continue

            evaluation, coord  = minimax(copy.copy(position), depth-1, alpha, beta, False)

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
            is_updated = False

            for k, v in child.items():
                r, c = k
                dr, dc = v

                for _player in position.player_list:
                     human_player=_player.return_player(r,c)
                     if human_player is not None and human_player.player_type != position.ai_type:
                        _r, _c, _dr, _dc = r, c, dr, dc
                        position.update_board(dr, dc, r, c)
                        is_updated=True
                        break
                break

            if not is_updated:
                continue

            evaluation, coord = minimax(copy.copy(position), depth-1, alpha, beta, True)

            if evaluation < minEval:
                record_coordinate_of_move['final'] = [_r, _c, _dr, _dc]

            minEval = min(minEval, evaluation)

            beta = min(beta, evaluation)
            if beta <= alpha:
                break

        return minEval, record_coordinate_of_move

#minimax(currentposition, 3 , -infi, true)
