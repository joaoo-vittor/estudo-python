from PIL import Image
import os

path = '/home/joao/Pictures'
save_img_path = '/home/joao/Pictures/imgs'
paths_img = []

for i in os.listdir(path):
    aux = ''
    if '.png' in i:
        aux += path + '/' + i
        paths_img.append((aux, i))


for full_path, name in paths_img:
    img = Image.open(full_path)

    # # width, height = img.size
    # # (esquerda, superior, direita, inferior) significa dois pontos
    area = (0, 0, 1366, 768)
    img_crop = img.crop(area)

    save_path = ''
    save_path = save_img_path + '/' + name

    img_crop.save(
        save_path,
        optimize=True,
        quality=70
    )

    img_crop.close()
    img.close()
