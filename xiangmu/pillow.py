from PIL import Image,ImageDraw,ImageFont
import random
import io
class code:
    def __init__(self):
        self.font="arial.ttf"
        # self.fontsize=random.randint(10,15)
        self.fonts="abcdefhij23456"
        self.length=4
        self.fontsizemin=20
        self.fontsizemax=30
        # self.fontsize=random.randint(15,20)
        self.img=None
        self.w=120
        self.h=50
        self.linenum=random.randint(5,10)
        self.pointnum = random.randint(20, 30)
        self.str=""
    def randomsize(self):
        return random.randint(12)
    def randomfontcolor(self):
        return (random.randint(0,125),random.randint(0,125),random.randint(0,125))
    def randombgcolor(self):
        return (random.randint(125,255),random.randint(125,255),random.randint(125,255))
    def create(self):
        self.bgcolor=self.randombgcolor()
        self.img=Image.new("RGBA",(self.w,self.h),self.randombgcolor())
    def lines(self):
        draw = ImageDraw.Draw(self.img)
        for index in range(self.linenum):
            x=random.randint(0,self.w)
            y = random.randint(0, self.h)
            x1 = random.randint(0, self.w)
            y1 = random.randint(0, self.h)
            draw.line([x,y,x1,y1],fill=self.randombgcolor(),width=random.randint(1,3))
    def points(self):
        draw = ImageDraw.Draw(self.img)
        for index in range(self.pointnum):
            x = random.randint(0, self.w)
            y = random.randint(0, self.h)
            draw.point([x,y],fill=self.randomfontcolor())

    def createtext(self):
        randomsize = random.randint(self.fontsizemin, self.fontsizemax)
        for index in range(self.length):
            draw = ImageDraw.Draw(self.img)
            codestr = self.fonts[random.randint(0, len(self.fonts) - 1)]
            font1 = ImageFont.truetype(self.font,randomsize)
            self.str+=codestr.lower()
            # font1.getsize()
            x=index*randomsize
            y=random.randint(0,self.h-randomsize)
            draw.text((x,y),codestr,fill=self.randomfontcolor(),font=font1)
            # self.img = self.img.rotate(5)
            self.fontrotate()
    def fontrotate(self):
        angel=random.randint(-5,5)
        self.img=self.img.rotate(angel)
        img = Image.new("RGBA", (self.w, self.h), self.randombgcolor())
        self.img=Image.composite(self.img,img,self.img)
    def output(self):
        self.create()
        self.lines()
        self.points()
        self.createtext()
        # self.img.show()
        # self.img.save("11111.png")
        imgs=io.BytesIO()
        # # # print(imgs,"888888888888888888888888888888888888888")
        self.img.save(imgs,"png")
        # # # # print(imgs.getvalue(),"333333333333333333333333333333333")
        return imgs.getvalue()

# obj=code()
# obj.output()