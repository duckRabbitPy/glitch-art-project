from io import BytesIO
import random
from django.core.files import File
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


#No filters
def make_thumbnail(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""

    im = image

    im = im.filter(ImageFilter.FIND_EDGES)

     # convert mode

    im.thumbnail(size) # resize image

    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output1') # create a django friendly File object

    return thumbnail

#With filter only
def make_thumbnail2(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""

    im = image

    im.thumbnail(size) # resize image

    #pixelate 
    PixVal = 2
    pixel_size = PixVal
    im = im.resize((im.size[0] // pixel_size,im.size[1] // pixel_size),Image.NEAREST)
    im = im.resize((im.size[0] * pixel_size,im.size[1] * pixel_size),Image.NEAREST)

    #change colour code
    datas = im.getdata()
    new_image_data = []
    redV = random.randrange(0, 300)
    greenV = random.randrange(0, 300)
    blueV = random.randrange(0, 300)

    for item in datas:
        # change all white (also shades of whites) pixels to
        # yellow
        if item[0] in list(range(190, 256)):
            new_image_data.append((redV, greenV, blueV))
        else:
            new_image_data.append(item)
    # update image data
    im.putdata(new_image_data)


    ######################################################

    #Pixel sorting code
    def sortBy(colorTuple, colorIndex, reverse):
        if reverse:
            return sorted(colorTuple, key=lambda x: x[colorIndex], reverse=reverse)
        else:
            return sorted(colorTuple, key=lambda x: x[colorIndex])

    imgList = list(im.getdata())
    loadImg = im.load()
    loadImgList = []
    loadImgList2 = []

    width, height = im.size

    if width <= 175 or height <= 175:
        raise ValueError("Image upload is too small")

    startWidth = random.randint(1, (width-150))
    startHeight = random.randint(1, (height-75))

    for i in range(startWidth, startWidth+150):
        for j in range(height):
            loadImgList.append(loadImg[i, j])


    for i in range(width):
        for j in range(startHeight, startHeight+75):
            loadImgList2.append(loadImg[i, j])

    loadImgList = sortBy(loadImgList, 2, False)
    loadImgList = sortBy(loadImgList, 1, False)
    loadImgList = sortBy(loadImgList, 0, False)


    loadImgList2 = sortBy(loadImgList2, 2, True)
    loadImgList2 = sortBy(loadImgList2, 1, True)
    loadImgList2 = sortBy(loadImgList2, 0, True)


    counter = 0

    for i in range(startWidth, startWidth+150):
        for j in range(height):
            loadImg[i, j] = loadImgList[counter]
            counter += 1


    counter = 0

    for i in range(width):
        for j in range(startHeight, startHeight+75):
            loadImg[i, j] = loadImgList2[counter]
            counter += 1


    ######################################################

    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output2') # create a django friendly File object

    return thumbnail


def make_thumbnail3(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""
    #with filter and colour change

    im = image

    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)

    im.thumbnail(size) # resize image

    #pixelate 
    PixVal = 2
    pixel_size = PixVal
    im = im.resize((im.size[0] // pixel_size,im.size[1] // pixel_size),Image.NEAREST)
    im = im.resize((im.size[0] * pixel_size,im.size[1] * pixel_size),Image.NEAREST)


    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output3') # create a django friendly File object

    return thumbnail

def make_thumbnail4(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""
    #With pixelation and filter and colour change
    im = image
    im = im.filter(ImageFilter.BLUR)

    im.thumbnail(size) # resize image

    #pixelate 
    PixVal = 2
    pixel_size = PixVal
    im = im.resize((im.size[0] // pixel_size,im.size[1] // pixel_size),Image.NEAREST)
    im = im.resize((im.size[0] * pixel_size,im.size[1] * pixel_size),Image.NEAREST)

    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output4') # create a django friendly File object

    return thumbnail

def make_thumbnail5(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""
    #With pixel sort and filter and colour change

    im = image

    im = im.filter(ImageFilter.SMOOTH_MORE)

    im.thumbnail(size) # resize image


    #pixelate 
    PixVal = 10
    pixel_size = PixVal
    im = im.resize((im.size[0] // pixel_size,im.size[1] // pixel_size),Image.NEAREST)
    im = im.resize((im.size[0] * pixel_size,im.size[1] * pixel_size),Image.NEAREST)


    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output5') # create a django friendly File object

    return thumbnail


def make_thumbnail6(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""
    #With pixel sort and filter and colour change

    im = image

    im = im.filter(ImageFilter.EDGE_ENHANCE)

    im.thumbnail(size) # resize image

   
    #Pixelate
    PixVal = 1
    pixel_size = PixVal
    im = im.resize((im.size[0] // pixel_size,im.size[1] // pixel_size),Image.NEAREST)
    im = im.resize((im.size[0] * pixel_size,im.size[1] * pixel_size),Image.NEAREST)


    #change colour code
    datas = im.getdata()
    new_image_data = []
    redV = random.randrange(0, 300)
    greenV = random.randrange(0, 300)
    blueV = random.randrange(0, 300)

    for item in datas:
        # change all white (also shades of whites) pixels to
        # yellow
        if item[0] in list(range(190, 256)):
            new_image_data.append((redV, greenV, blueV))
        else:
            new_image_data.append(item)
    # update image data
    im.putdata(new_image_data)



    ######################################################

    #Pixel sorting code
    def sortBy(colorTuple, colorIndex, reverse):
        if reverse:
            return sorted(colorTuple, key=lambda x: x[colorIndex], reverse=reverse)
        else:
            return sorted(colorTuple, key=lambda x: x[colorIndex])

    imgList = list(im.getdata())
    loadImg = im.load()
    loadImgList = []
    loadImgList2 = []

    width, height = im.size

    if width <= 175 or height <= 175:
        raise ValueError("Image upload is too small")

    startWidth = random.randint(1, (width-150))
    startHeight = random.randint(1, (height-75))

    for i in range(startWidth, startWidth+150):
        for j in range(height):
            loadImgList.append(loadImg[i, j])


    for i in range(width):
        for j in range(startHeight, startHeight+75):
            loadImgList2.append(loadImg[i, j])

    loadImgList = sortBy(loadImgList, 2, False)
    loadImgList = sortBy(loadImgList, 1, False)
    loadImgList = sortBy(loadImgList, 0, False)


    loadImgList2 = sortBy(loadImgList2, 2, True)
    loadImgList2 = sortBy(loadImgList2, 1, True)
    loadImgList2 = sortBy(loadImgList2, 0, True)


    counter = 0

    for i in range(startWidth, startWidth+150):
        for j in range(height):
            loadImg[i, j] = loadImgList[counter]
            counter += 1


    counter = 0

    for i in range(width):
        for j in range(startHeight, startHeight+75):
            loadImg[i, j] = loadImgList2[counter]
            counter += 1


    ######################################################


    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=95) # save image to BytesIO object

    thumbnail = File(thumb_io, name='output6') # create a django friendly File object

    return thumbnail

