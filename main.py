# write main
from LogModel import LogModel
from filter import split_string, calculateProbablityAndAssignValueToLogModel, counter, paseredCounter
import csv

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
            with open('c2.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(
                    ["index", "log_level", "timestamp", "device", "component", "log_message", "json", "probability"])
                for i, line in enumerate(lines_list):
                    probablity = 0.0
                    if hasattr(line, 'probability'):
                        probablity = line.probability
                    else:
                        probablity = 0.0

                    writer.writerow(
                        [i, line.log_level, line.timestamp, line.device, line.component, line.log_message, line.json,
                         probablity])

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
