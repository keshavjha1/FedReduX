import os
import tarfile
import glob

# get current directory

file_names = list()


def main():
    # loop through all files in directory
    current_dir = os.getcwd()
    print(current_dir)
    # define a list to store file names

    # loop through all files in directory
    for file_name in os.listdir(current_dir):
        # check if file is .tgz file
        if file_name.endswith('.tgz'):
            # open tar file`
            tar = tarfile.open(file_name, 'r:gz')
            # remove first word upto hypen from file name
            # remove .tgz from file name
            file_name = file_name[:-4]
            # store file_name in list
            file_names.append(file_name)
            # extract all files to current directory
            tar.extractall()
            print("Extracting completed " + file_name)

            # close tar file
            tar.close()


#write main function
def child_extarct(file_names):
    #define a string variable to store current directory name
    current_dir = os.getcwd();
    for file in file_names:
        # remove tar file
        print("filename", file)
        # change directory to file

        os.chdir(current_dir+"/"+file)

        all_gz_files = glob.glob('*.gz')
        #untar tech.gz file
        #  unzip .gz extenions files in current directory and store in list
        all



        # Extract only the tech.gz files
        tech_gz_files = [file for file in all_gz_files if 'tech.gz' in file]
        for file in all_gz_files:
            if file.endswith('.gz'):
                tar = tarfile.open(file, 'r:gz')
                tar.extractall()
                tar.close()
        # Print the list of tech.gz files
        print(tech_gz_files)

if __name__ == '__main__':
    main()
    child_extarct(file_names);
