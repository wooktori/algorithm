def solution(players, callings):
    dict = {player: i for i, player in enumerate(players)}
    for i in callings:
        index = dict[i]
        players[index - 1], players[index] = players[index], players[index - 1]

        dict[players[index]] = index
        dict[players[index - 1]] = index - 1

    return players
