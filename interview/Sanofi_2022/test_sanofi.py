import json


"""
Over all : 3 exerices, 10 quiz. Time to finish this exercise : 30 minutes
"""

def solution(jsonData):
    list_ans = []
    # load json to dictionary
    dict_data = json.loads(jsonData)
    for element in dict_data:
        e_des = element["description"].lower()
        e_des = e_des.replace(" ", "")
        ans = 0
        if "studio" not in e_des and "1-bed" not in e_des:
            ans = element["num_bedrooms"]
        else:
            preceding_studio = ["yogastudio", "dancestudio","artstudio"]
            preceding_1_bedroom = ["yoga1-bedroom", "dance1-bedroom", "art1-bedroom"]
            if "studio" in e_des:
                if "1-bed" not in e_des:
                    ans = 0
                else: #1-bed in e_des
                    if any(elem in e_des for elem in preceding_1_bedroom):
                        ans = 0
                    else:
                        ans = element["num_bedrooms"]
            if "1_bed" in e_des:
                if "studio" not in e_des:
                    ans = 1
                else: #studio in e_des
                    if any(elem in e_des for elem in preceding_studio):
                        ans = 1
                    else:
                        ans = element["num_bedrooms"]
        list_ans.append(ans)
    return list_ans








