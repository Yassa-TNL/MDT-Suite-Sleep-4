import glob
import numpy
import os
import pandas as pd
import re
import shutil

def sort_set_1(set1_array):
    newpath = "C:\\Users\\12977\\Documents\\Jenny\\UCI 2021W\\Yassa\\SortImages\\images\\mdto_images\\Set_1"
                # Change this directory to where the images are stored, the sorted images will be stored in a folder under the Set_1 folder.  

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in range(0, 4):
        path = newpath + '\\' + 'set1-1'
        if i == 1 or i == 3:
            path = newpath+'\\'+ 'set1-2'
        if not os.path.exists(path):
            os.makedirs(path)
        
        for j in set1_array[i]:
            fname = str(j)
            if j< 10:
                fname = '00'+str(j)
            elif j < 100:
                fname = '0'+str(j)
            if i < 2:
                a = shutil.copy(newpath + '\\'+fname+'a_1.jpg', path)
                b = shutil.copy(newpath + '\\'+fname+'b_1.jpg', path)
            else:     
                a = shutil.copy(newpath + '\\'+fname+'a_2.jpg', path)
                b = shutil.copy(newpath + '\\'+fname+'b_2.jpg', path)


def copy_to_path(arr, group):
    newpath = "C:\\Users\\12977\\Documents\\Jenny\\UCI 2021W\\Yassa\\SortImages\\images\\mdto_images\\Set_2"
            # Change this directory to where the images are stored, the sorted images will be stored in a folder under the Set_1 folder.  
    
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    path = newpath+'\\'+ 'Set2-' + str(group)
    if not os.path.exists(path):
        os.makedirs(path)
    
    for j in arr:
        fname = str(j)
        if j< 10:
            fname = '00'+str(j)
        elif j < 100:
            fname = '0'+str(j)
        if os.path.exists(newpath + '\\'+fname+'a_1.jpg'):
            a = shutil.copy(newpath + '\\'+fname+'a_1.jpg', path)
            b = shutil.copy(newpath + '\\'+fname+'b_1.jpg', path)
        else:     
            a = shutil.copy(newpath + '\\'+fname+'a_2.jpg', path)
            b = shutil.copy(newpath + '\\'+fname+'b_2.jpg', path) 


def main():
    xl_file = pd.ExcelFile("MDT.xlsx")
                    # put the code in the same folder as the MDT.xlsx

    dfs = {sheet_name: xl_file.parse(sheet_name) 
              for sheet_name in xl_file.sheet_names}


    set1 = dfs['Set1'].to_numpy()[:400,:1]

    set1_1 = []
    set1_2 = []

    for i in range(0, 400, 2):
        j = re.split('a_|.jpg',set1[i][0])
        if(j[1] == '2'):
            set1_2.append(int(j[0]))
        else:
            set1_1.append(int(j[0]))

    set1_1 = numpy.array(set1_1)
    print(set1_1.shape[0])
    indices1_1 = numpy.random.permutation(set1_1.shape[0])
    training_idx1_1, test_idx1_1 = indices1_1[:50], indices1_1[50:]
    training1_1, test1_1 = set1_1[training_idx1_1], set1_1[test_idx1_1]
    print(training1_1)
    print(test1_1)
    #1_2
    set1_2 = numpy.array(set1_2)
    print(set1_2.shape[0])
    indices1_2 = numpy.random.permutation(set1_2.shape[0])
    training_idx1_2, test_idx1_2 = indices1_2[:50], indices1_2[50:]
    training1_2, test1_2 = set1_2[training_idx1_2].tolist(), set1_2[test_idx1_2].tolist()
    print(len(training1_2))
    print(len(test1_2))
    set1_array = [training1_1,test1_1,training1_2,test1_2]
    print(set1_array)

    sort_set_1(set1_array)


     ###########
    #   set 2   #
     ###########
    set2 = dfs['Set2'].to_numpy()[:400,[0,4]]
    #print(set2)
    set2_1 = []
    set2_2 = []
    set2_4 = []
    set2_5 = []

    for i in range(0, 400, 2):
        j = re.split('a_|.jpg',set2[i][0])
        if(int(set2[i][1]) == 1):
            set2_1.append(int(j[0]))
        elif(int(set2[i][1]) == 2):
            set2_2.append(int(j[0]))
        elif(int(set2[i][1]) == 4):
            set2_4.append(int(j[0]))
        elif(int(set2[i][1]) == 5):
            set2_5.append(int(j[0]))
    print(set2_1)
    print(set2_2)
    print(set2_4)
    print(set2_5)
    print(len(set2_1)+len(set2_2)+len(set2_4)+len(set2_5))


    set2_1 = numpy.array(set2_1)
    shape1 = set2_1.shape[0]
    print(shape1)
    indices2_1 = numpy.random.permutation(set2_1.shape[0])
    training_idx2_1, test_idx2_1 = indices2_1[:int(shape1/2)], indices2_1[int(shape1/2):]
    training2_1, test2_1 = set2_1[training_idx2_1], set2_1[test_idx2_1]
    print(training2_1)
    print(test2_1)
    #1_2
    set2_2 = numpy.array(set2_2)
    shape2 = set2_2.shape[0]
    print(shape2)
    indices2_2 = numpy.random.permutation(set2_2.shape[0])
    training_idx2_2, test_idx2_2 = indices2_2[:int(shape2/2)], indices2_2[int(shape2/2):]
    training2_2, test2_2 = set2_2[training_idx2_2], set2_2[test_idx2_2]
    print(training2_2)
    print(test2_2)

    set2_4 = numpy.array(set2_4)
    shape4 = set2_4.shape[0]
    print(shape4)
    indices2_4 = numpy.random.permutation(set2_4.shape[0])
    training_idx2_4, test_idx2_4 = indices2_4[:int(shape4/2)], indices2_4[int(shape4/2):]
    training2_4, test2_4 = set2_4[training_idx2_4], set2_4[test_idx2_4]
    print(training2_4)
    print(test2_4)

    set2_5 = numpy.array(set2_5)
    shape5 = set2_5.shape[0]
    print(shape5)
    indices2_5 = numpy.random.permutation(set2_5.shape[0])
    training_idx2_5, test_idx2_5 = indices2_5[:int(shape5/2+1)], indices2_5[int(shape5/2+1):]
    training2_5, test2_5 = set2_5[training_idx2_5], set2_5[test_idx2_5]
    print(training2_5)
    print(test2_5)

    copy_to_path(training2_1, 1)
    copy_to_path(training2_2, 1)
    copy_to_path(training2_4, 1)
    copy_to_path(training2_5, 1)
    copy_to_path(test2_1, 2)
    copy_to_path(test2_2, 2)
    copy_to_path(test2_4, 2)
    copy_to_path(test2_5, 2)

    

if __name__ == "__main__":
    main()
