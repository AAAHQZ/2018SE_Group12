from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image
#多个图片合一
arr = ['p1.png', 'p2.png', 'p3.png', 'p4.png']
toImage = Image.new('RGBA',(2000,2000))
for i in range(4):
    fromImge = Image.open(arr[i])
    # loc = ((i % 2) * 200, (int(i/2) * 200))
   #原 loc = ((int(i / 2) * 400), (i%2) * 400)
    loc = (0 , i* 400)
    print(loc)
    toImage.paste(fromImge, loc)

toImage.save('merged.png')

#图片生成pdf
def imgtopdf(input_paths, outputpath):
    (maxw, maxh) = Image.open(input_paths).size
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(input_paths, 0, 0, maxw, maxh)
    c.showPage()
    c.save()
# 调用demo:
imgtopdf("merged.png", "a.pdf")