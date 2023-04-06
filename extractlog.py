import os
import tarfile


def main():
    #write a fucntion to extarct file wiht name admin tech  present in admin-tech folder in current directory
    #loop through all files in directory
    current_dir = os.getcwd()
    print(current_dir)
    #define a list to store file names

    #loop through all files in directory
    for file_name in os.listdir(current_dir):
        #check if file is .tgz file
        if file_name.endswith('.tgz'):
            #open tar file`
            tar = tarfile.open(file_name, 'r:gz')
            #remove first word upto hypen from file name
            #remove .tgz from file name
            file_name = file_name[:-4]
            #store file_name in list
            file_names.append(file_name)
            #extract all files to current directory
            tar.extractall()
            print("Extracting completed "+file_name)

            #close tar file
            tar.close()




if __name__ == '__main__':
    main()
