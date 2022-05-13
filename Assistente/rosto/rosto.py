from PIL import Image

imageObject = Image.open("falando.gif")  # já foi
image2 = Image.open("chocado.gif")  # já foi
image3 = Image.open("erro.gif")  # já foi
image4 = Image.open("espremendoolho.gif")  # já foi
image5 = Image.open("piscando.gif")  # já foi
image6 = Image.open("dormindo.gif")  # já foi


def falar():
    global imageObject
    # Os gifs possuem em sua maioria 2 frames, enquanto o de fala possuem 8 frames e o dormindo tem 3 frames
    for frame in range(0, imageObject.n_frames):
        imageObject.seek(frame)
        imageObject.show()


def dorme():
    global image6
    for frame in range(0, image6.n_frames):
        image6.seek(frame)
        image6.show()


def pisca():
    global image5
    for frame in range(0, image5.n_frames):
        image5.seek(frame)
        image5.show()


def erro():
    global image3
    for frame in range(0, image3.n_frames):
        image3.seek(frame)
        image3.show()


def choque():
    global image2
    for frame in range(0, image2.n_frames):
        image2.seek(frame)
        image2.show()


def espreme():
    global image4
    for frame in range(0, image4.n_frames):
        image4.seek(frame)
        image4.show()
