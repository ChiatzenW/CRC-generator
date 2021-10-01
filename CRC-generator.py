from PIL import Image, ImageDraw, ImageFont
import os
import toml



def vertical_merge(im1:Image, im2:Image):
    merged=Image.new('RGB', (im1.size[0], im1.size[1]+im2.size[1]), (225,225,225) )
    merged.paste(im1, (0,0))
    merged.paste(im2, (0, im1.height))
    return merged

def cut(s:str):
    size=50
    for i in range(int((len(s)-(len(s)%size))/size)):
        s_1=s[:(i*size+2*i)]
        s_2=s[(i*size+2*i):]
        s=s_1+"\n"+s_2
    return s


def fit_font_size(s:str, sizes:(int,int)):
    s=cut(s)
    font_size=1
    font = ImageFont.truetype("Hack-Regular.ttf", size=1)
    while font.getsize(s)[0]<sizes[0]*(0.65) and font.getsize(s)[1]<sizes[1]*(0.90):
        font_size+=1
        font = ImageFont.truetype("Hack-Regular.ttf", font_size)
    return font
        
def create_crc_card(c:dict, s:str):
    if not os.path.exists('crc'):
            os.mkdir('crc')
    
    class_head = Image.new('RGB', (1000,100), (225,225,225)) 
    draw = ImageDraw.Draw(class_head)
    draw.line((0, class_head.size[1])+class_head.size, width=40, fill= (0,0,0))
    draw.text((0, 0),cut(s),(0,0,0),fit_font_size(s, class_head.size))
    
    for i in c:
        r_c_line = Image.new('RGB', (1000,100), (225,225,225))
        draw2 = ImageDraw.Draw(r_c_line)
        draw2.line((r_c_line.size[0]/2, 0)+(r_c_line.size[0]/2, r_c_line.size[1]), width=20, fill= (0,0,0))
        draw2.line((0, r_c_line.size[1])+r_c_line.size, width=40, fill= (0,0,0))
        sizes=(r_c_line.size[0]/2, r_c_line.size[1]/2)
        draw2.text((0, 0),cut(i),(0,0,0),fit_font_size(i, sizes))
        draw2.text((r_c_line.size[0]/2+21, 0),cut(c[i]),(0,0,0),fit_font_size(c[i], sizes))
        class_head=vertical_merge(class_head, r_c_line)


        class_head.save("crc/"+s+".jpg", 'JPEG')

def main():
    """try:
        classes = toml.load("crc_classes.toml")
        for i in classes:
            create_crc_card(classes[i], i)
    except Exception as e:
        print(e) """
    classes = toml.load("crc_classes.toml")
    for i in classes:
        create_crc_card(classes[i], i)
    


if __name__ == "__main__":
    main()

