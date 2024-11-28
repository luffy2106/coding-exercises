


def select_best_person_left(test_result : dict, threshold : int):
    """
    args 
    - test_result (dict) : the score corresponding with each superhuman
    - threshold (int) : threshold above which superwoman need to be ignore
    
    return : the name of the person to hire
    """
    filter_supper_woman = {supper_woman:score for supper_woman,score in test_result.items() if score < threshold}

    best_person  = max(filter_supper_woman, key=filter_supper_woman.get)



    return best_person





test_result = {"Quicksnail": 140, "Grey Widow": 246, "Magnetoast": 228, "Pyro Girl": 157, "Captain Confetti": 87}
threshold = 200

print(select_best_person_left(test_result, threshold))


