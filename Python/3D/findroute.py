# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:05:44 2019

@author: hutton
"""
from os import listdir
import matplotlib.pyplot as plt
import math
from pydicom import dcmread
from statistics import stdev 

#dicName='D:\\dicom\\Lung_segmentation_visualization-master\\Segmentation_and_Visualization\\Data\\2018_3_7____08_37_35'
dicName = input("Enter path containing scans: ")

def takeSecond(elem):
    return elem[1]
def showDicom(myFileName):
    ds=dcmread(dicName+"_2\\"+myFileName)
    ds2=dcmread(dicName+"_3\\pancreas_"+myFileName)
    intercept=ds[0x0028,0x1052].value
    scale=ds[0x0028,0x1053].value
    
    ds.PixelData=ds.pixel_array.tostring()
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.axis('off')
    plt.savefig('1/foo0.png', bbox_inches='tight', pad_inches=0)
    for i in range(len(ds2.pixel_array.flat)):
        ds2.pixel_array.flat[i]=(-1024-intercept)/scale
    for i in range(len(ds.pixel_array.flat)):
        houseField=ds.pixel_array.flat[i]*scale+intercept
        if houseField<40:
            ds.pixel_array.flat[i]=4000
        else:
            ds.pixel_array.flat[i]=0
    
    startx=221
    starty=512-343
    lineWidth=3
    sortList=[]      
    currenty=starty
    currentx=startx
    print(currentx,currenty)
    for degree in range(0,360,3):
        arrayList=[]
        lineLength=1
        addX=0
        addY=0
        blackCount=0
        whiteCount=0
        
        while True:
            addX=math.floor(currentx+lineLength*math.cos(math.radians(degree)))
            addY=math.floor(currenty+lineLength*math.sin(math.radians(degree)))
            lineLength=lineLength+2
            if addX<512 and addX>=0 and addY<400 and addY>=0:
                widthIntercept=math.floor(lineWidth/2)
                for widthX in range(-1*widthIntercept,widthIntercept+1):
                    for widthY in range(-1*widthIntercept,widthIntercept+1):
                        if addY+widthY>=0 and addY+widthY<512 and addX+widthX>=0 and addX+widthX<512 and [addY+widthY,addX+widthX] not in arrayList:
                            arrayList.append([addY+widthY,addX+widthX])
            else:
                break
        currentCount=0
        blackArray=[]
        for eachArray in arrayList:
            currentCount=currentCount+1
            if ds.pixel_array[eachArray[0]][eachArray[1]]==0:
                blackCount=blackCount+1
                blackArray.append(currentCount)
            elif ds.pixel_array[eachArray[0]][eachArray[1]]==4000:
                whiteCount=whiteCount+1
        if whiteCount+blackCount>0:
            if (blackCount*100)/(whiteCount+blackCount)<10:
                if blackCount>40:
                    deviation=stdev(blackArray)
                else:
                    deviation=999
                if deviation>400:
                    sortList.append([degree,(blackCount*100)/(whiteCount+blackCount),arrayList])
                            
    sortList.sort(key=takeSecond)
    print(sortList)  
    if len(sortList)>3:  
        for i in range(3):    
            for eachArray in sortList[i][2]:
                ds.pixel_array[eachArray[0]][eachArray[1]]=(-250-intercept)/scale
                ds2.pixel_array[eachArray[0]][eachArray[1]]=(-250-intercept)/scale                            
            
            

        
    ds.PixelData=ds.pixel_array.tostring()
    ds2.PixelData=ds2.pixel_array.tostring()
    ds2.save_as('1/pancreas_'+myFileName)
    plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
    
    plt.axis('off')
    plt.savefig('1/foo.png', bbox_inches='tight', pad_inches=0)
    plt.show()
def saveDicom(myFileName):
    ds=dcmread(dicName+"\\"+myFileName)
    intercept=ds[0x0028,0x1052].value
    scale=ds[0x0028,0x1053].value
    
    ds.PixelData=ds.pixel_array.tostring()
    
    for i in range(len(ds.pixel_array.flat)):
        ds.pixel_array.flat[i]=(-1024-intercept)/scale
   
    ds.PixelData=ds.pixel_array.tostring()
    ds.save_as('1/'+myFileName)

    print("檔案：", myFileName)

    
'''files = listdir(dicName)
for f in files:
    saveDicom(f)'''
showDicom('IMG-0006-00021.dcm') 
