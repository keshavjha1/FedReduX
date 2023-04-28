# write main
import os

from LogModel import LogModel
from datetime import datetime

from filter import split_string, calculateProbablityAndAssignValueToLogModel, counter, paseredCounter
import csv


def assignLabel(line, problematicTimeStamp):
    # convert the timestamps to datetime objects
    # convert the timestamps to datetime objects
    timestamp1 = datetime.strptime(problematicTimeStamp, '%b %d %H:%M:%S')
    timestamp2 = datetime.strptime(line.timestamp, ' %b  %d %H:%M:%S')

    # check if the difference between the two timestamps is within 30 seconds
    if abs((timestamp2 - timestamp1).total_seconds()) <= 30:
       return "High Critical"

    if( line.log_level=="local7.debug"):
        return "Debug"

    if (line.log_level == "local7.info"):
        return "Info"

    if(line.log_level =="local7.warn"):
        return "Warning"
    if (line.log_level == "local7.error"):
        return "Critical"
    if(line.log_level == "local7.notice"):
        return "Notice"


def main():
    with open('c2.txt', 'r') as read_obj:
        lines = read_obj.readlines()
        lines = [line.rstrip() for line in lines]

        lines_dict = {}
        lines_list = []
        invalidList = []
        for line in lines:
            logModel = split_string(line)
            if isinstance(logModel, LogModel):
                lines_dict[logModel.timestamp] = logModel
                lines_list.append(logModel)
            else:
                invalidList.append(line)
                print("Not a valid log line")

        calculateProbablityAndAssignValueToLogModel(lines_list)

        # save lines_dict into csv file
        try:
            with open('c21.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(
                    ["index", "log_level", "timestamp", "device", "component", "log_message", "json", "label"])
                for i, line in enumerate(lines_list):
                    probablity = 0.0
                    if hasattr(line, 'probability'):
                        probablity = line.probability
                    else:
                        probablity = 0.0

                    label = assignLabel(line, "Apr 5 15:46:09")
                    writer.writerow(
                        [i, line.log_level, line.timestamp, line.device, line.component, line.log_message, line.json,label])

            with open('invalid.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["invalid log lines"])
                for line in invalidList:
                    writer.writerow([line])
            print(" Writing to the CSV file: ")

        except Exception as e:
            print("An error occurred while writing to the CSV file: ", str(e))



if __name__ == '__main__':
    main()


    print("==========\n")
    print("no of string input", counter)
    print("no of string parsed", paseredCounter)



    # 3. Write a python program to read the CSV file generated in step 2 and print the following: