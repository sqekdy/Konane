

def minimax(position, depth, alpha,beta, maximizingPlayer):

    if (depth == 0 or game_over in position):
        return static evaluation of position

    if maximizingPlayer:

        maxEval= float("-inf")

        for child of position:

            eval= minimax(child, depth-1, alpha, beta, false)
            maxEval= max(maxEval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break

        return maxEval

    else:

        minEval= float("inf")

        for child of position:

            eval= minimax(child, depth-1, alpha, beta, true)
            minEval=min(maxEval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break

        return minEval

#minimax(currentposition, 3 , -infi, true)
