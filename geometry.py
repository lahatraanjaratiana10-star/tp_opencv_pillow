from PIL import Image

with Image.open("hopper.ppm") as im:

    im_resized = im.resize((128, 128))
    im_resized.save("hopper_resized.jpg", "JPEG")


    im_rotated = im.rotate(45)
    im_rotated.save("hopper_rotated.jpg", "JPEG")

    print("geometry transformations completed!")