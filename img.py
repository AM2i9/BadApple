import os, sys
from imgtoascii import CLUT

FRAME = 1
"""
This section includes code I stole from
https://gist.github.com/A2x2/b1b27b15b0590d36351b9b19ce25a04e,
which is a modified version of
https://gist.github.com/puhitaku/7eaf6142fa5a42425f55
I DO NOT OWN THIS SECTION OF CODE
"""
# <----------------Start of code I stole---------------->
def _create_incs_lut():
    incs = [(0x00, 0x5f), (0x5f, 0x87), (0x87, 0xaf), (0xaf, 0xd7), (0xd7, 0xff)]
    res = []
    for part in range(256):
        for s, b in incs:
            if s <= part <= b:
                if abs(s - part) < abs(b - part):
                    res.append('%02x' % s)
                else:
                    res.append('%02x' % b)
                break
    return res

RGB2SHORT_DICT = dict(CLUT)
INCS_LUT = _create_incs_lut()


def lut(part):
    return INCS_LUT[part]


def rgb2short_fast(r, g, b):
    return RGB2SHORT_DICT['%s%s%s' % (lut(r), lut(g), lut(b))]

def convertImage(myoption):
        from PIL import Image
        im = Image.open(myoption)
        x = im.size[0]
        im = list(im.getdata())
        ctr = 0
        s = []
        for i, p in enumerate(im):
            short = rgb2short_fast(p[0], p[1], p[2])
            if short == "16":
                s.append("░░")
            elif short == "231":
                s.append("██")
            else:
                s.append("▒▒")
            # s.append("%s " % short)
            if (i+1) % x == 0:
                s.append("\n")
            ctr += 1
        s.append("\n")

        ss = ''.join(s).splitlines()
        ss = '\n' + '\n'.join(ss[::2]) + ','
        return ss
# <----------------End of code I stole---------------->
# Below is my code
if __name__ == '__main__':

    with open('raw','a',encoding='utf-8') as rawfile:
        
        for frame in os.listdir('frames'):

            file = f"{FRAME}.png"
            print('Frame:',FRAME)
            line = (convertImage(f'frames\\{file}'))
            rawfile.write(line)
            FRAME += 1
        rawfile.close()