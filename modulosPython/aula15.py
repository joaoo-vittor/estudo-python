"""
Aula 15

Pillow: redimensionando várias imagens automaticamente

"""
from PIL import Image
import os


def main(images_path, new_width=800):
    if not os.path.isdir(images_path):
        raise NotADirectoryError(f'{images_path} não encontrado')

    for root, dirs, files in os.walk(images_path):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.split(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # if converted_tag in file_full_path:
            #     apagaImagem(file_full_path)
            #     continue

            if converted_tag in file_full_path:
                continue

            """
            width     ---->   height
            new_width ---->   (new_height)

            new_height = (new_width * height) / width

            """

            img_pillow = Image.open(file_full_path)

            width, height = img_pillow.size

            new_height = round(((new_width * height) / width))

            new_image = img_pillow.resize(
                (new_width, new_height), Image.LANCZOS)

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70
            )

            new_image.close()
            img_pillow.close()


def apagaImagem(path):
    os.remove(path)


if __name__ == '__main__':
    images_path = '/home/joao/Pictures/'
    main(images_path, new_width=200)
