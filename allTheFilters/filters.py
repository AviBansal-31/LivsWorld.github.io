#this opens all special Image functions from PILLOW for us to use
from PIL import Image

def load_img(filePathPlaceholder):
    #this creates an Image Object by opening a file
    #open() is a function from the library that returns an Image Object
    #we then save this into a variable called imageObject
    #then we return the function
    imageObject = Image.open(filePathPlaceholder)
    return imageObject
#remember that imageObjectPlaceholder only has to match inside the definitions
def show_img(imageObjectPlaceholder):
    imageObjectPlaceholder.show()

def save_img(imageObjectPlaceholder, saveFileName):
    imageObjectPlaceholder.save(saveFileName, "jpeg")

def obamicon(imageObjectPlaceholder):
    pixels = imageObjectPlaceholder.getdata()
    
    new_pixel = []
    #these are the tuples for the RGB values
    #we have to run this thru something else for it to recognize them as colors
    darkBlue = (0,51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #this for loop goes thru every pixel in the image and determines the
    #intensity of the value.
    #then a conditional determines what color it will be filtered to 

    for i in pixels:
        intensity = i[0] + i[1] + i[2]

        if intensity < 182:
            new_pixel.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixel.append(red)
        elif intensity >=364 and intensity < 546:
            new_pixel.append(lightBlue)
        elif intensity >= 546:
            new_pixel.append(yellow)
    imageObjectPlaceholder.putdata(new_pixel)
    show_img(imageObjectPlaceholder)

def grayscale(imageObjectPlaceholder):
    #gets size
    width, height = image.size
    #creates new image and pixel map
    new = create_image(width, height)
    pixels = new.load()
    #for loop that transforms image to grayscale
    for i in range(width):
        for j in range(height):
            #gets pixels from original image
            pixel = get_pixel(image, i, j)
            #gets RGB values
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            #transforms to grayscale(averages out RGB values)
            gray = (red * 0.229) + (green * 0.587) + (blue * 0.114)
            #puts pixels into new image
            pixels[i, j] = (int(gray), int(gray), int(gray))
        #returns new image
        return new

    
pandaImage = load_img("cute_panda.jpg")
show_img(pandaImage)
save_img(pandaImage, "testing_save_image.bmp")
obamicon(pandaImage)
