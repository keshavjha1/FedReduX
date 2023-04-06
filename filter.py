import re
import csv
def main():
    with open('c1.txt', 'r') as read_obj:
        # Load the all lines of the file into a list sperate as per timestamp and store in a map
        # with key as timestamp and value as list of lines
        # Read all lines in the file one by one
        lines = read_obj.readlines()
        # Remove newline characters from list of lines
        lines = [line.rstrip() for line in lines]
        # Print lines
        print(lines)
        # Create a dictionary to store the lines as per timestamp
        lines_dict = {}
        #Create a list to store the lines as per timestamp
        lines_list = []
        invalidList = []
        # Loop through the lines
        for line in lines:
            #define varioble to get return value from split_string function and check if it has LogModel object
            logModel = split_string(line)
            if isinstance(logModel, LogModel):
                print(logModel)
                lines_dict[logModel.timestamp] = logModel
                lines_list.append(logModel)
            else:
                invalidList.append(line)
                print("Not a valid log line")


        # save lines_dict into csv file
        try:
            with open('c1.csv', 'w') as csv_file:
                # Create a writer object from csv module
                writer = csv.writer(csv_file)
                # Write header
                writer.writerow(["log_level", "timestamp", "component", "log_message"])
                # Loop through the list of lines
                for line in lines_list:
                    # Write line to the csv file
                    writer.writerow([line.log_level, line.timestamp, line.component, line.log_message])

            with open('invalid.csv', 'w') as csv_file:
                # Create a writer object from csv module
                writer = csv.writer(csv_file)
                # Write header
                writer.writerow(["invalid log lines"])
                # Loop through the list of lines
                for line in invalidList:
                    # Write line to the csv file
                    writer.writerow([line])
            print(" Writing to the CSV file: ")

        except Exception as e:
            print("An error occurred while writing to the CSV file: ", str(e))

        # Print the dictionary
        print(lines_dict)


# Create a model to store the elements of the list
class LogModel:
    def __init__(self, log_level, timestamp, component, log_message):
        self.log_level = log_level
        self.timestamp = timestamp
        self.component = component
        self.log_message = log_message

string = "local7.debug: Jan  4 02:14:24 vsmart SYSMGR[355]: sysmgr_read_config_file[656]: %SYSMGR_DBG_MAIN-1: Starting : /usr/sbin/vdaemon -f -p vsmart  -c 3 -m 4"
string2 ="kern.info: Oct 12 10:50:34 BAE-vSmart1 kernel: \"iptables-dropped:\"IN=eth1 OUT= MAC=02:16:4b:9c:a8:1e:02:e1:da:88:fd:b2:08:00 SRC=149.32.1.241 DST=10.0.2.50 LEN=56 TOS=0x00 PREC=0x00 TTL=40 ID=0 PROTO=ICMP TYPE=5 CODE=1 GATEWAY=149.32.1.254 [SRC=160.1.62.19 DST=149.32.160.51 LEN=44 TOS=0x00 PREC=0xC0 TTL=40 ID=60430 DF PROTO=UDP SPT=12446 DPT=12406 LEN=24 ]"



# define    global variable
counter = 0
paseredCounter = 0


# write a function to split the string
def split_string(log_line):
    # split the string using : as delimiter
    string_list = log_line.split(':')
    print(string_list)
    regex = r"^(\S+\.\S+:\s+\S+\s+\d+\s+\d+:\d+:\d+)\s+(.*?):\s+(.*?)$"
    matches = re.match(regex, log_line)
    global counter
    counter = counter + 1
    global paseredCounter
    if matches:
        paseredCounter = paseredCounter + 1
        part1 = matches.group(1)
        split_firstPart = part1.split(":", 1)
        component = matches.group(2)
        log_message = matches.group(3)
        return LogModel(split_firstPart[0], split_firstPart[1], component, log_message)
    else:
        return "No match found."


# write main
if __name__ == '__main__':
    main()
    split_string("local7.debug: Jan  4 02:14:24 vsmart SYSMGR[355]: sysmgr_read_config_file[656]: %SYSMGR_DBG_MAIN-1: Starting : /usr/sbin/vdaemon -f -p vsmart  -c 3 -m 4")
    split_string(string2)
    split_string("sdsdsd")
    print("==========\n")
    print("no of string input", counter)
    print("no of string parsed", paseredCounter)


