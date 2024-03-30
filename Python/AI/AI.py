from sys import path
from pydicom import dcmread
import tensorflow as tf
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import os
import numpy as np
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import warnings
import argparse
import pydicom
import skimage.morphology as sm
from skimage.measure import label
import skimage.color
import skimage.filters
import skimage.io as io
import skimage.viewer
import skimage.measure
from collections import Counter
from skimage import filters
import shutil
import xml.etree.ElementTree as ET
import cv2 as cv
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

workspace_name = 'pancreas'
model_name = "my_model2"
label_map_name = "Pancreas.pbtxt"
case_number = ""
min_thresh = 0.5
detection_type = ""
showfig = "0"
def init_para(casenum,type):
    global detection_type
    global case_number
    case_number = casenum
    detection_type = type


def normalizationDCM(image_array, hu_max, hu_min):
    image_array = (image_array - hu_min) / (hu_max - hu_min)

    return image_array * 255

def HU2Pixel(image_array, slope, intercept):
    # Hu = pixel * slope + intercept
    image_array = (image_array + intercept)/ slope
    return image_array
    
def convert2jpg(root_dir):
    for dirname, dirnames, filenames in os.walk(root_dir):
        jpg_num=1;
        # print path to all subdirectories first.
        for subdirname in dirnames:
            if subdirname[len(subdirname)-4:len(subdirname)] != '_jpg':  #沒jpg_
                demofilepath = os.path.join(dirname, subdirname) + "\\" \
                      + os.path.splitext(subdirname)[0] + "demofile.txt"#以subdirname為分隔+demofile.txt 可選擇分隔次數
                if  os.path.exists(demofilepath):
                    os.remove(demofilepath)
                print("delete log file: ", demofilepath)
                # print("dir: ", os.path.join(dirname, subdirname))
        
        # print path to all filenames.
        for filename in filenames:
            if os.path.splitext(filename)[-1] == ".dcm":#以filename分隔[-1]為檔案類型
            
                # print("file: ", os.path.join(dirname, filename))
                # print("path: ", dirname)               
                #print("file: ", os.path.splitext(dirname)[0])
                #print("file: ", os.path.splitext(filename)[-1])
                log_file_name = os.path.splitext(dirname)[0]#root到dirname ex./CtnData_1/tensorflow/workspace/pancreas/testmodel/1004655448
                #print("file: ", os.path.split(log_file_name)[1])#casenumber ex.1004655448
                log_file_name = os.path.split(log_file_name)[1] +"demofile.txt"#剩餘字元+demofile ex.1004655448demofile.txt
                log_file_name = os.path.join(dirname, log_file_name)#/CtnData_1/tensorflow/workspace/pancreas/testmodel/1004655448/1004655448demofile.txt
                #print("log_file_name: ", log_file_name)重複做多次一樣的結果可以考慮拿到loop外
                ds = pydicom.read_file(os.path.join(dirname, filename))#/CtnData_1/tensorflow/workspace/pancreas/testmodel/1004655448/IMG-0004-00001.dcm
                # print(ds)
                # print(ds[0x0028, 0x0103]])#(0028, 0103) Pixel Representation                US: 0
                # print(ds[0x0028, 0x1052])
                # print(ds[0x0028, 0x1053])
                
                rescale_intercept = int(ds[0x0028, 0x1052].value)   #截距Rescale Intercept                   DS: "-1024.0"
                rescale_slope = int(ds[0x0028, 0x1053].value)       #斜率Rescale Slope                       DS: "1.0"
    
                # (0008, 103e) Series Description  LO: 'Abdomen-A  6.0  B31f'#腹部
                # (0018, 0015) Body Part Examined  CS: 'ABDOMEN'
                # (0018, 0050) Slice Thickness     DS: "6.0"
 
                series_description = ds[0x0008, 0x103e].value
                #檢查描述和說明
                body_part = ds[0x0018, 0x0015].value
                #身體部位
                slice_thickness = int(ds[0x0018, 0x0050].value)
                #層厚
                #\t=tab
                dicom_log = os.path.join(dirname, filename) + "\t" \
                            + str(series_description) + "\t"  \
                            + str(body_part) + "\t" + \
                            str(slice_thickness) + "\t"
                
                if "Abdomen-A" in series_description and \
                   "ABDOMEN" in body_part and \
                   slice_thickness >= 6:
                    
                    dicom_log = dicom_log + "1\n"
                    
                    pmax = int(ds[0x0028, 0x0107].value)
                    #Largest Image Pixel Value           US: 4095後面沒用到
                    pmin = int(ds[0x0028, 0x0106].value)
                    #Smallest Image Pixel Value          US: 0

                    image_array = ds.pixel_array
                    hu_img = HU2Pixel(image_array, rescale_slope, rescale_intercept)
                    
                    WL = 70
                    WW = 250
                    WMin = (((WW/2) * -1) + WL)
                    WMax = (((WW/2) * 1) + WL)
                    CutOff = WW/ 2
                    hu_img[ hu_img <= WMin] = WMin
                    hu_img[ (hu_img >= WMax) & (hu_img < CutOff)] = WMin
                    hu_img[ hu_img >= CutOff] = WMax
    
                    result = normalizationDCM(hu_img, WMax, WMin).astype(np.uint8)
                    
                    #dicom
                    #path = dirname + "_dicom"
                    #if not os.path.isdir(path):
                    #    os.mkdir(path)
                
                    #shutil.copyfile(os.path.join(dirname, filename), path + "//" + filename )
                    
                    #pancreas
                    path = dirname #+ "_pancreas_jpg"
                    if not os.path.isdir(path):
                        os.mkdir(path)
                    
                    im = Image.fromarray(result)
                    im = im.convert("RGB")
                    im.save(path + "//" + os.path.splitext(filename)[0] + ".jpg")
                    
                    #effusion
                    #path = dirname + "_effusion_jpg"
                    #if not os.path.isdir(path):
                    #    os.mkdir(path)
                    
                    #im = Image.fromarray(result)
                    #im = im.convert("RGB")                 
                    #im.save(path + "//" + os.path.splitext(filename)[0] + ".jpg")
                else:
                    dicom_log = dicom_log + "0\n"
                f = open(log_file_name, "a")
                f.write(dicom_log)
                f.close()

#Load dicom to jpg
#def dicom2jpg(directory):
#    array = []
#    for dirpath,_,filenames in os.walk(directory):
#        for f in filenames:
#            if f[len(f)-4:len(f)] == '.dcm':
#                array.append(os.path.abspath(os.path.join(dirpath, f)))
#                fpath = os.path.abspath(os.path.join(dirpath, f))
#                ds = dcmread(fpath)
#                plt.imsave(fpath.replace("dcm", "jpg"), ds.pixel_array, cmap=plt.cm.gray)
         
#Loading the image
def testImgsFilePaths(directory):
    array = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            if f[len(f)-4:len(f)] == '.jpg':
                array.append(os.path.abspath(os.path.join(dirpath, f)))
      
    return array

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
    path: the file path to the image

    Returns:
    uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))


def pred3(image_arr, boxes, scores, HU_min, HU_max, open_radius, close_radius, gaus, f_name, f_dir, ai_label, img_of_box,arrs):
    img = np.asarray(image_arr)#轉化為矩陣
    mask = np.zeros((img.shape[0], img.shape[1]))#mask設置成img.shape[0]橫長 img.shape[1]縱寬的0矩陣
    #max_boxes_to_draw = 20
    i=0
    count = 0
         
    for i in range(boxes.shape[0]):#boundingbox數次
        if scores is None or scores[i] > min_thresh:#沒有scores或大於minthresh
            count = count + 1
            xmin = int(boxes[i][1]*512)
            xmax = int(boxes[i][3]*512)
            ymin = int(boxes[i][0]*512)
            ymax = int(boxes[i][2]*512)
            
            print("xmin = (" + str(boxes[i][1]) + ", " + str(xmin) +")" , 
                "xmax = (" + str(boxes[i][3]) + ", " + str(xmax) +")" ,
                "ymin = (" + str(boxes[i][0]) + ", " + str(ymin) +")" ,
                "ymax = (" + str(boxes[i][2]) + ", " + str(ymax) +")", end ='\n')
                
            print("topScore = " + str(scores[0]) , end ='\n')
            #arrs.append([xmin,xmax,ymin,ymax,scores[0]])
            img_num = f_name.split('.')[0]
            img_of_box.append([img_num,count]) 
            iou_f_name = f_name.split('.')[0]+".xml"
            ai_label_name = f_dir + "_" + iou_f_name
            ai_label.append(ai_label_name)
            
            find_coordinate(iou_f_name, i, xmin, xmax, ymin, ymax,arrs, scores[0])
            #############胰腺HU value 範圍
            tempmask = np.zeros(img.shape)#tempmask設為0矩陣
            tempmask[ymin:ymax, xmin:xmax] = 255#框出範圍設為255
            
            # if showfig == "1":
                # plt.figure()
                # plt.title("tempmask detection box")
                # plt.imshow(tempmask)
                # plt.show()
            
            tempmask[(img > HU_min) & (tempmask == 255)] = 255
            tempmask[(img <= HU_max) & (tempmask == 255)] = 0

            mask_label_region = label(tempmask, connectivity=1)#四面連接
            # convert the label image to color image
            colored_label_image = skimage.color.label2rgb(mask_label_region, bg_label=0)
            
            # if showfig == "1":
                # plt.figure()
                # plt.subplot(211)
                # plt.title("tempmask filter by HU & label")
                # plt.imshow(tempmask)
                
                # plt.subplot(212)
                # plt.imshow(colored_label_image)
                # plt.show()
            

            label_region_opening = sm.opening(mask_label_region, sm.disk(open_radius))#開運算:先腐蝕再膨脹消除小斑塊
            label_region_opening[label_region_opening != 0] = 255
            mask_label_region_opening = label(label_region_opening, connectivity=1)
            colored_label_region_opening = skimage.color.label2rgb(mask_label_region_opening, bg_label=0)
            
            # if showfig == "1":
                # plt.figure()
                # plt.title("mask_label_region_opening")
                # plt.imshow(colored_label_region_opening)
                # plt.show()
            
            # 指定區域的dicom圖 出现频率最高的單詞(10個) ex:'abracadabra' [('a', 5), ('b', 2), ('r', 2)]
            counts = Counter(mask_label_region_opening[ymin:ymax, xmin:xmax].flat)
            top_one = counts.most_common(10)
            biggest=0
            for most in top_one:
                
                if np.unique(label_region_opening[mask_label_region_opening == most[0]]) == 255:#unique除去重複組成新的array
                    biggest = most[0]
                    break
                
            #print("出現最高的區域編號 : ", biggest)
            mask[mask_label_region_opening == biggest] = 255
    
    #############閉運算#############高斯平滑
    mask_finished = filters.gaussian(sm.closing(mask, sm.disk(close_radius)), gaus)
    mask_finished[mask_finished >= 128] = 255
    mask_finished[mask_finished < 128] = 0
    return mask_finished
def find_coordinate(iou_f_name, i, xmin, xmax, ymin, ymax, arrs, topscore):
    if detection_type == "pancreas":
        xmlpath = '../../Data/doctor_p_xml/'+case_number+'/'+case_number+'_'+iou_f_name
    elif detection_type == "effusion":
        xmlpath = '../../Data/doctor_e_xml/'+case_number+'/'+case_number+'_'+iou_f_name
    if os.path.exists(xmlpath):
        #使用try exception防止找不到xml error
        #檔案載入並解析xml資料
        #print("/CtnData_1/tensorflow/workspace/pancreas/xml/"+case_number+"_"+iou_f_name)#/CtnData_1/tensorflow/workspace/pancreas/images/test/1006420946_IMG-0006-00016.xml
        tree = ET.parse(xmlpath)
        # 從字串中取得並解析xml資料
        root = tree.getroot()
        #f = open('boxes.txt', 'a')#輸出框座標
        #box = [f_name, "\n",
            #    str(xmin), " ", str(xmax), " ",
            #str(ymin), " ", str(ymax), "\n"]
        #f.writelines(box)
        #f.close()
        counter = 0
        for count in root.iter('object'):
            counter = counter + 1

        nparray = np.zeros((counter, 4), dtype=int)

        counter_2 = 0
        # 在第一層子節點中尋找object節點
        for finder in root.findall('object'):
            # 在第二層子節點中尋找bndboxt節點
            for finder_2 in finder.findall('bndbox'):
                xml_x_min = finder_2.find('xmin').text
                xml_x_max = finder_2.find('xmax').text
                xml_y_min = finder_2.find('ymin').text
                xml_y_max = finder_2.find('ymax').text
                nparray[counter_2] = [xml_x_min, xml_x_max, xml_y_min, xml_y_max]
                counter_2 = counter_2 + 1
        rect1 = nparray[0]
        rect2 = (xmin, xmax, ymin, ymax)
        iou = round(compute_iou(rect1, rect2),3)
        arrs.append([xmin,xmax,ymin,ymax,iou])
        print(iou)
        #mergeimg(f_name, nparray[i])
    else:
        arrs.append([xmin,xmax,ymin,ymax,0])
        print(xmlpath)
        print("No label")

def compute_iou(rec1, rec2):
    """
    computing IoU
    :param rec1: (y0, x0, y1, x1), which reflects
            (top, left, bottom, right)
    :param rec2: (y0, x0, y1, x1)
    :return: scala value of IoU
    """
    # computing area of each rectangles
    S_rec1 = (rec1[3] - rec1[2]) * (rec1[1] - rec1[0])
    S_rec2 = (rec2[3] - rec2[2]) * (rec2[1] - rec2[0])
    # computing the sum_area
    sum_area = S_rec1 + S_rec2

    # find the each edge of intersect rectangle
    left_line = max(rec1[0], rec2[0])
    right_line = min(rec1[1], rec2[1])
    top_line = min(rec1[3], rec2[3])
    bottom_line = max(rec1[2], rec2[2])

    # judge if there is an intersect

    intersect = (right_line - left_line) * (top_line - bottom_line)
    if (intersect / (sum_area - intersect))*1.0 < 0:
        return 0
    else:
        return (intersect / (sum_area - intersect))*1.0
def image_inference(gauge_count, gauge):
    ai_label = []
    f_name = ''
    PATH_TO_SAVED_MODEL='../../Data/'+detection_type+"_model/saved_model"
    print('Loading model...', end='')
    # Load saved model and build the detection function
    detect_fn=tf.saved_model.load(PATH_TO_SAVED_MODEL)
    print('Done!')
    #Loading the label_map
    print('Loading label_map...', end='')
    if detection_type =="pancreas":
        label_map_name = "Pancreas.pbtxt"
    elif detection_type =="effusion":
        label_map_name = "Effusion.pbtxt"
    PATH_TO_LABEL_MAP='../../Data/annotation/'+ label_map_name
    print(PATH_TO_LABEL_MAP)
    category_index=label_map_util.create_category_index_from_labelmap(PATH_TO_LABEL_MAP,use_display_name=True)
    print('Done!')
    PATH_TO_TEST_FILE='../../Data/'+ case_number + "/" + case_number

    IMGS_FOR_TEST = testImgsFilePaths(PATH_TO_TEST_FILE)
    print(*IMGS_FOR_TEST, sep = "\n")
    num_ai_detection = 0
    count_all_images = 0
    img_of_box = []
    arrs = []
    for IMG_PATH in IMGS_FOR_TEST:
        print(IMG_PATH)
        end =  int(IMG_PATH.split('-00')[2].split('.')[0])
    print("{end_word}:{end_num}".format(end_word = "end",end_num=end))
    for IMG_PATH in IMGS_FOR_TEST:
        ######################################
        gauge_count = gauge_count + 1 
        gauge.SetValue(int((gauge_count/end)*20))
        ######################################
        count_all_images = count_all_images +1
        f_name = os.path.split(IMG_PATH)[1]
        f_dir = os.path.split(os.path.split(IMG_PATH)[0])[1]
        print(int(f_name.split('-')[2].split('.')[0])/end*100)
        if int(f_name.split('-')[2].split('.')[0])/end*100>15 and int(f_name.split('-')[2].split('.')[0])/end*100<48:
            print('Running inference for {}... '.format( f_dir + "/" + f_name), end='\n')
            print(1)
            image_np=load_image_into_numpy_array(IMG_PATH)
            print(2)
            # Things to try:
            # Flip horizontally
            # image_np = np.fliplr(image_np).copy()
            # Convert image to grayscale
            # image_np = np.tile(
            #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

            # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
            input_tensor=tf.convert_to_tensor(image_np)
            # The model expects a batch of images, so add an axis with `tf.newaxis`.
            input_tensor=input_tensor[tf.newaxis, ...]

            # input_tensor = np.expand_dims(image_np, 0)
            detections=detect_fn(input_tensor)

            # All outputs are batches tensors.
            # Convert to numpy arrays, and take index [0] to remove the batch dimension.
            # We're only interested in the first num_detections.
            num_detections=int(detections.pop('num_detections'))
            detections={key:value[0,:num_detections].numpy()
                            for key,value in detections.items()}
            detections['num_detections'] = num_detections

            # detection_classes should be ints.
            detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

            image_np_with_detections=image_np.copy()
            if detection_type == "pancreas":
                viz_utils.visualize_boxes_and_labels_on_image_array(
                    image_np_with_detections,
                    detections['detection_boxes'],
                    detections['detection_classes'],
                    detections['detection_scores'],
                    category_index,
                    use_normalized_coordinates=True,
                    max_boxes_to_draw=2,     #max number of bounding boxes in the image
                    min_score_thresh=min_thresh,     #min prediction threshold
                    agnostic_mode=False)
            elif detection_type == "effusion":
                viz_utils.visualize_boxes_and_labels_on_image_array(
                    image_np_with_detections,
                    detections['detection_boxes'],
                    detections['detection_classes'],
                    detections['detection_scores'],
                    category_index,
                    use_normalized_coordinates=True,
                    max_boxes_to_draw=4,     #max number of bounding boxes in the image
                    min_score_thresh=min_thresh,     #min prediction threshold
                    agnostic_mode=False)
            # #matplotlib inline

            if showfig == "1":
                matplotlib.use('TkAgg')  # Or any other X11 back-end
                plt.figure()
                plt.imshow(image_np_with_detections)           
                plt.show()
        
            #if not os.path.exists(PATH_TO_TEST_FILE.replace("testmodel", "testmodeldir")):
            #    os.makedirs(PATH_TO_TEST_FILE.replace("testmodel", "testmodeldir"))
        
            #io.imsave(IMG_PATH.replace("testmodel", "testmodeldir"), image_np_with_detections)
        
            # boxes = np.squeeze(detections['detection_boxes'])
            # scores = np.squeeze(detections['detection_scores'])
            
            # upper_threshold_boxes = boxes[scores > min_thresh]
            # if len(upper_threshold_boxes) != 0:
                # print("detection information")
                # print(upper_threshold_boxes)
                
            #image open/close and gaus
            #if not os.path.exists(PATH_TO_TEST_FILE.replace("testmodel", "testmodelmask")):
            #    os.makedirs(PATH_TO_TEST_FILE.replace("testmodel", "testmodelmask"))
            
            ds = dcmread(IMG_PATH.replace(".jpg", ".dcm"))
            mask = pred3(ds.pixel_array, detections['detection_boxes'], detections['detection_scores'], 1024, 1064, 1, 5, 3, f_name, f_dir, ai_label
            ,img_of_box,arrs)
            
            #io.imsave(IMG_PATH.replace("testmodel", "testmodelmask"), mask.astype(np.uint8))
            for i in range(detections['detection_boxes'].shape[0]):#ai標記總數(框框數)
                if detections['detection_scores'] is None or detections['detection_scores'][i] > min_thresh:
                    num_ai_detection = num_ai_detection+1
            
            if showfig == "1":
                plt.figure()
                plt.imshow(mask)
                plt.show()
    print(f_name)
    print(1)
    end_number = int(f_name.split('-')[2].split('.')[0])
    print(end_number)
    F1score(num_ai_detection, ai_label, img_of_box, count_all_images,arrs,end_number)
    
def F1score(num_ai_detection, ai_label, img_of_box, count_all_images,arrs,end_number):
    if detection_type == "pancreas":
        xmlpath = '../../Data/doctor_p_xml/'+case_number    #獲取當前路徑
    elif detection_type == "effusion":
        xmlpath = '../../Data/doctor_e_xml/'+case_number    #獲取當前路徑
    num_files = 0 #路徑下檔案數量(包括資料夾)
    print("doctor label : ")
    if os.path.exists(xmlpath):
        for fn in os.listdir(xmlpath):
            if fn != '@eaDir' and fn.split('.')[1] == 'xml':
                num_files += 1
                print(fn)
    print(num_files)
    j = 0
    print("ai label : ")
    tmp = 0
    print(ai_label)
    number_tmp = num_ai_detection
    while j<num_ai_detection:#ai標記檔名
        if(tmp == ai_label[j]):
            number_tmp = number_tmp-1
        else:
            print(ai_label[j])
        tmp = ai_label[j]
        j = j+1
    print(number_tmp)#變為ai有框張數
    print(ai_label)
    a= []
    img_num = []
    for k in range(number_tmp):
        if k == 0:
            a.append(img_of_box[k][1])
        else:
            only_num_img_of_box1 =img_of_box[k-1][0].split('-00')[2].split('.')[0]#ex.001 002
            only_num_img_of_box2 =img_of_box[k][0].split('-00')[2].split('.')[0]#ex.001 002
            if int(only_num_img_of_box1)+3>int(only_num_img_of_box2):
                a.append(a[k-1]+1)
            else:
                a.append(img_of_box[k][1])
        img_num.append(img_of_box[k][0])
    tmp = 0
    tmp2 = 0
    first_check = 0
    for i in range(len(a)):
        if tmp < a[i]:
            tmp = a[i]
            tmp2 = i
    print(tmp)#最大連續數
    print(a)#一個一個數上去
    print(img_num)#連續圖片編號
    if detection_type == "pancreas":
        dr_xmlpath = '../../Data/doctor_p_xml/'+case_number+'/'
    elif detection_type == "effusion":
        dr_xmlpath = '../../Data/doctor_e_xml/'+case_number+'/'
    if os.path.exists(dr_xmlpath):
        if len(ai_label) != 0:
            only_num_img_of_box =img_num[tmp2-tmp+1].split('-00')[2].split('.')[0]
            first_check = int(only_num_img_of_box)
            print(first_check)#從哪開始(第幾張圖)
            img_of_boxs = []
            count = 0
            tmp = ''
            for i in range(len(img_of_box)):
                if(tmp == img_of_box[i][0]):
                    img_of_boxs[count-1][1]=img_of_box[i][1]
                else:
                    img_of_boxs.append(img_of_box[i])
                    count = count + 1
                tmp = img_of_box[i][0]
            print(img_of_boxs)#['IMG-0008-00009', 2]
            print(arrs)#[303, 467, 186, 263, 0.99999964]
            
            second_check = []
            tmp = 0
            count_for_fn = 0
            for i in range(number_tmp):
                print('i : {i_num}'.format(i_num=i))
                only_num_img_of_boxs =img_of_boxs[i][0].split('-00')[2].split('.')[0]#ex.001 002
                print("{}----------------".format(only_num_img_of_boxs))
                if int(only_num_img_of_boxs) >= first_check and int(only_num_img_of_boxs) < first_check+max(a):
                    if detection_type == "pancreas":
                        print("status:1")
                        #if int(only_num_img_of_boxs)*100/end_number>27 and int(only_num_img_of_boxs)*100/end_number<36:
                        #    print("status:2")
                        #    if img_of_boxs[i][1] ==1:
                        #        print("status:3")
                        #        second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                        #    elif  img_of_boxs[i][1] ==2:
                        #        print("status:4")
                        #        second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                        #        second_check.append([img_of_boxs[i][0],arrs[tmp+1][0],arrs[tmp+1][1],arrs[tmp+1][2],arrs[tmp+1][3],arrs[tmp+1][4]])
                        #        count_for_fn = count_for_fn +1
                        #else:
                        #    print("status:5")
                        if img_of_boxs[i][1] ==1:
                            print("status:6")
                            second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                        elif int(only_num_img_of_boxs) == first_check and img_of_boxs[i][1] ==2:
                            print("status:7")
                            second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                        elif img_of_boxs[i][1] ==2 and i>=1:
                            print("status:8")
                            first_check = first_check + 1
                            tmpposition1 = []
                            #last_only_num_img_of_boxs = int(img_of_boxs[i-1][0].split('-00')[2].split('.')[0])
                            #if last_only_num_img_of_boxs*100/end_number>27 and last_only_num_img_of_boxs*100/end_number<36:
                            #    print("status:9")
                            #    tmpx = ((second_check[len(second_check)-1][1]+second_check[len(second_check)-1][2])/2+(second_check[len(second_check)-2][1]+second_check[len(second_check)-2][2])/2)/2-7
                            #    tmpy = ((second_check[len(second_check)-1][3]+second_check[len(second_check)-1][4])/2+(second_check[len(second_check)-2][3]+second_check[len(second_check)-2][4])/2)/2
                            #    tmpposition1 += (tmpx,tmpy)
                            #    second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                            #    second_check.append([img_of_boxs[i][0],arrs[tmp+1][0],arrs[tmp+1][1],arrs[tmp+1][2],arrs[tmp+1][3],arrs[tmp+1][4]])
                            #else:
                            #    print("status:10")
                            tmpx = (second_check[len(second_check)-1][1]+second_check[len(second_check)-1][2])/2-7
                            tmpy = (second_check[len(second_check)-1][3]+second_check[len(second_check)-1][4])/2
                            tmpposition1 += (tmpx,tmpy)
                            #print(only_num_img_of_boxs)
                            #print(second_check[len(second_check)-1][1])
                            #print(second_check[len(second_check)-1][2])
                            #print(tmpposition1)
                            if (abs((arrs[tmp][0]+arrs[tmp][1])/2-tmpposition1[0])+abs((arrs[tmp][2]+arrs[tmp][3])/2-tmpposition1[1]))<=(abs((arrs[tmp+1][0]+arrs[tmp+1][1])/2-tmpposition1[0])+abs((arrs[tmp+1][2]+arrs[tmp+1][3])/2-tmpposition1[1])):
                                second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                            else:
                                second_check.append([img_of_boxs[i][0],arrs[tmp+1][0],arrs[tmp+1][1],arrs[tmp+1][2],arrs[tmp+1][3],arrs[tmp+1][4]])
                    elif detection_type == "effusion":
                        if img_of_boxs[i][1] >0:
                            second_check.append([img_of_boxs[i][0],arrs[tmp][0],arrs[tmp][1],arrs[tmp][2],arrs[tmp][3],arrs[tmp][4]])
                        if img_of_boxs[i][1] >1:
                            second_check.append([img_of_boxs[i][0],arrs[tmp+1][0],arrs[tmp+1][1],arrs[tmp+1][2],arrs[tmp+1][3],arrs[tmp+1][4]])
                        if img_of_boxs[i][1] >2:
                            second_check.append([img_of_boxs[i][0],arrs[tmp+2][0],arrs[tmp+2][1],arrs[tmp+2][2],arrs[tmp+2][3],arrs[tmp+2][4]])
                        if img_of_boxs[i][1] >3:
                            second_check.append([img_of_boxs[i][0],arrs[tmp+3][0],arrs[tmp+3][1],arrs[tmp+3][2],arrs[tmp+3][3],arrs[tmp+3][4]])
                tmp = tmp + img_of_boxs[i][1]
            print(second_check)
            #print(tmpposition1)
        
        
            True_positive=0
            True_negative=0
            for fn in os.listdir(xmlpath):#計算TP
                m = 0
                for label in second_check:
                    if fn != '@eaDir' and fn.split('.')[1] =='xml' and fn.split('-00')[2].split('.')[0] == label[0].split('-00')[2] and label[5]>0.5:
                        #print(fn.split('-00')[2].split('.')[0])
                        True_positive = True_positive+1
                        if(tmp == label[0]):
                            True_positive = True_positive - 1
                        tmp = label[0]
                    m =m+1
            False_positive = number_tmp-True_positive
            False_negative = num_files-True_positive
            True_negative = count_all_images - True_positive - False_positive - False_negative
            print("Before")
            print("True_positive:")
            print(True_positive)#應標有標
            print("False_positive:")
            print(False_positive)#ai標錯
            print("False_negative:")
            print(False_negative)#ai沒標到
            print("True_negative:")
            print(True_negative)#不應標沒標
            Precision = (True_positive)/(True_positive + False_positive)
            Recall = (True_positive)/(True_positive + False_negative)
            if True_positive == 0:
                F1_score=0
            else:
                F1_score = (Precision * Recall)/((Precision + Recall)/2)
            print("F1_score:")
            print(F1_score)


            limit_score = 0.5
            if detection_type =="effusion":
                limit_score=0
            True_positive=0
            True_negative=0
            for fn in os.listdir(xmlpath):#計算TP
                m = 0
                for label in second_check:
                    if fn != '@eaDir' and fn.split('.')[1] =='xml' and fn.split('-00')[2].split('.')[0] == label[0].split('-00')[2] and label[5]>limit_score:
                        #print(fn.split('-00')[2].split('.')[0])
                        True_positive = True_positive+1
                        if(tmp == label[0]):
                            True_positive = True_positive - 1
                        tmp = label[0]
                    m =m+1
            False_positive = len(second_check)-True_positive-count_for_fn
            False_negative = num_files-True_positive
            True_negative = count_all_images - True_positive - False_positive - False_negative
            print("After")
            print("True_positive:")
            print(True_positive)#應標有標
            print("False_positive:")
            print(False_positive)#ai標錯
            print("False_negative:")
            print(False_negative)#ai沒標到
            print("True_negative:")
            print(True_negative)#不應標沒標
            Precision = (True_positive)/(True_positive + False_positive)
            Recall = (True_positive)/(True_positive + False_negative)
            if True_positive == 0:
                F1_score=0
            else:
                F1_score = (Precision * Recall)/((Precision + Recall)/2)
            
            print("Precision:")
            print(Precision)
            print("Recall:")
            print(Recall)
            print("F1_score:")
            print(F1_score)

            root_path =  '../../Data/' + case_number 
            read_file = os.listdir( root_path )
            check_file = 0
            for fn in read_file:
                if fn == 'F1Score':
                    check_file = 1
                    break
            if check_file == 0:
                os.mkdir(root_path + '/F1Score')
            ######寫檔給結果讀取
            F1 = "F1 Score:"+str(round(F1_score,2)*100)+"%"
            path = root_path + '/F1Score/f1out_' + detection_type +'.txt'
            f = open(path, 'w')
            f.write(F1)
            f.close()

            F1_path = '..\\..\\Data\\' + case_number + '\\F1Score\\'
            ######結果圖表
            plt.figure()
            plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
            left = np.array([1])
            plt.ylim(ymax=np.ceil(115))
            plt.xlim(xmax=np.ceil(2))
            height1 = np.array([F1_score*100])
            F1_score_2 = 1-F1_score
            height2 = np.array([F1_score_2*100])

            labels = [case_number]
            bar1 = plt.bar(left, height1, color='blue', yerr=0, tick_label=labels,width=0.35)

            bar2 = plt.bar(left, height2, bottom=height1, yerr=0, color='red', tick_label=labels,width=0.35)
            plt.title('F1 Score')
            plt.legend((bar1[0], bar2[0]), ('F1_score', '誤差值'))
            plt.text(1.2, F1_score*100, str(round(F1_score,2)*100) + "%")
            plt.ylabel('分數')
            plt.xlabel('案例編號')
            plt.savefig(F1_path + 'F1_Score_' + detection_type +'.jpg')

            
            #xmlshow()
            enhence_show(second_check)
            #GenerateXml(second_check)
            creat_xml(second_check)
        else:
            print("NO TARGET OBJECT")
    else:
        print("DOCTOR NO LABEL")
    
    
def caculate_effusion_spot(directory):

    IMGS_FOR_CAL = testImgsFilePaths(directory)
   
    effusion_count = 0
    
    for IMG_PATH in IMGS_FOR_CAL:
        image_np=load_image_into_numpy_array(IMG_PATH)
        #effusion_count = effusion_count + label(image_np, connectivity=2)
        print(Counter(label(image_np, connectivity=2).flat))
    
    print("effusion_spot:", effusion_count, end='\n')
    
    if effusion_count > 1:
        print("CTSI Score: more than 1 effusion, 4")       
    elif effusion_count == 1:
        print("CTSI Score: 1 effusion, 3")
        
    else:
        print("CTSI Score: no effusions, 0-2")
        
    # '''
    # 判斷有幾處積液，
    # '''
    # bad = label(APeffusion3Dgaus_arr, connectivity=2)
    # print("積液處數量", len(np.unique(bad)))

    # if len(np.unique(bad)) > 1:
        # print("CTSI評分判斷：積液處多於1處，得分4分")
        # bad_percentage = APalive_percentage(APalive3Dgaus_arr)
        # print(bad_percentage)
    # elif len(np.unique(bad)) == 1:
        # print("CTSI評分判斷：積液處等於1處，得分3分")
        # bad_percentage = APalive_percentage(APalive3Dgaus_arr)
        # print(bad_percentage)
    # else:
        # print("CTSI評分判斷：沒有積液處，得分0~2分")
   
def pancreas_percentage(directory):
    print('caculate pancreas_percentage ... ', end='\n')
    
    # #AP_arr = np.asarray(AP_arr)
    # print(alive_arr.shape)
    # print(type(alive_arr))
    # alive_arr_nonzero = np.count_nonzero(alive_arr)
    # print(alive_arr_nonzero)
    # print(type(alive_arr_nonzero))
    # print("===== 胰腺存活、壞死百分比 =====")
    # alive = alive_arr_nonzero / 30669 * 100
    # bad = 100-alive
    # print("胰腺存活像素個數\t" + str(alive_arr_nonzero) + "\n基準胰腺像素個數\t30669")
    # print("胰腺存活百分比\t" + str(round(alive, 2)) + "%")
    # print("胰腺壞死百分比\t" + str(round(bad, 2)) + "%")
    # return round(bad, 2)
'''
def mergeimg(f_name, nparray):
    PATH_TO_JPG='../../Data/'+ case_number + "/" + detection_type +'/testmodeldir/' + case_number + "/" + f_name
    img = cv.imread(PATH_TO_JPG)
    cv.rectangle(img,(nparray[0],nparray[2]),(nparray[1],nparray[3]),(255,0,0),thickness=2)
    cv.imwrite('D:/gui/bounding_box/' + case_number + "/" + f_name, img)
'''
def enhence_show(second_check):
    PATH_TO_JPG='../../Data/'+ case_number + "/" + case_number
    XMLS_FOR_TEST = testImgsFilePaths(PATH_TO_JPG)
    for XML_PATH in XMLS_FOR_TEST:
        f_name = os.path.split(XML_PATH)[1]#IMG-0002-00025.jpg
        JPG='../../Data/'+ case_number + "/" + case_number + "/" + f_name
        only_number = f_name.split('-00')[2].split('.')[0]
        img = cv.imread(JPG)
        for second_check_1 in second_check:
            if second_check_1[0].split("-00")[2] == only_number:
                cv.rectangle(img,(second_check_1[1],second_check_1[3]),(second_check_1[2],second_check_1[4]),(0,0,255),thickness=2)
        if detection_type == "pancreas":
            PATH = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_bnd/'
        elif detection_type == "effusion":
            PATH = '../../Data/'+ case_number + "/" + detection_type +'/effusion_bnd/'
        if not os.path.exists(PATH):
                os.makedirs(PATH)
        cv.imwrite(PATH + f_name, img)
def xmlshow():
    if detection_type == "pancreas":
        PATH_TO_JPG='../../Data/doctor_p_xml/' + case_number
    elif detection_type == "effusion":
        PATH_TO_JPG='../../Data/doctor_e_xml/' + case_number
    XMLS_FOR_TEST = testImgsFilePaths(PATH_TO_JPG)
    for XML_PATH in XMLS_FOR_TEST:
        f_name = os.path.split(XML_PATH)[1]
        img_num = f_name.split('_')[1]
        iou_f_name = os.path.split(XML_PATH)[1].split('.')[0]+".xml"
        if detection_type == "pancreas":
            tree = ET.parse('../../Data/doctor_p_xml/'+case_number+"/"+iou_f_name)
        elif detection_type == "effusion":
            tree = ET.parse('../../Data/doctor_e_xml/'+case_number+"/"+iou_f_name)
        # 從字串中取得並解析xml資料
        root = tree.getroot()
        counter = 0
        for count in root.iter('object'):
            counter = counter + 1

        nparray = np.zeros((counter, 4), dtype=int)

        counter_2 = 0
        # 在第一層子節點中尋找object節點
        for finder in root.findall('object'):
            # 在第二層子節點中尋找bndboxt節點
            for finder_2 in finder.findall('bndbox'):
                xml_x_min = finder_2.find('xmin').text
                xml_x_max = finder_2.find('xmax').text
                xml_y_min = finder_2.find('ymin').text
                xml_y_max = finder_2.find('ymax').text
                nparray[counter_2] = [xml_x_min, xml_x_max, xml_y_min, xml_y_max]
                counter_2 = counter_2 + 1
        img = cv.imread(XML_PATH)
        cv.rectangle(img,(nparray[0][0],nparray[0][2]),(nparray[0][1],nparray[0][3]),(255,0,0),thickness=2)
        cv.imwrite('D:/gui/bounding_box/' + case_number + "/" + img_num, img)
def creat_xml(second_check):
    """
    新建xml文件
    :param xml_file: second_check bounding box 4座標
    """
    for i in range(len(second_check)):
        if i == 0 or second_check[i][0] != second_check[i-1][0]:
            print(second_check[i][0])
            root = ET.Element("annotation")
            child1 = ET.SubElement(root, "casenumber")
            child1.text = case_number
            object = ET.SubElement(root, "object")
            namen = ET.SubElement(object, "name")
            namen.text = 'pancreas'
            bndbox = ET.SubElement(object, "bndbox")
            xminn = ET.SubElement(bndbox, "xmin")
            xminn.text = str(second_check[i][1])
            yminn = ET.SubElement(bndbox, "ymin")
            yminn.text = str(second_check[i][3])
            xmaxn = ET.SubElement(bndbox, "xmax")
            xmaxn.text = str(second_check[i][2])
            ymaxn = ET.SubElement(bndbox, "ymax")
            ymaxn.text = str(second_check[i][4])
            tree = ET.ElementTree(root)
            if detection_type == "pancreas":
                path = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml'
                path_origin = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml_origin'
                writepath = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[i][0] +'.xml'
                writepath_origin = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml_origin/' + second_check[i][0] +'.xml'
            if detection_type == "effusion":
                path = '../../Data/'+ case_number + "/" + detection_type +'/effusion_xml'
                path_origin = '../../Data/'+ case_number + "/" + detection_type +'/effusion_xml_origin'
                writepath = '../../Data/'+ case_number + "/" + detection_type +'/effusion_xml/' + second_check[i][0] +'.xml'
                writepath_origin = '../../Data/'+ case_number + "/" + detection_type +'/effusion_xml_origin/' + second_check[i][0] +'.xml'
            if not os.path.exists(path):
                os.makedirs(path)
            if not os.path.exists(path_origin):
                os.makedirs(path_origin)
            tree.write(writepath,  encoding='utf-8')
            tree.write(writepath_origin,  encoding='utf-8')
        else:
            print(second_check[i][0])
            edit_xml(second_check[i])

def edit_xml(second_check):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    #print(second_check[0])
    #print('../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[0] +'.xml')
    if detection_type == "pancreas":
        treepath = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[0] +'.xml'
    elif detection_type == "effusion":
        treepath = '../../Data/'+ case_number + "/" + detection_type +'/effusion_xml/' + second_check[0] +'.xml'
    tree = ET.parse(treepath)
    root = tree.getroot()
    objs = ET.Element("object")
    root.append(objs)
    bndbox = ET.SubElement(objs, "bndbox")
    #print('error1')
    xminn = ET.SubElement(bndbox, "xmin")
    xminn.text = str(second_check[1])
    #print('error2')
    yminn = ET.SubElement(bndbox, "ymin")
    yminn.text = str(second_check[3])
    #print('error3')
    xmaxn = ET.SubElement(bndbox, "xmax")
    xmaxn.text = str(second_check[2])
    #print('error4')
    ymaxn = ET.SubElement(bndbox, "ymax")
    ymaxn.text = str(second_check[4])
    #print('error5')    
    tree.write(treepath,method='xml',encoding='utf-8')       # 更新xml文件
'''def GenerateXml(second_check):
    import xml.dom.minidom
    
    impl = xml.dom.minidom.getDOMImplementation()
    for i in range(len(second_check)):
        path = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[i][0] +'.xml'
        if second_check[i][0] != second_check[i-1][0]:
            print(second_check[i][0])
            annotation = impl.createDocument(None, 'annotation', None)
            root = annotation.documentElement
            casenumber = annotation.createElement('casenumber')
            root.appendChild(casenumber)
            casenumbertxt = annotation.createTextNode(case_number)
            casenumber.appendChild(casenumbertxt)
        print(second_check[i][0])
        dom = xml.dom.minidom.parse(second_check[i][0] +'.xml')
        root = dom.documentelement
        object_num = root.createElement('object')
        root.appendChild(object_num)

        name = root.createElement('name')
        nametxt = root.createTextNode(detection_type)
        name.appendChild(nametxt)
        object_num.appendChild(name)
        bndbox = root.createElement('bndbox')
        object_num.appendChild(bndbox)
        xmin = root.createElement('xmin')
        ymin = root.createElement('ymin')
        xmax = root.createElement('xmax')
        ymax = root.createElement('ymax')
        xmintxt = root.createTextNode(str(second_check[i][1]))
        ymintxt = root.createTextNode(str(second_check[i][3]))
        xmaxtxt = root.createTextNode(str(second_check[i][2]))
        ymaxtxt = root.createTextNode(str(second_check[i][4]))
        bndbox.appendChild(xmin)
        bndbox.appendChild(ymin)
        bndbox.appendChild(xmax)
        bndbox.appendChild(ymax)
        xmin.appendChild(xmintxt)
        ymin.appendChild(ymintxt)
        xmax.appendChild(xmaxtxt)
        ymax.appendChild(ymaxtxt)
        f= open('../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[i][0] +'.xml', 'w', encoding='utf-8')
        annotation.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
        f.close()'''
    
#if __name__ == "__main__":
    
     
#    PATH_TO_DICOM_FILE='D:/gui/testmodel/' + case_number
#    print(PATH_TO_DICOM_FILE)
#    convert2jpg(PATH_TO_DICOM_FILE)
    
#    image_inference()
    
    
#    PATH_TO_MASK_FILE='D:/gui/testmodelmask/' + case_number
#    if detection_type == "effusion":
#        caculate_effusion_spot(PATH_TO_MASK_FILE)
    
#    if detection_type == "pancreas":
#        pancreas_percentage(PATH_TO_MASK_FILE)
    
#    print('Inference Done... ', end='\n')
    
    

