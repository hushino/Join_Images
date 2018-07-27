from PIL import Image
import numpy as np

gato1 = Image.open("gato1.png")
gato2 = Image.open("gato2.png")

gato3 = Image.open("gato3.png")

area = (130, 0)
area1 = (-140, 0)
gato1.paste(gato2, area, gato2)

png_info = gato1.info
gato1.save('1.png', **png_info)

final = Image.open("1.png")

final.paste(gato3, area1, gato3)
png_info1 = final.info

final.save('1.png', **png_info1)







# im = Image.open("1.png")
# replace a single RGBA color
# im = Image.open('1.png')
# im = im.convert('RGBA')
#
# data = np.array(im)   # "data" is a height x width x 4 numpy array
# red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability
#
# # Replace white with red... (leaves alpha values alone...)
# white_areas = (red == 133) & (green == 130) & (blue == 138)
# data[..., :-1][white_areas.T] = (181, 64, 83)  # Transpose back needed
#
# im2 = Image.fromarray(data)
# im2.show()


# def redorblack(im):
#     newimdata = []
#     redcolor = (0, 0, 0)
#     blackcolor = (0, 0, 0)
#     for color in im.getdata():
#         if color == redcolor:
#             newimdata.append(redcolor)
#         else:
#             newimdata.append(blackcolor)
#     newim = Image.new(im.mode, im.size)
#     newim.putdata(newimdata)
#     return newim


# redorblack(im).save("1.png")
# sister.show()
