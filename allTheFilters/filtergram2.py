from filters import *

def main():
    pandaImage = load_img("cute_panda.jpg")
    show_img(pandaImage)
    save_img(pandaImage, "test3.bmp")
    grayscale(pandaImage)
