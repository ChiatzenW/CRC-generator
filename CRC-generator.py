from PIL import Image, ImageDraw, ImageFont
import os
import toml

font = ImageFont.truetype("Hack-Regular.ttf", size=16)
def main():
    try:
        classes = toml.load("crc_classes.toml")
        for i in classes:
            create_crc_card(classes[i], i)
    except Exception as e:
        print(e)
        
def create_crc_card(c:dict, s:str):
    if not os.path.exists('crc'):
            os.mkdir('crc')
    class_head = Image.new('RGB', (1000,100), (225,225,225)) 
    draw = ImageDraw.Draw(class_head)
    draw.line((0, class_head.size[1])+class_head.size, fill = 250)
    class_head.save("crc/"+s+".jpg", 'JPEG')

    


if __name__ == "__main__":
    main()

