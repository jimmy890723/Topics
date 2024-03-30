'''
pancreas的平均值為43956
'''
def CTSI_def(file_case_num):
    from pydicom import dcmread
    from pydicom.data import get_testdata_files

    from os import listdir, getcwd , mkdir
    from os.path import isfile, isdir, join

    import numpy as np
    import cv2
    from PIL import Image
    from PIL.ExifTags import TAGS
    import matplotlib.pyplot as plt

    from skimage import measure,color

    #正常胰腺的平均體積數值
    pancreas_normal = 43956

    #txt註記 
    check_write = 1

    Nowpath = getcwd() + '\\'
    #file_case_num = input('輸入要處理的case number\n')
    file_path =  Nowpath + "..\\..\\Data\\" + file_case_num + "\\"
    
    file_list = listdir(file_path)
    check_file = 0
    for f in file_list:
        if f == 'CTSI':
            check_file = 1
            break
    if check_file == 0:
        mkdir(file_path + 'CTSI')

    file_dic_class = file_path + file_case_num
    file_eff_class = file_path + "effusion\\effusion_obj"
    file_pan_class = file_path + "pancreas\\pancreas_obj"
    fileExt = ".jpg"
    file_dic_path = file_dic_class + '\\'
    file_eff_path = file_eff_class + '\\'
    file_pan_path = file_pan_class + '\\'
    # 取得所有檔案與子目錄名稱
    files_all = listdir(file_dic_class)
    files_eff = listdir(file_eff_class) 
    files_pan = listdir(file_pan_class) 

    case_quantity = 0
    eff_case_quantity = 0
    pan_case_quantity = 0
    file_eff = []
    file_pan = []

    for f in files_all:
        if f.endswith('.dcm'):
            case_quantity += 1

    for f in files_eff:
        if f.endswith(fileExt):
            file_eff.append(f)
            eff_case_quantity += 1

    for f in files_pan:
        if f.endswith(fileExt):
            file_pan.append(f)
            pan_case_quantity += 1

    #開啟要編寫的txt檔
    if check_write == 1:
        Output_path = file_path + 'Output_CTSI.txt'
        op_f = open(Output_path, 'w')
        op_f.write('案例碼: '+ file_case_num + '\n')
        op_f.write('案例切片總數: '+ str(case_quantity) + '\n')

        Eff_count_path = file_path + 'CTSI' + '\\Effusion_count.txt' 
        op_eff = open(Eff_count_path, 'w')

    '''
    胰腺壞死程度 (pancreas的部分)
    '''
    #電腦螢幕的DPI通常為72 (由於我們的圖片沒有Tag的存取，因此無法用Exif來取DPI)
    #pixel 轉 毫米  DPI:即每英寸多少點 ， 1英吋 = 25.4mm  以DPI=72為例 1mm = 2.83 pexel ; 1 pixel = 0.35mm
    def pixel2mm_area(pixel,dpi):
        w = pixel * 25.4 / dpi
        h = 25.4 / dpi 
        resault = w * h
        return resault

    case_dcm = file_pan[0].replace('jpg','dcm')
    ds = dcmread(file_dic_path + case_dcm)

    SliceThickness = int(ds[0x0018, 0x0050].value)
    print('SliceThickness:',SliceThickness)

    PixelSpacing = ds[0x0028, 0x0030].value
    print('PixelSpacing:',PixelSpacing)

    PixelSpacing_list = []

    for i in PixelSpacing:
        PixelSpacing_list.append(i)

    def detect_pancreas(img):
        i = 0
        j = 0
        counter = 0

        while j < 512:
            while i < 512:
                if img[i][j] > 0 :
                    counter += 1
                i += 1
            j += 1
            i = 0
            
        return counter

    counter_pixel = 0

    for case_obj in file_pan:
        OBJ_Image = cv2.imread(file_pan_path + case_obj)
        OBJ_Image = cv2.cvtColor(OBJ_Image, cv2.COLOR_BGR2GRAY)
        ret, OBJ_Image = cv2.threshold(OBJ_Image, 127, 255, cv2.THRESH_BINARY)
        count_pan_pixel = detect_pancreas(OBJ_Image)
        counter_pixel += count_pan_pixel

    #用dpi算體積佔比
    pan_area = pixel2mm_area(counter_pixel,72)
    pancreas_volum = pan_area * SliceThickness
    print('Total Pancreas volum:',pancreas_volum)

    '''
    #用PixelSpacing算體積佔比
    single_pixel = PixelSpacing_list[0] * PixelSpacing_list[1]
    pancreas_volum_2 = single_pixel * count_pan_pixel * SliceThickness
    print('Total Pancreas volum2:',pancreas_volum_2)
    '''
    #胰腺壞死比例分級
    def pancreas_death_level(pancreas_death_per):
        if pancreas_death_per <= 0:
            score = 0
        elif pancreas_death_per <= 0.3 and pancreas_death_per > 0:
            score = 2
        elif pancreas_death_per <= 0.5 and pancreas_death_per > 0.3:
            score = 4
        elif pancreas_death_per > 0.5:
            score = 6

        return score

    pancreas_death_per = 1-(pancreas_volum/pancreas_normal)
    pancreas_death_score = pancreas_death_level(pancreas_death_per)

    '''
    Balthazar (effusion的部分)
    '''
    if eff_case_quantity > 0:
        #抓檔名
        file_name = file_eff[0].replace(fileExt,'')
        file_name = file_name.split('-')

        Del_str = file_name[0] + '-' + file_name[1] + '-'

        counter_eff = 0     #記總共有多少塊
        counter_Pre = 0     #記前一張圖的編號
        Previous_eff = 0    #記前一張圖有幾塊 
        Previous_img = cv2.imread(file_eff_path + file_eff[0]) #記前一張圖像的樣子

        for case_obj in file_eff:
            check_first = 0 
            case_name = case_obj.replace(Del_str,'')
            case_name = case_name.replace(fileExt,'')
            counter_num = int(case_name)
            
            print(counter_num)

            check_jump = 0

            if counter_Pre == 0:
                check_first = 1
            else:
                if counter_num - counter_Pre > 1:
                    check_jump = 1  #表示跳號了，之後做cc後直接將塊數加上
                
            counter_Pre = counter_num
            OBJ_Image = cv2.imread(file_eff_path + case_obj)
        
            #做二值化，原因是影像在儲存的過程中，邊緣的部分像素值會有些微的浮動，因此需要再做二值化修正回來
            OBJ_Image = cv2.cvtColor(OBJ_Image, cv2.COLOR_BGR2GRAY)
            ret, OBJ_Image = cv2.threshold(OBJ_Image, 127, 255, cv2.THRESH_BINARY)
            
            '''
            plt.figure('OBJ_Image')
            plt.imshow(OBJ_Image,cmap=plt.cm.gray)
            plt.axis('off')
            '''
            #單看目前的case，做cc後的成果
            labels = measure.label(OBJ_Image,connectivity=2)
            print('regions number:',labels.max())
            tmp=color.label2rgb(labels)

            '''
            plt.figure('tmp_check')
            plt.imshow(tmp,interpolation='nearest')
            plt.axis('off')
            plt.show()
            '''
            #疊圖 overlap
            def overlap(img1,img2,img):
                i = 0
                j = 0

                while j < 512:
                    while i < 512:
                        if img1[i][j] > 0 or img2[i][j] > 0 :
                            img[i][j] = 255
                        i += 1
                    j += 1
                    i = 0
                
                return img

            tmp_overlap = np.array(OBJ_Image)
            if check_jump == 0 and check_first == 1:
                counter_eff += labels.max()   
            elif check_jump == 0 and check_first == 0:
                tmp_overlap = overlap(Previous_img,OBJ_Image,tmp_overlap)

                ove_labels = measure.label(tmp_overlap,connectivity=2)
                #與上一張疊圖之後的成果
                print('overlap regions number:',ove_labels.max())
                ove_tmp=color.label2rgb(ove_labels)
                if ove_labels.max() > Previous_eff:
                    counter_eff += ove_labels.max() - Previous_eff
            elif check_jump == 1:
                counter_eff += labels.max()
                
            #更新前一張的資訊
            Previous_img = np.array(OBJ_Image)
            Previous_eff = labels.max()
            #print('Total region number:',counter_eff)
            
            op_eff.write('此張slice積液區塊數量:' + str(labels.max()) +'\n')
            op_eff.write('目前累積積液區塊數量:' + str(counter_eff) +'\n')
    else:
        counter_eff = 0
        op_eff.write('此張slice積液區塊數量:0\n')
        op_eff.write('目前累積積液區塊數量:0\n')
    op_eff.close()

    print('Total region number:',counter_eff)

    #Balthazar分級
    def Balthazar(counter,pancreas_Swelling_per):
        if counter <= 0:
            if pancreas_Swelling_per <= 0:
                score = 0
            elif pancreas_Swelling_per <= 0.5 and pancreas_Swelling_per > 0:
                score = 1
            elif pancreas_Swelling_per > 0.5:
                score = 2
        elif counter > 0 and counter < 2:
            score = 3
        elif counter > 1:
            score = 4
        
        return score

    pancreas_Swelling_per = (pancreas_volum/pancreas_normal) - 1
    Balthazar_score = Balthazar(counter_eff,pancreas_Swelling_per)

    #Balthazar寫檔
    if check_write == 1:
        op_f.write('\n---Balthazar評分---\n')
        op_f.write('積液區塊總數: '+ str(counter_eff) + '\n')
        if counter_eff == 0:
            op_f.write('胰腺膨脹比例: '+ str(round(pancreas_Swelling_per,2)) + '\n')
        op_f.write('Balthazar 分數: '+ str(Balthazar_score) + '\n')

    #胰腺壞死評分寫檔
    if check_write == 1:
        op_f.write('\n---胰腺壞死評分---\n')
        op_f.write('胰腺體積: '+ str(round(pancreas_volum)) + '\n')
        op_f.write('胰腺壞死比例: '+ str(round(pancreas_death_per)) + '\n')
        op_f.write('胰腺壞死 分數: '+ str(pancreas_death_score) + '\n')

    #CTSI
    CTSI_score = pancreas_death_score + Balthazar_score

    if check_write == 1:
        op_f.write('\n---CTSI評分---\n')
        op_f.write('CTSI 分數: '+ str(CTSI_score) + '\n')
        op_f.close()

        Output_CTSI_txt = file_path + 'CTSI' + '\\'+ 'Output_chart.txt'
        Output_CTSI = open(Output_CTSI_txt, 'w')
        
        Output_CTSI.write('Balthazar:' + str(Balthazar_score) + '\n')
        Output_CTSI.write('胰腺壞死評分:' + str(pancreas_death_score) + '\n')
        Output_CTSI.write('CTSI:' + str(CTSI_score) + '\n')
        Output_CTSI.close()
        
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        fig = plt.figure()
        left = np.array([1, 2, 3])
        height1 = np.array([Balthazar_score, 0, Balthazar_score])  
        height2 = np.array([0, pancreas_death_score, pancreas_death_score])        

        labels = ['Balthazar', '胰腺壞死評分', 'CTSI']

        #選擇要在下面的棒狀圖 blue
        bar1 = plt.bar(left, height1, color='blue', tick_label=labels , width=0.25)
        bar2 = plt.bar(left, height2, color='red', tick_label=labels , width=0.25)
        #選擇要在上面的棒狀圖 red
        bar3 = plt.bar(left, height1, bottom=height2, color='blue', tick_label=labels , width=0.25)

        plt.title('CTSI結果')
        plt.legend((bar1[0], bar2[0]), ('Balthazar分數', '胰腺壞死評分'),loc=2)
        plt.text(1.2, Balthazar_score, Balthazar_score)
        plt.text(2.2, pancreas_death_score, pancreas_death_score)
        plt.text(3.2, CTSI_score, CTSI_score)
        plt.text(3.5, 2.5, r'輕型',c="g")
        plt.text(3.5, 4.5, r'中型',c="b")
        plt.text(3.5, 7.5, r'重型',c="y")
        plt.text(3.5, 9.5, r'危重型',c="r")

        plt.axhline(y=3, c="g", ls="--", lw=2)
        plt.axhline(y=5, c="b", ls="--", lw=2)
        plt.axhline(y=8, c="y", ls="--", lw=2)
        plt.axhline(y=10, c="r", ls="--", lw=2)

        plt.ylabel('分數')
        plt.xlabel('CTSI計算指標')
        # 設置y軸的上限
        plt.ylim(ymax=np.ceil(10))
        plt.xlim(xmax=np.ceil(4))
        #plt.show()

        fig.savefig(file_path + 'CTSI\\' + 'CTSI_chart.png')