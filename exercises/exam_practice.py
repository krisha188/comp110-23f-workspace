def free_biscuits(games: dict[str, list[int]]):
    """My doc string."""
    result: dict[str, bool] = {}
    # loop over each key in my input dictionary
    for key in games:
        # for each element of dict, sum up its values
        sum_list: list[int] = input[key]
        sum = 0
        for element in sum_list:
            sum+= element
        if sum >= 100:
            result[key] = True
        else: 
            result[key] = False
    return result