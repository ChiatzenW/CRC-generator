from PIL import Image
import os


def new_crc_menu():
    opt = 2
    print("What do you want to do now?")
    print("1. Create new CRC card.")
    print("2. Exit.")

    return int(input())

def new_class():
    class_name = ""
    class_name = input("Class name:")
    class_head = img = Image.new('RGB', (720, 30), (225,225,225))
    hack_fnt = "ttf"

def new_sub_line():
    res = ""
    collab=""
    res = input("Responsibility:")
    collab = input("Collaborator:")

def main():
    opt = 2
    opt = new_crc_menu()
    sub_opt=1
    while opt != 2:
        if not os.path.exists('crc'):
            os.path.mkdir('crc')
        else:
            img = Image.new('RGB', (720, 30), (225,225,225))
            img.save("crc.jpg")
        new_class()
        while sub_opt != 2:
           new_sub_line()
    opt = new_crc_menu()


if __name__ == "__main__":
    main()

