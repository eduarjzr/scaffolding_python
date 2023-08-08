def combinations_coins(coins, goal):
    result = []

    def get_combination_coins(actual_coins, combination_coins=[]):
        actual_goal = goal - sum(combination_coins)
        if actual_goal == 0:
            result.append(combination_coins)
            get_combination_coins(actual_coins, [])
            return
        elif len(actual_coins) == 0:
            return

        coin = pick_coin(actual_coins, actual_goal)
        if (coin == None):
            return

        combination_coins.append(coin['value'])
        actual_coins = remove_coin(coin, actual_coins)
        return get_combination_coins(actual_coins, combination_coins)

    get_combination_coins(coins)
    return result


def pick_coin(pull, actual_goal):

    if len(pull) == 0:
        return None

    if (actual_goal - pull[0]['value'] >= 0):
        return pull[0]

    return pick_coin(pull[1:], actual_goal)


def remove_coin(coin_to_remove, pull):
    new_pull = []
    for coin in pull:
        if coin['value'] == coin_to_remove['value']:
            leftover = coin['quantity'] - 1

            if leftover == 0:
                continue

            new_pull.append({
                'value':  coin['value'], 'quantity': leftover,
            })
        else:
            new_pull.append(coin)
    return new_pull
