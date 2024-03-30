def test_main(num_of_data, casenumber):    
    from ScanLoader import ScanLoader
    import Visualize as viz
    import vtk
    import os
    import globals
    #IP = input("Enter path containing scans: ")
    globals.initialize(casenumber)
    print(globals.IP)
    loader = ScanLoader(globals.IP)
    loader.getPatientInfo()
    patient_idx = num_of_data

    plist = loader.getPatientList()
    print(globals.IP + plist[int(patient_idx)])
    dic_path = os.path.join(globals.IP,str(plist[int(patient_idx)]))
    dic_path2 = os.path.join(globals.IP,str(plist[int(patient_idx)+1]))
    dic_path3 = os.path.join(globals.IP,str(plist[int(patient_idx)+2]))


    viz.vis(dic_path,dic_path2,dic_path3, casenumber)
