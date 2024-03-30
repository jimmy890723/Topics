# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:05:44 2019

@author: hutton
"""
from os import listdir, getcwd, mkdir
import matplotlib.pyplot as plt
import math
from pydicom import dcmread
from statistics import stdev
import numpy as np
import cv2
import os
import pandas as pd
from matplotlib import cm


def find_center(img):  # 取得重心位置
    x_total = 0
    y_total = 0
    total_num = 0
    for i in range(512):
        for j in range(512):
            if img[i][j][0] > 100:
                x_total += i
                y_total += j
                total_num += 1
    x_total = x_total / total_num
    y_total = y_total / total_num
    return (x_total, y_total)


def takeSecond(elem):
    return elem[1]


def cv_imread(file_path):
    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name)
    os.chdir(pwd)
    return cv_img


def straightLine(case_number, gauge_count, gauge):

    # 目前位置
    Nowpath = getcwd() + '\\'

    # 檔案路徑
    file_path = Nowpath + "..\\..\\Data\\" + case_number + "\\" + case_number
    # 讀取目的資料夾內所有資料名稱
    files = listdir(file_path)

    # 檔案list
    file_list = []
    # dicom list
    dicom_list = []
    # pixel_array list
    pixel_array_list = []

    # 將資料放入list中
    for f in files:
        if f.endswith('.dcm') == True:
            file_list.append(f)
            dicom_list.append(dcmread(file_path + "\\" + f))

    # 將dicom影像資料轉換成HU值
    for dcm in dicom_list:
        intercept = dcm[0x0028, 0x1052].value
        scale = dcm[0x0028, 0x1053].value
        data = (dcm.pixel_array * scale + intercept).astype('int32')
        pixel_array_list.append(data)

    # 將pixel_array 分成黑點(0)與白點(4000)
    for num in range(len(file_list)):
        for i in range(512):
            for j in range(512):
                if pixel_array_list[num][i][j] < 40:
                    pixel_array_list[num][i][j] = 4000
                else:
                    pixel_array_list[num][i][j] = 0

    # 測試
    # print(len(file_list))
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    a = pd.DataFrame(pixel_array_list[0])
    result = a.apply(pd.value_counts)
    # print(result)
    # print(pixel_array_list[0])
    # 邊緣影像路徑
    border_file_path = Nowpath + "..\\..\\Data\\" + \
        case_number + "\\effusion\\effusion_edg\\"
    # 讀取資料夾內檔案名稱
    border_files = listdir(border_file_path)
    # 取資料長度的一半
    num = len(border_files)
    num = math.floor(num/2)-1

    border = cv_imread(border_file_path + border_files[num])
    # print(border_file_path + border_files[num])
    center = find_center(border)

    floor = int(border_files[num][-6:-4]) - 1
    # 起點轉換成x,y兩點
    start_x = math.floor(center[0])
    start_y = math.floor(center[1])
    start_z = floor
    # 圖層差
    z_gap = 45 - floor
    # Z方向斜率
    line_slope = math.floor(start_x/z_gap)
    print("x:", start_x, "y:", start_y, "z:", start_z,
          "z_gap:", z_gap, "slope:", line_slope)

    # 起始圖層 28
    # 終點圖層 40

    #
    lineWidth = 3
    sortList = []
    currenty = start_y
    currentx = start_x

    for degree in range(0, 360, 3):
        ######################################
        gauge_count = gauge_count + 1
        gauge.SetValue(int((gauge_count/120)*20))
        ######################################
        arrayList = []
        lineLength = 1
        addX = 0
        addY = 0
        addZ = 3
        blackCount = 0
        whiteCount = 0

        while True:
            addX = math.floor(currentx+lineLength *
                              math.cos(math.radians(degree)))
            addY = math.floor(currenty+lineLength *
                              math.sin(math.radians(degree)))
            lineLength = lineLength+2
            if addX < 512 and addX >= 0 and addY < 512 and addY >= 0:
                widthIntercept = math.floor(lineWidth/2)
                for widthX in range(-1*widthIntercept, widthIntercept+1):
                    for widthY in range(-1*widthIntercept, widthIntercept+1):
                        if addY+widthY >= 0 and addY+widthY < 512 and addX+widthX >= 0 and addX+widthX < 512 and [addY+widthY, addX+widthX] not in arrayList:
                            arrayList.append([addY+widthY, addX+widthX])
            else:
                break

        currentCount = 0
        blackArray = []
        z_high = 0
        slope_num = 0
        for eachArray in arrayList:
            slope_num += 1
            currentCount = currentCount+1
            if slope_num > line_slope * 3:
                slope_num = 0
                z_high += 1
            if pixel_array_list[start_z + z_high][eachArray[0]][eachArray[1]] == 0:
                blackCount = blackCount+1
                blackArray.append(currentCount)
                # print("black")
            elif pixel_array_list[start_z + z_high][eachArray[0]][eachArray[1]] == 4000:
                whiteCount = whiteCount+1
                # print("white")
        if whiteCount+blackCount > 0:
            # print("fuck")
            # if (blackCount*100)/(whiteCount+blackCount) < 10:
            # if blackCount > 40:
            # deviation = stdev(blackArray)
            # else:
            deviation = 999
            # if deviation > 400:
            sortList.append([degree, (blackCount*100) /
                            (whiteCount+blackCount), arrayList])

    sortList.sort(key=takeSecond)
    # print(sortList)

    # 分數儲存
    score_list = []
    # 長度儲存
    long_list = []

    if len(sortList) > 3:
        for i in range(len(sortList)):
            # print(sortList[i][1])
            score_list.append(100-sortList[i][1])
            long_list.append(len(sortList[i][2]))
            z_high = 0
            slope_num = 0
            for eachArray in sortList[i][2]:
                slope_num += 1
                if slope_num > line_slope * 3:
                    slope_num = 0
                    z_high += 1
                dicom_list[start_z + z_high].pixel_array[eachArray[0]
                                                         ][eachArray[1]] = (2000 + (i * 2) - intercept)/scale
    save_list = listdir(Nowpath + "..\\..\\Data\\" + case_number + "\\path")
    check_file = 0
    for f in save_list:
        if '3_line_dcm' == f:
            check_file = 1
            break

    if check_file == 0:
        mkdir(Nowpath + "..\\..\\Data\\" + case_number + "\\path\\3_line_dcm")
        mkdir(Nowpath + "..\\..\\Data\\" + case_number + "\\path\\4_Astar_dcm")
        mkdir(Nowpath + "..\\..\\Data\\" + case_number + "\\path\\score")
    for i in range(len(file_list)):
        dicom_list[i].PixelData = dicom_list[i].pixel_array.tobytes()
        dicom_list[i].save_as(
            Nowpath + "..\\..\\Data\\" + case_number + "\\path\\3_line_dcm\\" + file_list[i])

    for i in range(3):
        print(long_list[i])
        print(score_list[i])
    print("success")

    score_path = '..\\..\\Data\\' + case_number + '\\path\\score\\'
    file = open(score_path + 'score.txt', 'w')
    seq = ["path1_長度:" + str(long_list[0]) + " path1_通過率:" + str(round(score_list[0], 2)) + "%" + "\n",
           "path2_長度:" +
           str(long_list[1]) + " path2_通過率:" +
           str(round(score_list[1], 2)) + "%" + "\n",
           "path3_長度:" + str(long_list[2]) + " path3_通過率:" + str(round(score_list[2], 2)) + "%"]
    file.writelines(seq)
    file.close()

    plt.figure()
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    paths = ['path_1', 'path_2', 'path_3']
    math_scores = [float(str(round(score_list[0], 2))), float(
        str(round(score_list[1], 2))), float(str(round(score_list[2], 2)))]
    x = np.arange(len(paths))
    cmap = cm.jet(np.linspace(0, 1, len(paths)))
    # plt.barh(x, math_scores, color=cmap)
    plt.barh(x, math_scores, color=['red', 'green', 'blue'] ,height=0.35)
    plt.yticks(x, paths)
    plt.text(round(score_list[0], 2) + 1, 0, str(round(score_list[0], 2)) + '%')
    plt.text(round(score_list[1], 2) + 1, 1, str(round(score_list[1], 2)) + '%')
    plt.text(round(score_list[2], 2) + 1, 2, str(round(score_list[2], 2)) + '%')
    plt.ylabel('路徑(前三順位)')
    plt.xlabel('通過率(%)')
    plt.title('路徑通過率')
    plt.xlim(xmax=np.ceil(115))
    plt.savefig(score_path + 'path_img.png')  # 儲存圖片
