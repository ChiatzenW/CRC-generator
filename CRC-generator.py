from PIL import Image
from os import path

class CRC_generator():
    def main():
        if path.isfile('crc.jpg'):
            img = Image.open(crc.jpg)
        else:
            img = Image.new('RGB', (720, 576), (225,225,225))
            img.save("crc.jpg")

    def new_crc_menu():
        opt = 2
        print("What do you want to do now?")
        print("1. Create new CRC card.")
        print("2. Exit.")

        return int(input())

    def new_class():
        class_name = ""
        class_name = input("Class name:")

    def new_sub_line():
        res = ""
        collab=""
        res = input("Responsibility:")
        collab = input("Collaborator:")

