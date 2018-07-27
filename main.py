from PIL import Image

sister = Image.open("gato1.png")
girl = Image.open("gato2.png")

gato3 = Image.open("gato3.png")

area = (130, 0)
area1 = (-140, 0)
sister.paste(girl, area, girl)

png_info = sister.info
sister.save('1.png', **png_info)

final = Image.open("1.png")

final.paste(gato3, area1, gato3)
png_info1 = final.info
final.save('1.png', **png_info1)

# sister.show()


