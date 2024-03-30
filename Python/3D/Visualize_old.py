import vtk
from vtk.util import numpy_support
import numpy as np
import globals

DEBUG_MODE = 1
PRINT_PATH = 0
PRINT_MPR3D = 0
clickPointsList = []


class Visualize():
    def __init__(self):
        self.__ren = vtk.vtkRenderer()
        self.__colorFunc = vtk.vtkColorTransferFunction()
        self.__alphaChannelFunc = vtk.vtkPiecewiseFunction()
        self.__pathVolume = vtk.vtkVolume()
        self.__bodyVolume = vtk.vtkVolume()
        self.__fluidVolume = vtk.vtkVolume()
    '''
    設定render位置
    '''

    def viz_SetViewport(self, xmin, xmax, ymin, ymax):
        self.__ren.SetViewport(xmin, xmax, ymin, ymax)
    '''
    設定render名稱
    '''

    def viz_SetViewportName(self, name, x, y, fontsize=24, color=[0, 0, 0], bgcolor=[1, 1, 0]):
        text = vtk.vtkTextActor()
        text.SetInput(name)
        text.SetPosition(x, y)
        text.GetTextProperty().SetFontSize(fontsize)
        text.GetTextProperty().SetColor(color[0], color[1], color[2])
        text.GetTextProperty().FrameOn()
        text.GetTextProperty().SetFrameColor(color[0], color[1], color[2])
        text.GetTextProperty().SetBackgroundColor(
            bgcolor[0], bgcolor[1], bgcolor[2])
        text.GetTextProperty().SetBackgroundOpacity(1)
        self.__ren.AddActor2D(text)
    '''
    設定render燈光
    '''

    def viz_SetLighting(self, r, g, b):
        light = vtk.vtkLight()
        light.SetColor(r, g, b)
        self.__ren.AddLight(light)
    '''
    設定render背景
    '''

    def viz_SetBackground(self, r, g, b):
        self.__ren.SetBackground(r, g, b)

    '''
    以下三個為讀取Data後要做處理才會用到，接著並建模，暫時沒用到
    '''

    def viz_SetDataUsingPath(self, path):
        data = np.load(path)
        self.viz_SetData(data)

    def viz_SetData(self, data):
        self.__dataImporter = vtk.vtkImageImport()
        data_string = data.tostring()
        x, y, z = data.shape
        self.__dataImporter.CopyImportVoidPointer(
            data_string, len(data_string))
        self.__dataImporter.SetDataScalarTypeToUnsignedChar()
        self.__dataImporter.SetNumberOfScalarComponents(1)
        self.__dataImporter.SetDataExtent(0, z - 1, 0, y - 1, 0, x - 1)
        self.__dataImporter.SetWholeExtent(0, z - 1, 0, y - 1, 0, x - 1)

    def viz_visualize(self):
        volume = vtk.vtkVolume()
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(self.__colorFunc)
        volumeProperty.SetScalarOpacity(self.__alphaChannelFunc)
        volumeProperty.ShadeOn()
        volumeProperty.SetInterpolationTypeToLinear()
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(self.__dataImporter.GetOutputPort())
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        self.__ren.AddVolume(volume)

    '''
    建出完整的scan，option=1則建出胰腺
    '''

    def viz_VisualizeDICOM(self, path, option=0):

        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        dc_color_func = vtk.vtkColorTransferFunction()
        dc_color_func.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        dc_color_func.AddRGBPoint(-124, 0.62, 0.05, 0.05)
        # dc_color_func.AddRGBPoint(-124, 0.92, 1.00, 0.01)  # 胰臟顏色
        dc_color_func.AddRGBPoint(-77, 0.55, 0.25, 0.15)
        dc_color_func.AddRGBPoint(94, 0.88, 0.60, 0.29)
        dc_color_func.AddRGBPoint(179, 1.0, 0.94, 0.95)
        dc_color_func.AddRGBPoint(260, 0.62, 0.0, 0.0)
        # dc_color_func.AddRGBPoint(3071, 0.82, 0.66, 1.0)
        dc_color_func.AddRGBPoint(3071, 1.0, 1.0, 1.0)

        dc_color_func.AddRGBPoint(-250, 0.53, 0.53, 0.53)  # 路線

        dc_alpha_func = vtk.vtkPiecewiseFunction()  # 透明度 0~1
        dc_alpha_func.AddPoint(-251, 0.0)  # 路線
        dc_alpha_func.AddPoint(-250, 1.0)  # 路線
        dc_alpha_func.AddPoint(-249, 0.0)  # 路線
        dc_alpha_func.AddPoint(-3024, 0.0)
        dc_alpha_func.AddPoint(78, 0.0)  # 0.29
        dc_alpha_func.AddPoint(100, 0.0)  # 骨頭器官腎臟 原值為0.55
        dc_alpha_func.AddPoint(260, 0.84)  # 0.84 幾乎全身
        dc_alpha_func.AddPoint(3071, 0.875)  # 0.875
        if option == 1:
            dc_alpha_func.AddPoint(-125, 0.0)
            dc_alpha_func.AddPoint(-124, 0.8)
            dc_alpha_func.AddPoint(-123, 0)

        volumeProperty = vtk.vtkVolumeProperty()  # 光影
        volumeProperty.SetColor(dc_color_func)
        volumeProperty.SetScalarOpacity(dc_alpha_func)
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.5)
        volumeProperty.SetDiffuse(1.0)
        volumeProperty.SetSpecular(0.5)
        volumeProperty.SetSpecularPower(25)
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()  # GPU加速
        volumeMapper.SetInputConnection(dc_img_reader.GetOutputPort())
        self.__bodyVolume.SetMapper(volumeMapper)
        self.__bodyVolume.SetProperty(volumeProperty)
        self.__ren.AddVolume(self.__bodyVolume)
    '''
    建出積液的scan
    '''

    def viz_VisualizeDICOM_Segment(self, path):

        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        dc_color_func = vtk.vtkColorTransferFunction()
        dc_alpha_func = vtk.vtkPiecewiseFunction()

        dc_alpha_func.AddPoint(-3024, 0.0)
        dc_alpha_func.AddPoint(-251, 0.0)
        dc_alpha_func.AddPoint(-250, 0.8)
        dc_alpha_func.AddPoint(-249, 0)
        dc_alpha_func.AddPoint(1000, 0.0)
        dc_alpha_func.AddPoint(1200, 0.03)
        dc_alpha_func.AddPoint(1700, 0.0)
        dc_alpha_func.AddPoint(3071, 0.0)
        dc_color_func.AddRGBPoint(-250, 0.53, 0.53, 0.53)
        dc_color_func.AddRGBPoint(1199, 0.66, 0.66, 0.0)

        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(dc_color_func)
        volumeProperty.SetScalarOpacity(dc_alpha_func)

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(dc_img_reader.GetOutputPort())
        self.__fluidVolume.SetMapper(volumeMapper)
        self.__fluidVolume.SetProperty(volumeProperty)
        self.__ren.AddVolume(self.__fluidVolume)
    '''
    建出路徑的scan
    '''

    def viz_VisualizeDICOM_augment(self, path):
        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        dc_color_func = vtk.vtkColorTransferFunction()
        dc_alpha_func = vtk.vtkPiecewiseFunction()

        dc_alpha_func.AddPoint(-3024, 0.0)
        dc_alpha_func.AddPoint(1999, 0.0)  # 路線
        dc_alpha_func.AddPoint(2000, 1.0)  # 路線1
        dc_alpha_func.AddPoint(2001, 0.0)  # 路線
        dc_alpha_func.AddPoint(2002, 1.0)  # 路線2
        dc_alpha_func.AddPoint(2003, 0.0)  # 路線
        dc_alpha_func.AddPoint(2004, 1.0)  # 路線3
        dc_alpha_func.AddPoint(2005, 0.0)  # 路線

        dc_alpha_func.AddPoint(1000, 0.0)
        dc_alpha_func.AddPoint(3071, 0.0)
        dc_color_func.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        # dc_color_func.AddRGBPoint(-250, 0.53, 0.53, 0.53)
        dc_color_func.AddRGBPoint(1999, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2000, 1.0, 0.0, 0.0)  # 路線1
        dc_color_func.AddRGBPoint(2001, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2002, 0.0, 1.0, 0.0)  # 路線2
        dc_color_func.AddRGBPoint(2003, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2004, 0.0, 0.0, 1.0)  # 路線3
        dc_color_func.AddRGBPoint(2005, 0.0, 0.0, 0.0)  # 路線
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(dc_color_func)
        volumeProperty.SetScalarOpacity(dc_alpha_func)

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(dc_img_reader.GetOutputPort())
        self.__pathVolume.SetMapper(volumeMapper)
        self.__pathVolume.SetProperty(volumeProperty)
        self.__ren.AddVolume(self.__pathVolume)

    def viz_VisualizeDICOM_augment_many(self, path):
        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        dc_color_func = vtk.vtkColorTransferFunction()
        dc_alpha_func = vtk.vtkPiecewiseFunction()

        dc_alpha_func.AddPoint(2005, 0.0)  # 路線
        dc_alpha_func.AddPoint(2006, 1.0)  # 路線4
        dc_alpha_func.AddPoint(2007, 0.0)  # 路線
        dc_alpha_func.AddPoint(2008, 1.0)  # 路線5
        dc_alpha_func.AddPoint(2009, 0.0)  # 路線
        dc_alpha_func.AddPoint(2010, 1.0)  # 路線6
        dc_alpha_func.AddPoint(2011, 0.0)  # 路線

        dc_alpha_func.AddPoint(1000, 0.0)
        dc_alpha_func.AddPoint(3071, 0.0)
        dc_color_func.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        # dc_color_func.AddRGBPoint(-250, 0.53, 0.53, 0.53)
        dc_color_func.AddRGBPoint(2005, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2006, 1.0, 1.0, 1.0)  # 路線4
        dc_color_func.AddRGBPoint(2007, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2008, 1.0, 1.0, 1.0)  # 路線5
        dc_color_func.AddRGBPoint(2009, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2010, 1.0, 1.0, 1.0)  # 路線6
        dc_color_func.AddRGBPoint(2011, 0.0, 0.0, 0.0)  # 路線
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(dc_color_func)
        volumeProperty.SetScalarOpacity(dc_alpha_func)

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(dc_img_reader.GetOutputPort())
        self.__pathVolume.SetMapper(volumeMapper)
        self.__pathVolume.SetProperty(volumeProperty)
        self.__ren.AddVolume(self.__pathVolume)

    def viz_VisualizeDICOM_augment_many1(self, path):
        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        dc_color_func = vtk.vtkColorTransferFunction()
        dc_alpha_func = vtk.vtkPiecewiseFunction()

        dc_alpha_func.AddPoint(2011, 0.0)  # 路線
        dc_alpha_func.AddPoint(2012, 1.0)  # 路線7
        dc_alpha_func.AddPoint(2013, 0.0)  # 路線
        dc_alpha_func.AddPoint(2014, 1.0)  # 路線8
        dc_alpha_func.AddPoint(2015, 0.0)  # 路線
        dc_alpha_func.AddPoint(2016, 1.0)  # 路線9
        dc_alpha_func.AddPoint(2017, 0.0)  # 路線

        dc_alpha_func.AddPoint(1000, 0.0)
        dc_alpha_func.AddPoint(3071, 0.0)
        dc_color_func.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        # dc_color_func.AddRGBPoint(-250, 0.53, 0.53, 0.53)
        dc_color_func.AddRGBPoint(2011, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2012, 1.0, 1.0, 1.0)  # 路線7
        dc_color_func.AddRGBPoint(2013, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2014, 1.0, 1.0, 1.0)  # 路線8
        dc_color_func.AddRGBPoint(2015, 0.0, 0.0, 0.0)  # 路線
        dc_color_func.AddRGBPoint(2016, 1.0, 1.0, 1.0)  # 路線9
        dc_color_func.AddRGBPoint(2017, 0.0, 0.0, 0.0)  # 路線
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(dc_color_func)
        volumeProperty.SetScalarOpacity(dc_alpha_func)

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(dc_img_reader.GetOutputPort())
        self.__pathVolume.SetMapper(volumeMapper)
        self.__pathVolume.SetProperty(volumeProperty)
        self.__ren.AddVolume(self.__pathVolume)

    def viz_Badcenter(self, path, txt):
        dc_img_reader = vtk.vtkDICOMImageReader()
        dc_img_reader.SetDirectoryName(path)
        dc_img_reader.Update()
        (xMin, xMax, yMin, yMax, zMin, zMax) = dc_img_reader.GetExecutive(
        ).GetWholeExtent(dc_img_reader.GetOutputInformation(0))
        (xSpacing, ySpacing, zSpacing) = dc_img_reader.GetOutput().GetSpacing()
        (x0, y0, z0) = dc_img_reader.GetOutput().GetOrigin()

        f = open(txt)
        for line in f:
            p = line.strip('\n').split(" ")
            source = vtk.vtkSphereSource()
            source.SetRadius(5)
            source.SetCenter(
                x0+float(p[0])*xSpacing, y0+float(p[1])*ySpacing, z0+(float(p[2])-0.5)*zSpacing)
            source.SetPhiResolution(11)
            source.SetThetaResolution(21)
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(source.GetOutputPort())
            polygonActor = vtk.vtkActor()
            polygonActor.SetMapper(mapper)
            polygonActor.GetProperty().SetDiffuseColor(1, 0, 0)

            self.__ren.AddActor(polygonActor)

    def GetRenderer(self):
        return self.__ren

    def GetPath(self):
        return self.__pathVolume

    def GetFluid(self):
        return self.__fluidVolume

    def GetBody(self):
        return self.__bodyVolume


def vis(dicom_path, dicom_path2, dicom_path3, casenumber):
    global current_ren
    globals.initialize(casenumber)
    # Renderers
    viz1, viz2, viz3, viz4, viz5, viz6, viz7 = [Visualize() for i in range(7)]
    current_ren = viz2.GetRenderer()
    # Setting Viewports
    viz1.viz_SetViewport(0.0, 0.502, 0.331, 1.0)
    viz2.viz_SetViewport(0.335, 0.502, 0.664, 1.0)
    viz3.viz_SetViewport(0.668, 0.502, 1.0, 1.0)
    viz4.viz_SetViewport(0.0, 0.0, 0.248, 0.498)
    viz5.viz_SetViewport(0.252, 0.0, 0.498, 0.498)
    viz6.viz_SetViewport(0.502, 0.0, 0.748, 0.498)
    viz7.viz_SetViewport(0.752, 0.0, 1.0, 0.498)

    viz1.viz_SetViewportName('Good pancreas', 10, 30)
    viz2.viz_SetViewportName(
        'Good pancreas and Necrotic pancreas ( Fluid area )', 10, 30)
    viz2.viz_SetViewportName('Green Line : 86.8%', 10, 80)
    viz2.viz_SetViewportName('Blue Line : 87.1%', 10, 140)
    viz2.viz_SetViewportName('Red Line : 88.6%', 10, 200)
    viz3.viz_SetViewportName('Necrotic pancreas ( Fluid area )', 10, 30)
    viz4.viz_SetViewportName('coronal', 10, 30)
    viz5.viz_SetViewportName('axial', 10, 30)
    viz6.viz_SetViewportName('sagittal', 10, 30)
    viz7.viz_SetViewportName('ALL', 10, 30)

    # Setting background
    viz1.viz_SetBackground(1.0, 1.0, 1.0)
    viz2.viz_SetBackground(1.0, 1.0, 1.0)
    viz3.viz_SetBackground(1.0, 1.0, 1.0)
    viz4.viz_SetBackground(1.0, 1.0, 1.0)
    viz5.viz_SetBackground(1.0, 1.0, 1.0)
    viz6.viz_SetBackground(1.0, 1.0, 1.0)
    viz7.viz_SetBackground(1.0, 1.0, 1.0)

    # Setting Data
    viz1.viz_VisualizeDICOM(dicom_path2, 1)
    viz2.viz_VisualizeDICOM(dicom_path2, 1)
    viz2.viz_VisualizeDICOM_Segment(dicom_path)
    viz2.viz_Badcenter(dicom_path2, globals.txt)
    viz3.viz_VisualizeDICOM(dicom_path2, 0)
    viz3.viz_VisualizeDICOM_Segment(dicom_path)
    viz3.viz_Badcenter(dicom_path2, globals.txt)
    viz7.viz_Badcenter(dicom_path2, globals.txt)

    # Setting light
    viz1.viz_SetLighting(1.0, 1.0, 1.0)
    viz2.viz_SetLighting(1.0, 1.0, 1.0)
    viz3.viz_SetLighting(1.0, 1.0, 1.0)
    viz4.viz_SetLighting(1.0, 1.0, 1.0)
    viz5.viz_SetLighting(1.0, 1.0, 1.0)
    viz6.viz_SetLighting(1.0, 1.0, 1.0)
    viz7.viz_SetLighting(1.0, 1.0, 1.0)

    worldPicker = vtk.vtkWorldPointPicker()

    dc_img_reader = vtk.vtkDICOMImageReader()
    dc_img_reader.SetDirectoryName(dicom_path2)
    dc_img_reader.Update()
    '''(xMin, xMax, yMin, yMax, zMin, zMax) = dc_img_reader.GetExecutive().GetWholeExtent(dc_img_reader.GetOutputInformation(0))
    (xSpacing, ySpacing, zSpacing) = dc_img_reader.GetOutput().GetSpacing()
    (x0, y0, z0) = dc_img_reader.GetOutput().GetOrigin()
    
    center = [x0 + xSpacing * 0.5 * (xMin + xMax),
              y0 + ySpacing * 0.5 * (yMin + yMax),
              z0 + zSpacing * 0.5 * (zMin + zMax)]'''

    # Picker
    picker = vtk.vtkCellPicker()
    picker.SetTolerance(0.005)

    # PlaneWidget
    planeWidgetX = vtk.vtkImagePlaneWidget()
    planeWidgetX.DisplayTextOn()
    planeWidgetX.SetInputConnection(dc_img_reader.GetOutputPort())
    planeWidgetX.SetPlaneOrientationToXAxes()
    planeWidgetX.SetSliceIndex(256)
    planeWidgetX.SetDefaultRenderer(viz7.GetRenderer())
    planeWidgetX.SetPicker(picker)
    planeWidgetX.RestrictPlaneToVolumeOn()
    planeWidgetX.SetWindowLevel(250, 70)
    planeWidgetX.SetKeyPressActivationValue("x")
    prop1 = planeWidgetX.GetPlaneProperty()
    prop1.SetColor(1, 0, 0)
    prop1.SetLineWidth(5)
    proptext1 = planeWidgetX.GetTextProperty()
    proptext1.SetColor(0, 0, 0)
    proptext1.FrameOn()
    proptext1.SetFrameColor(0, 0, 0)
    proptext1.SetBackgroundColor(1, 1, 0)
    proptext1.SetBackgroundOpacity(1)
    proptext1.SetFontSize(20)

    planeWidgetY = vtk.vtkImagePlaneWidget()
    planeWidgetY.DisplayTextOn()
    planeWidgetY.SetInputConnection(dc_img_reader.GetOutputPort())
    planeWidgetY.SetPlaneOrientationToYAxes()
    planeWidgetY.SetDefaultRenderer(viz7.GetRenderer())
    planeWidgetY.SetSliceIndex(256)
    planeWidgetY.RestrictPlaneToVolumeOn()
    planeWidgetY.SetPicker(picker)
    planeWidgetY.SetWindowLevel(250, 70)
    planeWidgetY.SetKeyPressActivationValue("y")
    prop2 = planeWidgetY.GetPlaneProperty()
    prop2.SetColor(1, 1, 0)
    prop2.SetLineWidth(5)
    proptext1 = planeWidgetY.GetTextProperty()
    proptext1.SetColor(0, 0, 0)
    proptext1.FrameOn()
    proptext1.SetFrameColor(0, 0, 0)
    proptext1.SetBackgroundColor(1, 1, 0)
    proptext1.SetBackgroundOpacity(1)
    proptext1.SetFontSize(20)

    planeWidgetZ = vtk.vtkImagePlaneWidget()
    planeWidgetZ.DisplayTextOn()
    planeWidgetZ.SetInputConnection(dc_img_reader.GetOutputPort())
    planeWidgetZ.SetPlaneOrientationToZAxes()
    planeWidgetZ.SetDefaultRenderer(viz7.GetRenderer())
    planeWidgetZ.SetSliceIndex(40)
    planeWidgetZ.RestrictPlaneToVolumeOn()
    planeWidgetZ.SetPicker(picker)
    planeWidgetZ.SetWindowLevel(250, 70)
    planeWidgetZ.SetKeyPressActivationValue("z")
    prop2 = planeWidgetZ.GetPlaneProperty()
    prop2.SetColor(0, 0, 1)
    prop2.SetLineWidth(5)
    proptext1 = planeWidgetZ.GetTextProperty()
    proptext1.SetColor(0, 0, 0)
    proptext1.FrameOn()
    proptext1.SetFrameColor(0, 0, 0)
    proptext1.SetBackgroundColor(1, 1, 0)
    proptext1.SetBackgroundOpacity(1)
    proptext1.SetFontSize(20)

    # Extract a slice in the desired orientation
    reslice = planeWidgetX.GetReslice()
    reslice.SetOutputDimensionality(2)
    reslice.SetInterpolationModeToLinear()
    reslice2 = planeWidgetY.GetReslice()
    reslice2.SetOutputDimensionality(2)
    reslice2.SetInterpolationModeToLinear()
    reslice3 = planeWidgetZ.GetReslice()
    reslice3.SetOutputDimensionality(2)
    reslice3.SetInterpolationModeToLinear()

    colorMapX = vtk.vtkImageMapToColors()
    colorMapX.SetLookupTable(planeWidgetX.GetLookupTable())
    colorMapX.SetInputConnection(reslice.GetOutputPort())
    imageActorX = vtk.vtkImageActor()
    imageActorX.PickableOff()
    imageActorX.GetMapper().SetInputConnection(colorMapX.GetOutputPort())
    colorMapY = vtk.vtkImageMapToColors()
    colorMapY.SetLookupTable(planeWidgetY.GetLookupTable())
    colorMapY.SetInputConnection(reslice2.GetOutputPort())
    imageActorY = vtk.vtkImageActor()
    imageActorY.PickableOff()
    imageActorY.GetMapper().SetInputConnection(colorMapY.GetOutputPort())
    colorMapZ = vtk.vtkImageMapToColors()
    colorMapZ.SetLookupTable(planeWidgetZ.GetLookupTable())
    colorMapZ.SetInputConnection(reslice3.GetOutputPort())
    imageActorZ = vtk.vtkImageActor()
    imageActorZ.PickableOff()
    imageActorZ.GetMapper().SetInputConnection(colorMapZ.GetOutputPort())

    # RenderWindow
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(viz1.GetRenderer())
    renWin.AddRenderer(viz2.GetRenderer())
    renWin.AddRenderer(viz3.GetRenderer())
    renWin.AddRenderer(viz4.GetRenderer())
    renWin.AddRenderer(viz5.GetRenderer())
    renWin.AddRenderer(viz6.GetRenderer())
    renWin.AddRenderer(viz7.GetRenderer())

    # Add outlineactor
    viz4.GetRenderer().AddActor2D(imageActorX)
    viz5.GetRenderer().AddActor2D(imageActorY)
    viz6.GetRenderer().AddActor2D(imageActorZ)
    interactorStyle = vtk.vtkInteractorStyleMultiTouchCamera()
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetInteractorStyle(interactorStyle)
    interactor.SetRenderWindow(renWin)

    # Load widget interactors and enable
    planeWidgetX.SetInteractor(interactor)
    planeWidgetX.On()
    planeWidgetY.SetInteractor(interactor)
    planeWidgetY.On()
    planeWidgetZ.SetInteractor(interactor)
    planeWidgetZ.On()

    def KeyPressEvent(obj, event):
        global current_ren, PRINT_PATH, PRINT_MPR3D, clickPointsList

        keyCode = obj.GetKeyCode()

        if DEBUG_MODE:
            print("Key Pressed: ", obj.GetKeyCode())

        if keyCode in ['c', 'C']:
            viz2.GetRenderer().RemoveActor2D(polygonActor)
            renWin.Render()
            del clickPointsList[:]
        if keyCode == '1':
            del clickPointsList[:]
            current_ren = viz1.GetRenderer()
        if keyCode == '2':
            del clickPointsList[:]
            current_ren = viz2.GetRenderer()
        if keyCode == '3':
            del clickPointsList[:]
            current_ren = viz3.GetRenderer()
        if keyCode == '4':
            del clickPointsList[:]
            current_ren = viz7.GetRenderer()
        if keyCode == '5':
            if PRINT_MPR3D == 0:
                viz7.viz_VisualizeDICOM(dicom_path2, 1)
                viz7.viz_VisualizeDICOM_Segment(dicom_path)
                PRINT_MPR3D = 1
            else:
                viz7.GetRenderer().RemoveVolume(viz7.GetBody())
                viz7.GetRenderer().RemoveVolume(viz7.GetFluid())
                PRINT_MPR3D = 0
        if keyCode in ['p', 'P']:
            if PRINT_PATH == 0:
                viz2.viz_VisualizeDICOM_augment(dicom_path3)
                viz3.viz_VisualizeDICOM_augment(dicom_path3)
                viz2.viz_SetViewportName('1,2,3 Line', 10, 260)
                PRINT_PATH = 1
            else:
                viz2.GetRenderer().RemoveVolume(viz2.GetPath())
                viz3.GetRenderer().RemoveVolume(viz3.GetPath())
                viz2.viz_SetViewportName(' NO  Line', 10, 260)
                PRINT_PATH = 0
        if keyCode in ['o', 'O']:
            if PRINT_PATH == 0:
                viz2.viz_VisualizeDICOM_augment_many(dicom_path3)
                viz3.viz_VisualizeDICOM_augment_many(dicom_path3)
                viz2.viz_SetViewportName('4,5,6 Line', 10, 260)
                PRINT_PATH = 1
            else:
                viz2.GetRenderer().RemoveVolume(viz2.GetPath())
                viz3.GetRenderer().RemoveVolume(viz3.GetPath())
                viz2.viz_SetViewportName(' NO  Line', 10, 260)
                PRINT_PATH = 0
        if keyCode in ['i', 'I']:
            if PRINT_PATH == 0:
                viz2.viz_VisualizeDICOM_augment_many1(dicom_path3)
                viz3.viz_VisualizeDICOM_augment_many1(dicom_path3)
                viz2.viz_SetViewportName('7,8,9 Line', 10, 260)
                PRINT_PATH = 1
            else:
                viz2.GetRenderer().RemoveVolume(viz2.GetPath())
                viz3.GetRenderer().RemoveVolume(viz3.GetPath())
                viz2.viz_SetViewportName(' NO  Line', 10, 260)
                PRINT_PATH = 0

    def displayClickPoints():
        global polygonActor, clickPointsList

        if len(clickPointsList) == 2:
            viz2.GetRenderer().RemoveActor(polygonActor)
            points = vtk.vtkPoints()
            lines = vtk.vtkCellArray()
            polygon = vtk.vtkPolyData()
            polygonMapper = vtk.vtkPolyDataMapper()
            polygonActor = vtk.vtkActor()

            points.SetNumberOfPoints(10)
            points.SetPoint(0, clickPointsList[0])
            points.SetPoint(1, clickPointsList[1])

            lines.InsertNextCell(2)
            lines.InsertCellPoint(0)
            lines.InsertCellPoint(1)

            polygon.SetPoints(points)
            polygon.SetLines(lines)
            tubes = vtk.vtkTubeFilter()
            tubes.SetInputData(polygon)
            tubes.SetNumberOfSides(20)
            tubes.SetRadius(5)
            tubes.Update()
            polygonMapper.SetInputData(tubes.GetOutput())
            polygonActor.SetMapper(polygonMapper)
            polygonActor.GetProperty().SetColor(0.53, 0.53, 0.53)
            viz2.GetRenderer().AddActor(polygonActor)
            renWin.Render()
        elif len(clickPointsList) == 1:
            source = vtk.vtkSphereSource()

            source.SetRadius(10)
            # 388*0.677734375,301*0.677734375,31*8-4
            source.SetCenter(clickPointsList[0])
            source.SetPhiResolution(11)
            source.SetThetaResolution(21)

            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(source.GetOutputPort())
            polygonActor = vtk.vtkActor()
            polygonActor.SetMapper(mapper)
            polygonActor.GetProperty().SetDiffuseColor(0.6, 0.7, 0.45)

            viz2.GetRenderer().AddActor(polygonActor)
            renWin.Render()

    def RightButtonPressEvent(obj, event):

        points = vtk.vtkPoints()
        points.SetNumberOfPoints(6)

        x, y = obj.GetInteractor().GetEventPosition()

        worldPicker.Pick(x, y, 0, current_ren)
        worldPos = worldPicker.GetPickPosition()

        singleClickedPoint = [worldPos[0], worldPos[1], worldPos[2]]
        clickPointsList.append(singleClickedPoint)

        displayClickPoints()

        if DEBUG_MODE:
            print("Screen Coordinates:: ", x, y)
            print("worldPos ", worldPos[0], worldPos[1], worldPos[2])
            print("ClickPoints:: ")
            print(" ", clickPointsList)
        return
    interactorStyle.AddObserver("RightButtonPressEvent", RightButtonPressEvent)
    interactor.AddObserver("KeyPressEvent", KeyPressEvent)
    renWin.SetFullScreen(1)
    displayClickPoints()
    renWin.Render()
    interactor.Start()
