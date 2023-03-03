import os
import tarfile
import glob
import subprocess
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
        print("directory", file)
        all_gz_files = glob.glob('*.gz')
        tech_gz_files = [file for file in all_gz_files if 'tech.gz' in file]
        # Print the list of tech.gz files
        print(tech_gz_files)
        # change directory to file


        dir_path= current_dir+"/"+file;
        for filename in os.listdir(dir_path):
            # check if the file is compressed using gzip
            if filename.endswith(".gz"):
                # create the full path to the file
                filepath = os.path.join(dir_path, filename)
                print("gunziping file: " + filepath)
                # run the gunzip command using subprocess module
                subprocess.run(["gunzip", "-f", filepath])



if __name__ == '__main__':
    main()
    child_extarct(file_names);
