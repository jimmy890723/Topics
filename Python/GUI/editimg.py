import cv2
import numpy as np
import xml.etree.ElementTree as ET
import os
drawing = False # true if mouse is pressed
ix,iy = -1,-1#最小
x_, y_ = 0,0#最大
# mouse callback function
min_tmp = []
max_tmp = []
anchor = []

def edit_main(num,case_number,detection_type,count):
    def draw_shape(event,x,y,flags,param):
        print(event)
        global ix,iy,drawing,mode,x_,y_, r

        if event == cv2.EVENT_LBUTTONDOWN:
            print('inside mouse lbutton event....')
            drawing = True
            ix,iy = x,y
            global min_tmp
            min_tmp.append([ix,iy])
            x_,y_ = x,y
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            copy = img.copy()
            x_,y_ = x,y
            cv2.rectangle(copy,(ix,iy),(x_,y_),(0,255,0),1)
            cv2.imshow("image", copy)
        #
        elif event == cv2.EVENT_LBUTTONUP:
            print('inside mouse button up event')
            drawing = False
            global max_tmp
            max_tmp.append([x_,y_])
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
    
    global x_,y_,ix,iy
    img_num = "../../Data/" + case_number + "/" + detection_type + "/" + detection_type +"_bnd/" + str(num[count])
    img = cv2.imread(img_num)
    temp_img = np.copy(img)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_shape)
    while(1):
        global min_tmp,max_tmp,anchor
        # print('inside while loop...')
        cv2.imshow('image',img)
        if not cv2.EVENT_MOUSEMOVE:
            copy = img.copy()
            # print('x_: , y_ : '.format(x_,y_))
            print(x_)
            cv2.rectangle(copy,(ix,iy),(x_,y_),(0,255,0),1)
            cv2.imshow('image',copy)
            
        k = cv2.waitKey(1) & 0xFF
        if k == ord('x'): #resets the image (removes rectangles)
            img = np.copy(temp_img)
            x_,y_ = -10,-10
            ix,iy = -10,-10
            min_tmp = []
            max_tmp = []
            anchor = []
        elif k == 27:
            img = np.copy(temp_img)
            x_,y_ = -10,-10
            ix,iy = -10,-10
            print(min_tmp)
            print(max_tmp)
            for i in range(len(min_tmp)):
                anchor.append([min_tmp[i][0],min_tmp[i][1],max_tmp[i][0],max_tmp[i][1]])
            print(anchor)
            if len(anchor)>0:
                creat_xml(anchor,num[count],case_number,detection_type)
                enhence_show(anchor,num[count],case_number,detection_type)
                min_tmp = []
                max_tmp = []
                anchor = []
            break
    cv2.destroyAllWindows()
def creat_xml(anchor,num,case_number,detection_type):
    """
    新建xml文件
    :param xml_file: second_check bounding box 4座標
    """
    root = ET.Element("annotation")
    child1 = ET.SubElement(root, "casenumber")
    child1.text = case_number
    object = ET.SubElement(root, "object")
    namen = ET.SubElement(object, "name")
    namen.text = 'pancreas'
    bndbox = ET.SubElement(object, "bndbox")
    xminn = ET.SubElement(bndbox, "xmin")
    xminn.text = str(anchor[0][0])
    yminn = ET.SubElement(bndbox, "ymin")
    yminn.text = str(anchor[0][1])
    xmaxn = ET.SubElement(bndbox, "xmax")
    xmaxn.text = str(anchor[0][2])
    ymaxn = ET.SubElement(bndbox, "ymax")
    ymaxn.text = str(anchor[0][3])
    tree = ET.ElementTree(root)
    path = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml'
    img_name = str(num).split(".")[0]
    writepath = '../../Data/'+ case_number + '/' + detection_type +'/' + detection_type + '_xml/' + img_name +'.xml'
    if detection_type == "effusion":
        path.replace("pancreas_xml","effusion_xml")
        writepath.replace("pancreas_xml","effusion_xml")
    if not os.path.exists(path):
        os.makedirs(path)
    
    tree.write(writepath,  encoding='utf-8')
    if len(anchor) >1:
        for i in range(len(anchor)-1,0,-1):
            edit_xml(anchor[len(anchor)-i],img_name,case_number,detection_type)
            print('???')

def edit_xml(anchor,img_name,case_number,detection_type):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    #print(second_check[0])
    #print('../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[0] +'.xml')
    treepath = '../../Data/'+ case_number + '/' + detection_type +'/' + detection_type + '_xml/' + img_name +'.xml'
    if detection_type == "effusion":
        treepath.replace("pancreas_xml","effusion_xml")
    tree = ET.parse(treepath)
    root = tree.getroot()
    objs = ET.Element("object")
    root.append(objs)
    bndbox = ET.SubElement(objs, "bndbox")
    #print('error1')
    xminn = ET.SubElement(bndbox, "xmin")
    xminn.text = str(anchor[0])
    #print('error2')
    yminn = ET.SubElement(bndbox, "ymin")
    yminn.text = str(anchor[1])
    #print('error3')
    xmaxn = ET.SubElement(bndbox, "xmax")
    xmaxn.text = str(anchor[2])
    #print('error4')
    ymaxn = ET.SubElement(bndbox, "ymax")
    ymaxn.text = str(anchor[3])
    #print('error5')    
    tree.write(treepath,method='xml',encoding='utf-8')
def enhence_show(anchors,img_name,case_number,detection_type):
    ai_JPG='../../Data/'+ case_number + "/" + detection_type +'/' + detection_type + '_bnd/' + img_name
    init_JPG='../../Data/'+ case_number + "/" + case_number +'/' + img_name
    img = cv2.imread(init_JPG)
    fix_JPG = '../../Data/'+ case_number + "/" + detection_type +'/' + detection_type + '_fix/' + img_name
    if not os.path.exists(fix_JPG):
        fix_JPG = '../../Data/'+ case_number + "/" + detection_type +'/testmodel/' + case_number + '/' + img_name
    for anchor in anchors:
        cv2.rectangle(img,(anchor[0],anchor[1]),(anchor[2],anchor[3]),(0,255,0),thickness=2)
    PATH = '../../Data/'+ case_number + "/" + detection_type +'/' + detection_type + '_bnd/'
    path_fix = '../../Data/'+ case_number + "/" + detection_type +'/' + detection_type + '_fix/'
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    if not os.path.exists(path_fix):
        os.makedirs(path_fix)
    cv2.imwrite(PATH + img_name, img)
    cv2.imwrite(path_fix + img_name, img)