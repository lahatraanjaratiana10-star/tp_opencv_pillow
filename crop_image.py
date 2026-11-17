from PIL import Image


with Image.open("hopper.ppm") as im:

  
    box = (0, 0, 64, 64)
    region = im.crop(box)

    
    region.save("hopper_crop.jpg", "JPEG")
    print("success !")