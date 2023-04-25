import re
import json
from LogModel import LogModel


def calculateProbalbility(index, json_obj_2, probablity_dict):
    for key, value in json.loads(json_obj_2).items():
        # if value isjson oebject and it has eihter message or notification as key in it then print value of message or notification key
        if isinstance(value, dict) and ("message" in value or "Notification" in value):
            probablityKey = ""
            # check condition if message key is present in json object then assign value of message key to probablityKey

            if ("message" in value):
                probablityKey = value["message"]
            if ("Notification" in value):
                probablityKey = value["Notification"]

            probablityKey = re.sub(r'\d+', '', probablityKey)

            if probablityKey in probablity_dict:
                currentVal = probablity_dict[probablityKey][0]
                indexlist = probablity_dict[probablityKey][1]
                indexlist.append(index)
                probablity_dict[probablityKey] = [currentVal + 1, indexlist]
            else:
                indexlist = [index]
                probablity_dict[probablityKey] = [1, indexlist]



def calculateProbablityAndAssignValueToLogModel(lines_list):
    probablity_dict = {}

    for index, line in enumerate(lines_list):
        calculateProbalbility(index, line.json, probablity_dict)


    print("keshav")
    for key, value in probablity_dict.items():
        probability = key
        print(key, "has occurance of ", probability)
        indexList = probablity_dict[key][1]
        for index in indexList:
            logmodel = lines_list[index]
            logmodel.probability = probability
            print("logmodel.probability", logmodel.probability)


    print("calculate Probability is finished")



# define    global variable
counter = 0
paseredCounter = 0


def use_regex(input_string):
    # Extract the key and value from the input string

    try:
        key, value_str = input_string.split(':', 1)

        # Extract the values from the value string
        values = {}
        value_str = value_str.strip()
        while value_str:
            try:
                colon_pos = value_str.index(':')
                key_val = [value_str[:colon_pos].strip(), '']
                value_str = str(value_str[colon_pos + 1:].strip())

                if value_str.startswith('"'):
                    value_pos = value_str.index('"', 1)
                    key_val[1] = value_str[1:value_pos]
                    value_str = value_str[value_pos + 1:].strip()
                else:
                    try:
                        space_pos = value_str.index(' ')
                    except ValueError:
                        space_pos = len(value_str)
                    key_val[1] = value_str[:space_pos]
                    value_str = value_str[space_pos:].strip()

                values[key_val[0]] = key_val[1]
            except ValueError:
                values['message'] = value_str
                value_str = ''
    except ValueError:
        key = 'message'
        values = {'message': input_string}

    # Create the JSON object
    json_obj = {key: values}

    # Convert the JSON object to a string and print it
    json_str = json.dumps(json_obj, indent=4)
    return str(json_str)


# write a function to split the string
def split_string(log_line):
    # split the string using : as delimiter
    string_list = log_line.split(':')
    regex = r"^(\S+\.\S+:\s+\S+\s+\d+\s+\d+:\d+:\d+)\s+(.*?):\s+(.*?)$"
    matches = re.match(regex, log_line)
    global counter
    counter = counter + 1
    global paseredCounter
    if matches:
        paseredCounter = paseredCounter + 1
        part1 = matches.group(1)
        split_firstPart = part1.split(":", 1)
        system = matches.group(2)
        device = system.split(" ", 1)[0]
        component = system.split(" ", 1)[1]
        log_message = matches.group(3)
        json = ''
        try:
            json = use_regex(log_message)
        except:
            json = "No json found"

        return LogModel(split_firstPart[0], split_firstPart[1], device, component, log_message, json)
    else:
        return "No match found."


