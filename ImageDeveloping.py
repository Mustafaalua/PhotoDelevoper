from PIL import Image, ImageOps
import os

try:
    #Read undevelopedPictures and extract .png files
    files = []
    directory = os.path.curdir+r"\undevelopedPictures"
    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f) and f.endswith(".png"):
            files.append(f)
    
    #Download all relevant files
    uploadDirectory = os.path.curdir+r"\developedPictures"
    for picture in files:
        img = Image.open(picture)
        
        #Convert
        img = img.convert('RGB')

        #Invert
        imgInvert = ImageOps.invert(img)

        #Contrast
        imgInvert = ImageOps.autocontrast(imgInvert)

        #Save
        newPath = uploadDirectory+"\developed"+os.path.basename(picture)
        imgInvert.save(newPath)
        print("Uploaded a new photo: "+newPath)     
except:
    print("Failed")
    pass
