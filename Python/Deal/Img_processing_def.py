def Img_processing_def(file_case_num,choose_type, gauge_count, gauge):
    from pydicom import dcmread
    from pydicom.data import get_testdata_files

    from os import listdir, getcwd , mkdir
    from os.path import isfile, isdir, join

    import csv

    #平均重疊率
    avg_overlap_rate = 0
    avg_dice_rate = 0
    avg_voe_rate = 0
    avg_rvd_rate = 0
    case_quantity = 0
    end = 0

    #類別與設定 effusion:(0-40); pancreas:(50-80) / 'G:effusion R:Pancreas'
    if choose_type == 'pancreas':
        file_type = 'pancreas'
        HU_Threshold_max = 80   #Threshold 原定上界
        HU_Threshold_min = 50    #Threshold 原定下界
        filter_color = 'R'
        Percentage_area = 0.25    #統計佔比多少百分比的HU值當作範圍 
    elif choose_type == 'effusion':
        file_type = 'effusion'
        HU_Threshold_max = 40   #Threshold 原定上界
        HU_Threshold_min = 0    #Threshold 原定下界
        filter_color = 'G'
        Percentage_area = 0.4    #統計佔比多少百分比的HU值當作範圍
    else:
        print('Input error!')  

    #包含與醫師的畫記的比較+txt/csv註記+儲存結果圖
    check_manual = 1
    check_write = 1
    choose_showimg = 0
    check_save = 1
    choose_Manual = 1

    #目前位置
    Nowpath = getcwd() + '\\'

    if choose_Manual == 1:
        tmp_list = []
        manual_list = listdir(Nowpath + "..\\..\\Data\\" + file_case_num + "\\" + file_type)
        for f in manual_list:
            if f.endswith('_jpg'):
                tmp_list.append(f)
        file_case_jpg = tmp_list[0]

    # 指定要列出所有檔案的目錄 
    file_path =  Nowpath + "..\\..\\Data\\" + file_case_num + "\\"
    file_DIC_class = file_path + file_case_num    
    file_xml_check = 1
    file_xml_check_list = listdir(file_path + file_type) 
    for f in file_xml_check_list:
        if f.endswith("xml") ==  True:
            file_xml_check = 0
            break
    if file_xml_check == 1:
        mkdir(file_path + file_type + "\\" + file_type + "_xml")
    file_XML_class = file_path + file_type + "\\" + file_type + "_xml"
    if choose_Manual == 1:
        file_JPG_class = file_path + file_type + "\\" + file_case_jpg

    fileExt = ".xml"
    # 取得所有檔案與子目錄名稱
    files = listdir(file_XML_class) 

    file_xml = []

    for f in files:
    # 產生檔案的絕對路徑
    #fullpath = join(file_XML_class, f)
        if f.endswith(fileExt):
            file_xml.append(f)
            case_quantity += 1

    #print("xml_檔案：", file_xml)

    file_DIC_path =  file_DIC_class +'\\'
    file_XML_path =  file_XML_class +'\\'
    if check_manual == 1:
        file_JPG_path =  file_JPG_class +'\\'

    save_list = listdir(file_path + file_type)
    file_checkname = file_type + '_ove' 
    file_check = 0

    for f in save_list:
        if f == file_checkname:
            file_check = 1
            break

    if file_check == 0:
        if file_type == 'effusion':
            mkdir(file_path + "path" + "\\1_" + file_type + "_dcm")
        elif file_type == 'pancreas':
            mkdir(file_path + 'path' + "\\2_" + file_type + "_dcm")
        mkdir(file_path + file_type + "\\" + file_type + "_obj")
        mkdir(file_path + file_type + "\\" + file_type + "_edg")
        mkdir(file_path + file_type + "\\" + file_type + "_ove")
        mkdir(file_path + file_type + "\\" + file_type + "_txt")
        mkdir(file_path + file_type + "\\" + file_type + "_seg")

    #開啟要編寫的txt檔
    if check_write == 1:
        Output_txt = file_path + file_type + '\\' + file_type + '_ove' +'\\'+ 'Output.txt'
        op_f = open(Output_txt, 'w')
        op_f.write('案例碼: '+ file_case_num + '\n')
        op_f.write('型態: '+ file_type + '\n')
        op_f.write('被圈選的切片數量: '+ str(case_quantity) + '\n')

        Output_csv = file_path + file_type + '\\' + file_type + '_ove' +'\\'+ 'Output.csv'
        csvfile = open(Output_csv, 'w', newline='')
        op_csv = csv.writer(csvfile)
        op_csv.writerow(['No.', 'DICE', 'VOE', 'RVD'])

    #判斷dcm的file跟xml的file名稱編寫的規則是否一致 (name_unified)
    files_dc = listdir(file_DIC_class) 
    fileExt_dc = '.dcm'
    file_dcm = []
    file_num = []

    for f in files_dc:
        if f.endswith(fileExt_dc):
            file_dcm.append(f)
            file_num.append(f.replace(fileExt_dc,""))

    check_xml_null = 0
    if case_quantity == 0:
        check_xml_null = 1
        if file_type == 'effusion':
            op_f.write('This case doesn`t detect any effusion.\n')
            print('This case doesn`t detect any effusion.\n')
        elif file_type == 'pancreas':
            op_f.write('This case doesn`t detect any pancreas.\n')
            print('This case doesn`t detect any pancreas.\n')

    if check_xml_null == 1 and check_save == 1:
        for case_dcm in file_dcm:
            ds = dcmread(file_DIC_path + case_dcm)
            rescale_intercept = int(ds[0x0028, 0x1052].value)
            rescale_slope = int(ds[0x0028, 0x1053].value)
            
            if file_type == 'pancreas':
                ds.save_as(file_path + 'path' + '\\2_' + file_type + '_dcm' +'\\'+ case_dcm)
            elif file_type == 'effusion':
                for i in range(512):
                    for j in range(512):
                        ds.pixel_array[i][j] = (-1020-rescale_intercept)/rescale_slope
                ds.PixelData = ds.pixel_array.tobytes()
                ds.save_as(file_path + 'path' + '\\1_' + file_type + '_dcm' +'\\'+ case_dcm)
    elif check_xml_null == 0:
        
        name_unified = 0
        for f in file_dcm:
            if f == file_xml[0].replace(".xml",".dcm"):
                name_unified = 1
                break

        N_xml_dcm = []
        case_dcm = []
          
        for f in file_num:
            check_found = 0
            tmp_f = f + '.dcm'
            for case_xml in file_xml:
                if f in case_xml:
                    case_dcm.append(tmp_f)
                    check_found = 1
                    break    
            if check_found == 0:
                N_xml_dcm.append(tmp_f)
        
        if check_save == 1:
            for case_dcm in N_xml_dcm:
                print('case num:',case_dcm.replace(".dcm", ""))
                ds = dcmread(file_DIC_path + case_dcm)
                rescale_intercept = int(ds[0x0028, 0x1052].value)
                rescale_slope = int(ds[0x0028, 0x1053].value)
                
                if file_type == 'pancreas':
                    ds.save_as(file_path + 'path' + '\\2_' + file_type + '_dcm' +'\\'+ case_dcm)
                elif file_type == 'effusion':
                    for i in range(512):
                        for j in range(512):
                            ds.pixel_array[i][j] = (-1020-rescale_intercept)/rescale_slope
                    ds.PixelData = ds.pixel_array.tobytes()
                    ds.save_as(file_path + 'path' + '\\1_' + file_type + '_dcm' +'\\'+ case_dcm)
        
        case_counter = 0
        #處理並儲存有xml的case
        for case_xml in file_xml:
            end = end + 1
        for case_xml in file_xml:
            ######################################
            gauge_count = gauge_count + 1 
            gauge.SetValue(int((gauge_count/end)*20))
            ######################################
            case_counter += 1
            if check_write == 1:
                Output_slice = file_path + file_type + '\\' + file_type + '_txt' +'\\'+ case_xml.replace(".xml", ".txt") 
                op_slice = open(Output_slice, 'w')
                op_slice.write('案例碼: '+ file_case_num + '\n')
                op_slice.write('型態: '+ file_type + '\n')
                op_slice.write('切片編號: '+ case_xml.replace(".xml", "") + '\n')

            if name_unified == 0:
                for f in file_num:
                    if f in case_xml:
                        case_dcm = f + '.dcm'
                        break
                ds = dcmread(file_DIC_path + case_dcm)
            else:
                ds = dcmread(file_DIC_path + case_xml.replace(".xml", ".dcm"))  
                case_dcm = case_xml.replace(".xml", ".dcm")

            print('case num:',case_dcm.replace(".dcm", ""))

            import matplotlib.pyplot as plt
            import seaborn as sns
            import pandas as pd
            import math

            def HU2Pixel(image_array, slope, intercept):
                # Hu = pixel * slope + intercept
                image_array = (image_array + intercept)/ slope
                return image_array

            def normalizationDCM(image_array, hu_max, hu_min):
                image_array = (image_array - hu_min) / (hu_max - hu_min)

                return image_array * 255

            import numpy as np
            import cv2
            from PIL import Image

            # 設定原始像素值範圍
            pmax = ds.LargestImagePixelValue
            pmin = ds.SmallestImagePixelValue

            # 設定slope和intercept
            rescale_intercept = int(ds[0x0028, 0x1052].value)
            rescale_slope = int(ds[0x0028, 0x1053].value)

            # 轉化成HU值
            Or_Image = ds.pixel_array
            '''
            plt.figure('Ori_HU')
            plt.title('Ori_HU')
            plt.imshow(Or_Image, cmap=plt.cm.gray)
            plt.axis('off')
            '''
            #Re_Image = Or_Image * ds.RescaleSlope + ds.RescaleIntercept
            Re_Image = HU2Pixel(Or_Image, rescale_slope, rescale_intercept)
            '''
            plt.figure('Trans_HU')
            plt.title('Trans_HU')
            plt.imshow(Re_Image, cmap=plt.cm.gray)
            plt.axis('off')
            plt.show()    
            '''
            #窗位窗寬映射 (對比度)
            Win_HU = np.array(Re_Image)

            WL = 70
            WW = 250
            WMin = (((WW/2) * -1) + WL)
            WMax = (((WW/2) * 1) + WL)
            CutOff = WW/ 2
            Win_HU[ Win_HU <= WMin] = WMin
            Win_HU[ (Win_HU >= WMax) & (Win_HU < CutOff)] = WMin
            Win_HU[ Win_HU >= CutOff] = WMax

            if choose_showimg == 1:
                plt.figure('Window_HU')
                plt.title('Window_HU')
                plt.imshow(Win_HU, cmap=plt.cm.gray)
                plt.axis('off')
                plt.show()

            HU_min = (pmin + rescale_intercept) / rescale_slope
            HU_max = (pmax + rescale_intercept) / rescale_slope

            # 轉換為 0 ~ 255 的像素值 (儲存圖像防止對比度跑掉的必經步驟)
            rescale = normalizationDCM(Win_HU, WMax, WMin)

            #讀取 xml
            import xml.etree.ElementTree as ET

            tree = ET.parse(file_XML_path + case_xml)
            root = tree.getroot()

            counter = 0

            for count in root.iter('object'):
                counter = counter + 1

            bdarray = np.zeros((counter,4), dtype=int)

            counter_2 = 0
            for finder in root.findall('object'):
                for finder_2 in finder.findall('bndbox'):
                    x_min = finder_2.find('xmin').text
                    x_max = finder_2.find('xmax').text
                    y_min = finder_2.find('ymin').text
                    y_max = finder_2.find('ymax').text
                    bdarray[counter_2] = [x_min, x_max, y_min, y_max]
                    counter_2 = counter_2 + 1

            for i in range(counter): 
                print(bdarray[i])

            '''
            以下是做與醫師畫記比對時使用
            '''
            #查看醫師手繪的區域內HU值狀況
            def converted(path_dir, filter_color):
                img_path = path_dir
                filtered_img = single_image_filter_color(img_path, filter_color)
                                            
                #cv2.imshow('first',filtered_img)
                #cv2.waitKey()
                check_manual = check_Manual_real(filtered_img)

                if check_manual == 1:
                    mask = filtered_img
                    mask.setflags(write = 1)
                    mask[mask != 255] = 0
                    image = mask
                    
                    filled_up = detect_rect_on_image(image)
                else:
                    filled_up = filtered_img
                
                return filled_up

            #根據醫師畫記的顏色來判斷擷取目標
            def single_image_filter_color(img_path, filter_color):
                img = Image.open(img_path)
                img = np.asarray(img)
                filtered_img = img
                
                if filter_color  == "G":
                    filtered_img = cv2.inRange( img, 
                                                np.array([ 0, 100,  0]), 
                                                np.array([80, 255, 80]))
                elif filter_color  == "R":
                    filtered_img = cv2.inRange( img, 
                                                np.array([100,  0,  0]), 
                                                np.array([255, 40, 40]))
                
                return filtered_img

            #內外輪廓填充
            def detect_rect_on_image(filtered_img):

                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))   
                img_rect = cv2.morphologyEx( filtered_img, 
                                            cv2.MORPH_CLOSE, 
                                            kernel,iterations=2)
                # print ("contours type ", type(contours))
                image, contours, hierarchy = cv2.findContours(img_rect, 
                                                    cv2.RETR_CCOMP,
                                                    3)
                hierarchy = np.squeeze(hierarchy)
                for i in range(len(contours)):
                    # 存在內轮廓，說明在裡層
                    if (hierarchy[i][3] != -1):
                        img_draw = cv2.drawContours(img_rect, contours, i, 255, -1)
                
                #print ("contours len: ", len(contours))

                return img_draw

            #檢查醫師是否有畫記
            def check_Manual_real(img):
                i = 0
                j = 0
                check_point = 0

                while j < 512:
                    while i < 512:
                        if img[i][j] > 0:
                            check_point = 1
                            break
                        i += 1
                    if check_point == 1:
                        break
                    j += 1
                    i = 0
                
                return check_point

            #掃描影像並找最大最小值
            def detect_img(img1,img2):
                i = 0
                j = 0
                max = img1[i][0]
                min = img1[1][0]

                while j < 512:
                    while i < 512:
                        if img2[i][j] > 1:
                            max = compare_big(max,img1[i][j])
                            min = compare_small(min,img2[i][j])
                        i += 1
                    j += 1
                    i = 0
                
                return max,min 

            def compare_big(val1,val2):
                if val1 > val2:
                    tmp = val1
                else:
                    tmp = val2

                return tmp

            def compare_small(val1,val2):
                if val1 < val2:
                    tmp = val1
                else:
                    tmp = val2

                return tmp

            def Manual_HU(img1,img2,HU_min):
                i = 0
                j = 0
                counts = 0

                while j < 512:
                    while i < 512:
                        if img2[i][j] == 0:
                            img1[i][j] = HU_min       
                            counts += 1
                        i += 1
                    j += 1
                    i = 0
                
                return img1,counts 

            if check_manual == 1:
                '''
                if check_write == 1:
                    op_f.write('Img number: '+ case_dcm.replace(".dcm", "") + '\n')
                '''
                #讀取jpg查看像素點位置並修改像素值    
                path_dir = file_JPG_path + case_dcm.replace(".dcm", ".jpg")
                JPG_Image = cv2.imread(path_dir)
                filled_up = converted(path_dir, filter_color)

                filled_total_pixel = pd.Series(filled_up.flatten()).value_counts().values[0]

                Manual_max,Manual_min = detect_img(Re_Image,filled_up)
                print('Manual_img range of HU: '+ str(Manual_min) +' ~ '+ str(Manual_max))

                Manual_img = np.array(Re_Image)

                Manual_total_pixel = sum(pd.Series(Manual_img.flatten()).value_counts().values)
                '''
                if filled_total_pixel == Manual_total_pixel:
                    HU_min_counts = 0
                else:
                '''    
                Manual_img,HU_min_counts = Manual_HU(Manual_img,filled_up,HU_min)
                
            # 出現頻率80%的HU值 (histogram)
            # series內的面積佔比由大至小依序累加，直到超過80%的醫師畫記面積
            def calculate_Percentage(img,total_counts,HU_Threshold_max,HU_Threshold_min,percentage):
                '''
                print('value_0:',pd.Series(img.flatten()).value_counts().values[0] )
                print('value_1:',pd.Series(img.flatten()).value_counts().values[1] )
                print('index_0:',pd.Series(img.flatten()).value_counts().index[0] )
                print('index_1:',pd.Series(img.flatten()).value_counts().index[1] )
                '''
                keep_counts = pd.Series(img.flatten()).value_counts().values[1]
                
                count_index = 2
                total_counts = total_counts * percentage
                keep_add = 0
                
                while keep_add == 0:
                    if keep_counts < total_counts:
                        keep_counts += pd.Series(img.flatten()).value_counts().values[count_index] 
                        count_index += 1
                    else:
                        keep_add = 1

                #原本是設定為學理上的HU值，現在改為序列內的第一個
                index_max =  pd.Series(img.flatten()).value_counts().index[1]   
                index_min =  pd.Series(img.flatten()).value_counts().index[1]

                for i in range(2,count_index):
                    tmp = pd.Series(img.flatten()).value_counts().index[i]
                    print('index:',tmp)
                    if tmp < (HU_Threshold_max + 20) and tmp > (HU_Threshold_min - 20) :
                        index_max = compare_big(index_max,tmp)
                        index_min = compare_small(index_min,tmp)
                
                print('index_max:',index_max)
                print('index_min:',index_min)

                return index_max,index_min,count_index

            #判斷type，來修改HU值
            def Check_type(Type,HU_max,HU_min,HU_Threshold_max,HU_Threshold_min):
                if Type == 'pancreas':
                    '''
                    if HU_max > HU_Threshold_max + 5:
                        HU_max = HU_Threshold_max + 5 
                    '''
                    if HU_min < HU_Threshold_min - 5:
                        HU_min = HU_Threshold_min - 5
                    if HU_max < HU_Threshold_max - 5:
                        HU_max = HU_Threshold_max - 5
                    if HU_min > HU_Threshold_min + 5:
                        HU_min = HU_Threshold_min + 5
                return HU_max,HU_min
            '''
            if check_manual == 1:
                print('total_pixel:',len(Manual_img.flatten()))
                Manual_total_counts = len(Manual_img.flatten()) - HU_min_counts
                print('Manual_total_count:',Manual_total_counts)
                #Manual_index_max, Manual_index_min, Manual_count_index = calculate_Percentage(Manual_img,Manual_total_counts,HU_Threshold_max,HU_Threshold_min,Percentage_area) 
            ''' 
            # Histogram
            def Show_Histogram(img,count_index,num,percentage):
                plt.figure(num)
                top = pd.Series(img.flatten()).value_counts().index[1:count_index]
                sns.countplot(y = img.flatten(), order = top,
                            color = "g", orient = "h")
                plt.title('Index that accounts for '+ str(percentage) +'% HU value & its counts')
                plt.xlabel('Counts')
                plt.ylabel('Index that accounts for '+ str(percentage) +'% HU value')

            #Show_Histogram(Manual_img,Manual_count_index,3,20)
            #plt.show()
            #手繪圖內的閥值外區塊圖顯示
            def Manual_Threshold(img,Th1,Th2,HU_min,HU_max):
                i = 0
                j = 0
                counts = 0

                while j < 512:
                    while i < 512:
                        if img[i][j] > HU_min and img[i][j] < Th1 :
                            img[i][j] = HU_max       
                        elif img[i][j] > Th1 and img[i][j] < Th2 :
                            img[i][j] = HU_max    
                        i += 1
                    j += 1
                    i = 0
                
                return img 
            '''
            if check_manual == 1:
                Manual_threshold = np.array(Manual_img)
                Manual_threshold = Manual_Threshold(Manual_threshold,Manual_index_min,Manual_index_max,HU_min,HU_max)
            '''

            #範圍內負數修補
            def Manual_negative(img,num):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if img[i][j] < 0 and img[i][j] >= num :
                            img[i][j] = 1      
                        i += 1
                    j += 1
                    i = 0
                
                return img

            if check_manual == 1:
                Tran_Mamual_Img = np.array(Manual_img)
                Tran_Mamual_Img = Manual_negative(Tran_Mamual_Img,HU_Threshold_min-100)

            #局部處理
            '''
            JPG的處理是對應後續與醫師的比對，若沒有相關的操作可以略過
            '''
            if check_manual == 1:
                Origin_JPG = np.array(JPG_Image)

                JPG_Image[:,0:bdarray[0][0]] = 0
                JPG_Image[:,bdarray[0][1]:] = 0
                JPG_Image[:bdarray[0][2],bdarray[0][0]:bdarray[0][1]] = 0
                JPG_Image[bdarray[0][3]:,bdarray[0][0]:bdarray[0][1]] = 0

                #判斷需要存取多少個bounding box (目前只完成2個與3個的版本)
                if counter == 2:
                    #先將bounding box 內的影像存起
                    box_data_1 = np.array(Origin_JPG)
                    box_data_1[:,0:bdarray[1][0]] = 0
                    box_data_1[:,bdarray[1][1]:] = 0
                    box_data_1[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = 0
                    box_data_1[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = 0

                    JPG_Image += box_data_1
                    #cv2.imshow('JPG_Have2part', JPG_Image)
                elif counter == 3:
                    #先將bounding box 內的影像存起
                    box_data_1 = np.array(Origin_JPG)
                    box_data_1[:,0:bdarray[1][0]] = 0
                    box_data_1[:,bdarray[1][1]:] = 0
                    box_data_1[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = 0
                    box_data_1[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = 0

                    box_data_2 = np.array(Origin_JPG)
                    box_data_2[:,0:bdarray[2][0]] = 0
                    box_data_2[:,bdarray[2][1]:] = 0
                    box_data_2[:bdarray[2][2],bdarray[2][0]:bdarray[2][1]] = 0
                    box_data_2[bdarray[2][3]:,bdarray[2][0]:bdarray[2][1]] = 0

                    JPG_Image += box_data_1
                    JPG_Image += box_data_2
                    #cv2.imshow('JPG_Have3part', JPG_Image) 

            #由於之後是採用不同的bounding-box採用不同的閥值，因此在對各個不同的bd做局部處理後，將接著做二值化，最後再將圖像組合
            '''
            #threshold(img,閥值,最大灰階值)
            #THRESH_BINARY:小於門檻值 = 0 ，大於則設為最大灰階值   
            #THRESH_TOZERO:小於門檻值 = 0 ，大於則不變      THRESH_TOZERO_INV:大於門檻值 = 0，小於則不變
            #Threshold method = ['BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
            '''
            #test for 局部修改pixel值  [y軸,x軸]   ex:bounding box[215:315,275:400]
            Par_Image = np.array(Re_Image)
            Origin_ParImg = np.array(Par_Image)
            Par_Image[:,0:bdarray[0][0]] = 0
            Par_Image[:,bdarray[0][1]:] = 0
            Par_Image[:bdarray[0][2],bdarray[0][0]:bdarray[0][1]] = 0
            Par_Image[bdarray[0][3]:,bdarray[0][0]:bdarray[0][1]] = 0

            Par_1_Img = np.array(Par_Image)
            Par_1_Img[:,0:bdarray[0][0]] = HU_min
            Par_1_Img[:,bdarray[0][1]:] = HU_min
            Par_1_Img[:bdarray[0][2],bdarray[0][0]:bdarray[0][1]] = HU_min
            Par_1_Img[bdarray[0][3]:,bdarray[0][0]:bdarray[0][1]] = HU_min

            Img_total_counts_1 = (bdarray[0][1] - bdarray[0][0]) * (bdarray[0][3] - bdarray[0][2]) 
            Img_index_max_1,Img_index_min_1,Img_count_index_1 = calculate_Percentage(Par_1_Img,Img_total_counts_1,HU_Threshold_max,HU_Threshold_min,Percentage_area)
            #Show_Histogram(Par_1_Img,Img_count_index_1,2,20)
            #plt.show()
            Img_index_max_1,Img_index_min_1 = Check_type(file_type,Img_index_max_1,Img_index_min_1,HU_Threshold_max,HU_Threshold_min)

            print('HU_Range_1:',Img_index_min_1,'~',Img_index_max_1)

            #下面是做二值化的部分，由於同樣是要分有多少個bounding box來做處理，所以就先寫在這裡 
            Tran_Par_Image_1 = Manual_negative(Par_1_Img,Img_index_min_1)
            ret,Par_dst_1 = cv2.threshold(Tran_Par_Image_1,0,255,cv2.THRESH_TOZERO)
            ret,Par_dst_1 = cv2.threshold(Par_dst_1,Img_index_max_1,255,cv2.THRESH_TOZERO_INV)
            if Img_index_min_1 < 0:
                Img_index_min_1 = 0
            ret,Par_dst_1 = cv2.threshold(Par_dst_1,Img_index_min_1,255,cv2.THRESH_BINARY)    #後面的'一起做二值化'是把目標變成index_HU_max

            Par_saving = np.array(Par_dst_1)
            #修改濾除區域的HU值_2
            def filter_HU_2(img,bdarray,HU_min):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if j > bdarray[0][0] and j < bdarray[0][1] and i > bdarray[0][2] and i < bdarray[0][3]:
                            i += 1
                            continue 
                        elif j > bdarray[1][0] and j < bdarray[1][1] and i > bdarray[1][2] and i < bdarray[1][3]:
                            i += 1
                            continue 
                        else:
                            img[i][j] = HU_min
                        i += 1
                    j += 1
                    i = 0
                
                return img

            #修改濾除區域的HU值_3
            def filter_HU_3(img,bdarray,HU_min):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if j > bdarray[0][0] and j < bdarray[0][1] and i > bdarray[0][2] and i < bdarray[0][3]:
                            i += 1
                            continue 
                        elif j > bdarray[1][0] and j < bdarray[1][1] and i > bdarray[1][2] and i < bdarray[1][3]:
                            i += 1
                            continue
                        elif j > bdarray[2][0] and j < bdarray[2][1] and i > bdarray[2][2] and i < bdarray[2][3]:
                            i += 1
                            continue  
                        else:
                            img[i][j] = HU_min
                        i += 1
                    j += 1
                    i = 0
                
                return img

            if counter == 1:
                #plt.show()
                Par_Image[:,0:bdarray[0][0]] = HU_min
                Par_Image[:,bdarray[0][1]:] = HU_min
                Par_Image[:bdarray[0][2],bdarray[0][0]:bdarray[0][1]] = HU_min
                Par_Image[bdarray[0][3]:,bdarray[0][0]:bdarray[0][1]] = HU_min    

                Img_total_counts = (bdarray[0][1] - bdarray[0][0]) * (bdarray[0][3] - bdarray[0][2])
            #判斷需要存取多少個bounding box (目前只完成2個與3個的版本)
            elif counter == 2:
                #先將bounding box 內的影像存起
                box_data_1 = np.array(Origin_ParImg)
                box_data_1[:,0:bdarray[1][0]] = 0
                box_data_1[:,bdarray[1][1]:] = 0
                box_data_1[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = 0
                box_data_1[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = 0

                Par_Image += box_data_1
                Par_Image = filter_HU_2(Par_Image,bdarray,HU_min)
                
                #cv2.imshow('Have2part', Par_Image)

                Img_total_counts = (bdarray[0][1] - bdarray[0][0]) * (bdarray[0][3] - bdarray[0][2]) + (bdarray[1][1] - bdarray[1][0]) * (bdarray[1][3] - bdarray[1][2])

                Par_2_Img = np.array(box_data_1)
                Par_2_Img[:,0:bdarray[1][0]] = HU_min
                Par_2_Img[:,bdarray[1][1]:] = HU_min
                Par_2_Img[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = HU_min
                Par_2_Img[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = HU_min

                Img_total_counts_2 = (bdarray[1][1] - bdarray[1][0]) * (bdarray[1][3] - bdarray[1][2]) 
                Img_index_max_2,Img_index_min_2,Img_count_index_2 = calculate_Percentage(Par_2_Img,Img_total_counts_2,HU_Threshold_max,HU_Threshold_min,Percentage_area)
                Img_index_max_2,Img_index_min_2 = Check_type(file_type,Img_index_max_2,Img_index_min_2,HU_Threshold_max,HU_Threshold_min)

                print('HU_Range_2:',Img_index_min_2,'~',Img_index_max_2)
                #Show_Histogram(Par_2_Img,Img_count_index_2,2,Percentage_area*100)
                #plt.show()

                #下面是做二值化的部分，由於同樣是要分有多少個bounding box來做處理，所以就先寫在這裡 
                Tran_Par_Image_2 = Manual_negative(Par_2_Img,Img_index_min_2)
                ret,Par_dst_2 = cv2.threshold(Tran_Par_Image_2,0,255,cv2.THRESH_TOZERO)
                ret,Par_dst_2 = cv2.threshold(Par_dst_2,Img_index_max_2,255,cv2.THRESH_TOZERO_INV)
                if Img_index_min_2 < 0:
                    Img_index_min_2 = 0
                ret,Par_dst_2 = cv2.threshold(Par_dst_2,Img_index_min_2,255,cv2.THRESH_BINARY)    #後面的'一起做二值化'是把目標變成index_HU_max

                Par_saving += Par_dst_2
            elif counter == 3:
                #先將bounding box 內的影像存起
                box_data_1 = np.array(Origin_ParImg)
                box_data_1[:,0:bdarray[1][0]] = 0
                box_data_1[:,bdarray[1][1]:] = 0
                box_data_1[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = 0
                box_data_1[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = 0

                box_data_2 = np.array(Origin_ParImg)
                box_data_2[:,0:bdarray[2][0]] = 0
                box_data_2[:,bdarray[2][1]:] = 0
                box_data_2[:bdarray[2][2],bdarray[2][0]:bdarray[2][1]] = 0
                box_data_2[bdarray[2][3]:,bdarray[2][0]:bdarray[2][1]] = 0

                Par_Image += box_data_1
                Par_Image += box_data_2
                Par_Image = filter_HU_3(Par_Image,bdarray,HU_min)

                #cv2.imshow('Have3part', Par_Image) 

                Img_total_counts = (bdarray[0][1] - bdarray[0][0]) * (bdarray[0][3] - bdarray[0][2]) + (bdarray[1][1] - bdarray[1][0]) * (bdarray[1][3] - bdarray[1][2]) + (bdarray[2][1] - bdarray[2][0]) * (bdarray[2][3] - bdarray[2][2])

                Par_2_Img = np.array(box_data_1)
                Par_2_Img[:,0:bdarray[1][0]] = HU_min
                Par_2_Img[:,bdarray[1][1]:] = HU_min
                Par_2_Img[:bdarray[1][2],bdarray[1][0]:bdarray[1][1]] = HU_min
                Par_2_Img[bdarray[1][3]:,bdarray[1][0]:bdarray[1][1]] = HU_min

                Img_total_counts_2 = (bdarray[1][1] - bdarray[1][0]) * (bdarray[1][3] - bdarray[1][2]) 
                Img_index_max_2,Img_index_min_2,Img_count_index_2 = calculate_Percentage(Par_2_Img,Img_total_counts_2,HU_Threshold_max,HU_Threshold_min,Percentage_area)
                Img_index_max_2,Img_index_min_2 = Check_type(file_type,Img_index_max_2,Img_index_min_2,HU_Threshold_max,HU_Threshold_min)
                print('HU_Range_2:',Img_index_min_2,'~',Img_index_max_2)

                Par_3_Img = np.array(box_data_2)
                Par_3_Img[:,0:bdarray[2][0]] = HU_min
                Par_3_Img[:,bdarray[2][1]:] = HU_min
                Par_3_Img[:bdarray[2][2],bdarray[2][0]:bdarray[2][1]] = HU_min
                Par_3_Img[bdarray[2][3]:,bdarray[2][0]:bdarray[2][1]] = HU_min

                Img_total_counts_3 = (bdarray[2][1] - bdarray[2][0]) * (bdarray[2][3] - bdarray[2][2]) 
                Img_index_max_3,Img_index_min_3,Img_count_index_3 = calculate_Percentage(Par_3_Img,Img_total_counts_3,HU_Threshold_max,HU_Threshold_min,Percentage_area)
                Img_index_max_3,Img_index_min_3 = Check_type(file_type,Img_index_max_3,Img_index_min_3,HU_Threshold_max,HU_Threshold_min)
                print('HU_Range_3:',Img_index_min_3,'~',Img_index_max_3)

                #Show_Histogram(Par_2_Img,Img_count_index_2,2,Percentage_area*100)
                #Show_Histogram(Par_3_Img,Img_count_index_3,3,Percentage_area*100)
                #plt.show()
                #下面是做二值化的部分，由於同樣是要分有多少個bounding box來做處理，所以就先寫在這裡 
                Tran_Par_Image_2 = Manual_negative(Par_2_Img,Img_index_min_2)
                ret,Par_dst_2 = cv2.threshold(Tran_Par_Image_2,0,255,cv2.THRESH_TOZERO)
                ret,Par_dst_2 = cv2.threshold(Par_dst_2,Img_index_max_2,255,cv2.THRESH_TOZERO_INV)
                if Img_index_min_2 < 0:
                    Img_index_min_2 = 0
                ret,Par_dst_2 = cv2.threshold(Par_dst_2,Img_index_min_2,255,cv2.THRESH_BINARY)    #後面的'一起做二值化'是把目標變成index_HU_max

                Tran_Par_Image_3 = Manual_negative(Par_3_Img,Img_index_min_3)
                ret,Par_dst_3 = cv2.threshold(Tran_Par_Image_3,0,255,cv2.THRESH_TOZERO)
                ret,Par_dst_3 = cv2.threshold(Par_dst_3,Img_index_max_3,255,cv2.THRESH_TOZERO_INV)
                if Img_index_min_3 < 0:
                    Img_index_min_3 = 0
                ret,Par_dst_3 = cv2.threshold(Par_dst_3,Img_index_min_3,255,cv2.THRESH_BINARY)    #後面的'一起做二值化'是把目標變成index_HU_max
                Par_saving += Par_dst_2
                Par_saving += Par_dst_3
            '''    
            plt.figure('Par_HU')
            plt.title('Par_HU')
            plt.imshow(Par_Image, cmap=plt.cm.gray)
            plt.axis('off')
            '''
            if choose_showimg == 1:
                plt.figure('Partial_separate_binary')
                plt.title('Partial_separate_binary')
                plt.imshow(Par_saving, cmap=plt.cm.gray)
                plt.axis('off')
                plt.show()

            '''
            connected-component
            '''
            #MedianBlur中值模糊
            Tran_dst_uint = Par_saving.astype(np.uint8)
            Blr_dst = cv2.medianBlur(Tran_dst_uint,5)
            #cv2.imshow("MedianBlur",Blr_dst)

            def cal_areas(img):
                i = 0
                j = 0
                count = 0
                while j < 512:
                    while i < 512:
                        if img[i][j] > 0:
                            count += 1
                        i += 1
                    j += 1
                    i = 0
                
                return count

            cal_area = cal_areas(Blr_dst)
            print('MedianBlur_area:',cal_area)
            #connected component labeling
            #針對thresholded圖片進行connected components analysis，
            # neighbors=8表示採用8向方式, background=0表示pixel值為0則認定為背景
            from skimage import measure
            labels = measure.label(Blr_dst, neighbors=8, background=0)  

            #建立一個空的圖，存放稍後將篩選出的字母及數字
            cc_mask = np.zeros(Par_saving.shape, dtype='uint8')

            region = measure.regionprops(labels)

            #顯示一共貼了幾個Lables（即幾個components）
            print("[INFO] Total {} blobs".format(len(region)))
            cc_index = counter+2    
            
            if file_type == 'pancreas':
                cc_index = counter

            tmp_area = np.empty(len(region))
            for i in range(len(region)):
                tmp_area[i] = region[i].area
                print('tmp_area:',tmp_area[i])
            
            #if:目標面積小的影像，防止cc後損失太多面積，取>50的所有面積 elif:目標最大面積佔模糊化之後的面積比例超過半數以上，則取counter數的面積
            if pd.Series(tmp_area.flatten()).sort_values(ascending=False).values[0] < 400:
                tmp_index = 0
                for i in range(len(region)):
                    if pd.Series(tmp_area.flatten()).sort_values(ascending=False).values[i] > 50:
                        tmp_index += 1
                if tmp_index > cc_index:
                    cc_index = tmp_index
                print('Most biggest area < 400,so connected component numbers have:',cc_index)
            elif pd.Series(tmp_area.flatten()).sort_values(ascending=False).values[0] > cal_area/1.5 and file_type == 'effusion':
                cc_index = counter
                print('Most biggest area > 66 percentage of area,so connected component numbers have:',cc_index)
            '''
            for i in range(len(region)):
                print('test for tmp_index:',pd.Series(tmp_area.flatten()).sort_values(ascending=False).index[i])
                print('test for tmp_area:',pd.Series(tmp_area.flatten()).sort_values(ascending=False).values[i])
            '''

            #防止被偵測到的面積數量小於預設值cc_index
            if cc_index > len(region):
                cc_index = len(region)

            biggest = np.empty([cc_index])    
            for i in range(cc_index):
                biggest[i] = pd.Series(tmp_area.flatten()).sort_values(ascending=False).index[i]
                print('bigget index:',biggest[i])
                print('The area:',tmp_area[int(biggest[i])])

            def Trans_Pixel_value(img):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if img[i][j] == 1 :
                            img[i][j] = 255       
                        i += 1
                    j += 1
                    i = 0
                
                return img

            for i in range(cc_index):
                labelMask = (labels == int(biggest[i])+1).astype(np.uint8)
                labelMask = Trans_Pixel_value(labelMask)
                '''
                plt.figure('LabelMask')
                plt.title('LabelMask')
                plt.imshow(labelMask, cmap=plt.cm.gray)
                plt.axis('off')
                plt.show()
                cv2.waitKey(0)
                '''
                cc_mask += labelMask

            #顯示所抓取到的內容
            if choose_showimg == 1:
                plt.figure('Large_Blobs')
                plt.title('Large_Blobs')
                plt.imshow(cc_mask, cmap=plt.cm.gray)
                plt.axis('off')
                plt.show()

            '''
            Morphological Filtering
            '''
            #Morphological Filtering 型態過濾 (Region Growing的概念)
            from skimage.morphology import (erosion, dilation, opening, closing,  # noqa
                                            white_tophat, black_tophat)
            from skimage.morphology import skeletonize, convex_hull_image  # noqa
            from skimage.morphology import disk  # noqa
            from skimage.morphology import remove_small_objects  # noqa
            from skimage import color  # noqa

            selem = disk(4)
            selem_mid = disk(3)
            selem_small = disk(2)

            #擴張   (擴大白區，縮小黑區)
            dilated = dilation(cc_mask, selem_mid)  
            #cv2.imshow('o_d', dilated)

            #閉闔   (擴張後腐蝕)
            closed = closing(dilated, selem)   
            #cv2.imshow('o_d_c', closed)
            closed_int = closed.astype(int)
            fixed = np.array(closed)

            #形態處理後的檢查與修補
            checkpoint = 0
            count_fixed = 0
            checkmin = 0
            checktimes = 0
            check_multifix = 0

            while checkpoint == 0:
                checktimes += 1
                print('times:',checktimes)
                #連通區域標記   (區塊分群)
                labels = measure.label(closed_int,connectivity=2)

                tmp=color.label2rgb(labels)  #根据不同的标记显示不同的颜色
                print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记) (+1推測是為了記錄最大的黑色面積)

                for region in measure.regionprops(labels): #循环得到每一个连通区域属性集
                    print('regions No.:',region)
                    print('regions area:',region.area)

                '''
                plt.figure(tmp_check)
                plt.imshow(tmp,interpolation='nearest')
                plt.axis('off')
                plt.show()
                '''
                #判斷影像是否還需要修補
                props = measure.regionprops(labels)
                #for loop 跑 range 只會跑到 range 的最大範圍-1，一到最大範圍就跳出迴圈
                if len(props) > counter:
                    print('Have detected broken pieces')
                    fixed = closing(fixed, selem)
                    closed_int = fixed.astype(int)
                    count_fixed += 1
                    if count_fixed > 3:
                        check_multifix = 1
                        resMatrix = np.zeros(fixed.shape)
                        #刪除最小區域
                        if checkmin > 0 and len(props) > counter:
                            min_area = props[0].area
                            for i in range(1, len(props)):
                                min_area = min(min_area,props[i].area)
                            for i in range(0, len(props)):
                                if props[i].area > min_area:           
                                    tmp = (labels == i + 1).astype(np.uint8)
                                    resMatrix += tmp 
                        elif checkmin > 0 and len(props) < counter:
                            print('Have fixed')
                            resMatrix = np.array(fixed)
                            checkpoint = 1        
                        #刪除微小區域
                        else:
                            for i in range(0, len(props)):
                                print('area:', props[i].area)
                                if props[i].area > 250:           
                                    tmp = (labels == i + 1).astype(np.uint8)
                                    resMatrix += tmp
                        fixed = np.array(resMatrix)
                        closed_int = fixed.astype(int)
                        checkmin += 1
                elif len(props) == counter :
                    print('Have fixed')
                    checkpoint = 1
                elif len(props) < counter :
                    print('The numbers of existing are less than needed')
                    checkpoint = 1

            if check_multifix == 1:
                fixed = fixed * 255

            if choose_showimg == 1:
                plt.figure('Fixed')
                plt.title('Fixed')
                plt.imshow(fixed, cmap=plt.cm.gray)
                plt.axis('off')
                plt.show()

            #canny edge detection
            Par_blurred = cv2.GaussianBlur(fixed, (5, 5), 0)
            #cv2.imshow('Blurred', Par_blurred)
            Par_blurred = np.uint8(Par_blurred)
            Par_canny = cv2.Canny(Par_blurred,1,5)  #(1,5)因為做形態處理時，像素值被改成1 or 0，因此梯度變化很小
            if choose_showimg == 1:
                cv2.imshow('Par_Result', Par_canny)

            #將canny結果疊合到醫師畫記的圖像上
            def overlap(img1,img2,_type):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if img2[i][j] > 1:
                            if _type == 1:
                                img1[i][j] = (255,255,0)
                            elif _type == 0:
                                if img1[i][j] > -500:
                                    img1[i][j] = (-1000)
                                else:
                                    img1[i][j] = (255)
                        i += 1
                    j += 1
                    i = 0
                return img1

            def overlap_rate(img1,img2):
                i = 0
                j = 0
                count1 = 0
                count2 = 0

                while j < 512:
                    while i < 512:
                        if img1[i][j] > 0 and img2[i][j] > 0:
                            count1 += 1
                        if img1[i][j] > 0 or img2[i][j] > 0:
                            count2 += 1
                        i += 1
                    j += 1
                    i = 0
                rate = count1 / count2
                
                return rate

            def Dice(img1,img2):
                i = 0
                j = 0
                count1 = 0
                count2 = 0
                Intersection = 0

                while j < 512:
                    while i < 512:
                        if img1[i][j] > 0:
                            count1 += 1
                        if img2[i][j] > 0:
                            count2 += 1
                        if img1[i][j] > 0 and img2[i][j] > 0:
                            Intersection += 1
                        i += 1
                    j += 1
                    i = 0

                molecular = 2*Intersection 
                Denominator = count1 + count2
                rate = molecular/Denominator
                
                return rate
            
            def RVD(img1,img2):
                i = 0
                j = 0
                count1 = 0
                count2 = 0
                Intersection = 0

                while j < 512:
                    while i < 512:
                        if img1[i][j] > 0:
                            count1 += 1
                        if img2[i][j] > 0:
                            count2 += 1
                        i += 1
                    j += 1
                    i = 0

                molecular = count2 - count1
                if count1 == 0:
                    rate = 1
                else:
                    rate = molecular/count1

                return rate

            if check_manual == 1:
                Copy_Ori_JPG = np.array(Origin_JPG)
                overlap_img = overlap(Copy_Ori_JPG,Par_canny,1)
                if choose_showimg == 1:
                    cv2.imshow('overlap',overlap_img)
                '''
                plt.figure('Overlap')
                plt.title('Overlap')
                plt.imshow(overlap_img)
                plt.axis('off')
                plt.show()
                '''
                
                Dice_Rate = Dice(fixed,Tran_Mamual_Img)
                print('DICE_rate:',Dice_Rate)

                Overlap_Rate = overlap_rate(fixed,Tran_Mamual_Img)
                Voe_rate = 1 - Overlap_Rate
                print('VOE_rate:',Voe_rate)

                Rvd_Rate = RVD(Tran_Mamual_Img,fixed)
                print('RVD_rate:',Rvd_Rate)

                avg_dice_rate += Dice_Rate
                avg_voe_rate += Voe_rate
                avg_rvd_rate += Rvd_Rate

                tmp_dice_rate = avg_dice_rate/case_counter
                tmp_voe_rate = avg_voe_rate/case_counter
                tmp_rvd_rate = avg_rvd_rate/case_counter

                if check_write == 1:
                
                    op_slice.write('\n---此張切片的結果---\n')
                    op_slice.write('DICE: '+ str(round(Dice_Rate * 100,2)) + '%\n')
                    op_slice.write('VOE: '+ str(round(Voe_rate * 100,2)) + '%\n')
                    op_slice.write('RVD: '+ str(round(Rvd_Rate * 100,2)) + '%\n')
                    
                    op_slice.write('\n---累積的結果---\n')
                    op_slice.write('Avg_DICE: '+ str(round(tmp_dice_rate * 100,2)) + '%\n')
                    op_slice.write('Avg_VOE: '+ str(round(tmp_voe_rate * 100,2)) + '%\n')
                    op_slice.write('Avg_RVD: '+ str(round(tmp_rvd_rate * 100,2)) + '%\n')

                    op_slice.close()
                    op_csv.writerow([case_dcm.replace(".dcm", ""), Dice_Rate, Voe_rate, Rvd_Rate])

            #儲存成dcm  
            def svae_dcm(img,ds,_type,intercept,slope):
                i = 0
                j = 0
                if _type == 'effusion':
                    while j < 512:
                        while i < 512:
                            if img[i][j] > 0:
                                ds.pixel_array[i][j] = (1200-intercept)/slope
                            else:
                                ds.pixel_array[i][j] = (-1020-intercept)/slope
                            i += 1
                        j += 1
                        i = 0
                elif _type == 'pancreas':
                    while j < 512:
                        while i < 512:
                            if img[i][j] > 0:
                                ds.pixel_array[i][j] = (-124-intercept)/slope
                            i += 1
                        j += 1
                        i = 0

                return ds

            ds_save = svae_dcm(fixed,ds,file_type,rescale_intercept,rescale_slope)
            ds_save.PixelData = ds_save.pixel_array.tobytes()

            #save the image 
            if file_type == 'effusion':
                fixed_tra = (fixed/255) * 850
            elif file_type == 'pancreas':
                fixed_tra = (fixed/255) * 950

            if check_save == 1:
                if file_type == 'effusion':
                    #存成疊合用dcm
                    ds_save.save_as(file_path + 'path' + '\\1_' + file_type + '_dcm' +'\\'+ case_dcm)
                elif file_type == 'pancreas':
                    ds_save.save_as(file_path + 'path' + '\\2_' + file_type + '_dcm' +'\\'+ case_dcm)
                #目標區塊
                cv2.imwrite(file_path + file_type + '\\' + file_type + '_obj' +'\\'+ case_dcm.replace(".dcm", ".jpg"), fixed_tra)
                #路徑規劃
                cv2.imwrite(file_path + file_type + '\\' + file_type + '_edg' +'\\'+ case_dcm.replace(".dcm", ".jpg"), Par_canny)
                #結果比對
                cv2.imwrite(file_path + file_type + '\\' + file_type + '_ove' +'\\'+ case_dcm.replace(".dcm", ".jpg"), overlap_img)

            if choose_showimg == 1: 
                cv2.waitKey(0)

    if check_xml_null == 0:
        #平均重疊率
        avg_dice_rate = avg_dice_rate / case_quantity
        print('Avg DICE_rate:' + str(avg_dice_rate))
        avg_voe_rate = avg_voe_rate / case_quantity
        print('Avg VOE_rate:' + str(avg_voe_rate))
        avg_rvd_rate = avg_rvd_rate / case_quantity
        print('Avg RVD_rate:' + str(avg_rvd_rate))

    if check_write == 1:
        DICE_score = round(avg_dice_rate * 100, 2)
        VOE_score = round(avg_voe_rate * 100, 2)
        RVD_score = round(avg_rvd_rate * 100, 2)

        op_f.write('\n---DICE---\n')
        op_f.write('Avg_DICE: '+ str(DICE_score) + '%\n')
        op_f.write('\n---VOE---\n')
        op_f.write('Avg_VOE: '+ str(VOE_score) + '%\n')
        op_f.write('\n---RVD---\n')
        op_f.write('Avg_RVD: '+ str(RVD_score) + '%\n')
        op_csv.writerow(['Avg', avg_dice_rate, avg_voe_rate, avg_rvd_rate])
        op_f.close()

        Output_seg_txt = file_path + file_type + '\\' + file_type + '_seg' +'\\'+ 'Output_chart.txt'
        op_seg = open(Output_seg_txt, 'w')
        op_seg.write('DICE:' + str(DICE_score) + '%\n')
        op_seg.write('VOE:' + str(VOE_score) + '%\n')
        op_seg.write('RVD:' + str(RVD_score) + '%\n')
        op_seg.close()

        fig = plt.figure()
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

        left = np.array([1, 2, 3])
        height1 = np.array([DICE_score, VOE_score, RVD_score])  
        height2 = np.array([100-DICE_score, 0, 0])        
        height3 = np.array([0, 100-VOE_score, 100-RVD_score])     

        labels = ['DICE', 'VOE', 'RVD']

        if check_xml_null == 0:
            #選擇要在下面的棒狀圖 blue
            bar1 = plt.bar(left, height1, color='blue', tick_label=labels , width=0.25)

            #選擇要在上面的棒狀圖 red
            bar2 = plt.bar(left, height2, bottom=height1, color='red', tick_label=labels , width=0.25)

            bar3 = plt.bar(left, height3, bottom=height1, color='green', tick_label=labels , width=0.25)
            plt.legend((bar1[0], bar2[0], bar3[0]), ('執行結果', '與最佳情況的差距','與最差情況的差距'))
        else:
            bar = plt.bar(left, height1, tick_label=labels , width=0.25)
        
        if file_type == 'effusion': 
            plt.title('積液分割結果')
        elif file_type == 'pancreas':
            plt.title('胰腺分割結果')
        plt.text(1.2, DICE_score, str(DICE_score) + '%')
        plt.text(2.2, VOE_score, str(VOE_score) + '%')
        plt.text(3.2, RVD_score, str(abs(RVD_score)) + '%')
        plt.ylabel('比例(%)')
        plt.xlabel('分割指標')

        plt.xlim(xmax=np.ceil(4))
        plt.ylim(ymax=np.ceil(130))
        
        #plt.show()
        #儲存 save
        fig.savefig(file_path + file_type + '\\' + file_type + '_seg' +'\\'+ 'segementation_chart.png')