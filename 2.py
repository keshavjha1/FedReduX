import json
import re

def calculateProbalbility(index, json_obj_2 ,probablity_dict):

    for key, value in json_obj_2.items():
        print(key ,"    ",  value)
         # if value isjson oebject and it has eihter message or notification as key in it then print value of message or notification key
        if isinstance(value, dict) and ("message" in value or "Notification" in value):
            probablityKey= ""
            # check condition if message key is present in json object then assign value of message key to probablityKey

            if("message" in value):
                probablityKey =  value["message"]
            if ("Notification" in value):

                probablityKey = value["Notification"]

            probablityKey=  re.sub(r'\d+', '', probablityKey)

            if probablityKey in probablity_dict:
                probablity_dict[probablityKey][0] += 1
            else:
                probablity_dict[probablityKey] = [1, index]
            probablity_dict[probablityKey][1] = index








    pass

def calculateProbablityAndAssignValueToLogModel(lines_list):
    probablity_dict= {}

    calculateProbalbility(0, lines_list[0], probablity_dict)
    calculateProbalbility(1, lines_list[1], probablity_dict)

    for key, value in probablity_dict.items():
        probability = probablity_dict[key][0]/len(lines_list)
        print( lines_list[probablity_dict[key][1]] , "has probablity of " ,probability)


def main():
   #define a json varible
    json_str ="{\"%Viptela-e13sinjuk-swps900100-sysmgrd-6-INFO-1400002\":{\"2021-04-0515\":\"46:08\",\"Notification\":\"process-down\",\"severity-level\":\"major\",\"host-name\":\"e13sinjuk-swps900100\",\"system-ip\":\"::\",\"process-name\":\"vbond_0\",\"process-id\":\"2409\",\"reason\":\"Terminatedduetosignal11\"}}"
    # convert json_str into json
    json_obj = json.loads(json_str)


    print(json_obj)
    json_Str_2 ="{\"message\":{\"message\":\"RTM_DELROUTEipv4multicastprotokernel\"}}"
    json_obj_2 = json.loads(json_Str_2)
    print(json_obj_2)
    lines_list = []
    lines_list.append(json_obj)
    lines_list.append(json_obj_2)

    calculateProbablityAndAssignValueToLogModel(lines_list)





if __name__ == '__main__':
    main()