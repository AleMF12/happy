from PIL import Image, ImageDraw, ImageFont

### YOUR CODE STARTS HERE
# First I created the variable img which represents the image. I used the file from https://infopalette.com/2020/09/28/the-deeper-the-love-the-deeper-the-hate/.
img = Image.open("IMG-6448.png")
# second I created another variable called dra for draw the image.
dra = ImageDraw.Draw(img)
# in this step I chose the fonte size and type for the text which is Comic Sans MS Bold Italic for windows 10 and size 26 for the words. I found the information about the font on
# the website https://learn.microsoft.com/en-us/typography/fonts/windows_10_font_list.
fnt = ImageFont.truetype('comicz.ttf', 26)
# This step I chose the center for horizontal iqual 200 and vertical 470 and then I wrote the texts.
dra.text((200,470),f'{"Romanos 12:21"}\n{"No seas vencido de lo malo, sino vence con el bien el mal."}\n\n{"Romans 12:21"}\n{"Do not let evil conquer you, but conquer evil by doing good."}', font=fnt, fill=(0,0,0))
# Finally I saved the image in png format. Then I displayed it on screen.
img.save("my-bible-verse.png")
img.show()
### YOUR CODE ENDS HERE