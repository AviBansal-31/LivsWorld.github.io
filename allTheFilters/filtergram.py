#this imports everything from the filters file into this file so we don't
#have to put it before each function from the filters library
from filters import *

def main():
    #camelCase: always start with a lowercase then use uppercase
    #loads image
    pandaImage = load_img("cute_panda.jpg")
    #shows and saves image to same directory code was saved
    show_img(pandaImage)
    save_img(pandaImage, "test2.bmp")
    obamicon(pandaImage)
