from distutils import extension
import os 
import shutil
Downloads = "C:\\Users\\Admin\\Downloads"
destination_folder = "C:\\Users\\Admin\\Desktop\\DESKTOP\\LAKSH\\LAKSH\\WHITEHAT JR\\PYTHON CODES\\P-102\\destination_folder"
list_of_fies = os.listdir(Downloads)
for filename in list_of_fies:
    name,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in [".pdf",".PDF",".pptx",".docx",".xlsx",'.gif','.png','.jpg','.jpeg','.jfif']:
        path1=Downloads+'/'+filename
        path2=destination_folder+'/'+"documentfiles"
        path3=destination_folder+'/'+"documentfiles"+'/'+filename 
        
        if os.path.exists(path2):
            print("moving"+filename+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)    
            print("moving"+filename+"...")
            shutil.move(path1,path3)