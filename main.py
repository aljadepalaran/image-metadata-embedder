from PIL import Image, ExifTags, ImageDraw, ImageFont
print("Running...")

def add_text(im, text, topleft, size, colour):
  font = ImageFont.truetype("./Montserrat.ttf", size)
  draw = ImageDraw.Draw(im)
  draw.text(topleft, text, font=font,fill=colour)
  return im

if __name__ == "__main__":
  with Image.open("./test.jpg") as img:
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    focal_length = exif['FocalLength']
    exposure_time = float(exif['ExposureTime'])
    shutter_speed = f"1/{int(1 / exposure_time)}"
    aperature = exif['FNumber']

    print(exif)

    im = add_text(img, f"{focal_length}mm     {shutter_speed}     f/{aperature}", (500, 3500), 150, (255, 255, 255))
    im.save("./saved.jpg")
    print(img.size)