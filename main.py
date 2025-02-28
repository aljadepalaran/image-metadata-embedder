from PIL import Image, ExifTags, ImageDraw, ImageFont

def add_text(im, text, topleft, size, colour):
  font = ImageFont.truetype("./Montserrat.ttf", size)
  draw = ImageDraw.Draw(im)
  draw.text(topleft, text, font=font,fill=colour)
  return im

def parse_exif(exif_data):
  return exif['FocalLength'], float(exif['ExposureTime']), exif['FNumber']

if __name__ == "__main__":
  print("Adding metadata as text into the image.")

  with Image.open("./test.jpg") as img:
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    focal_length, exposure_time, aperature = parse_exif(exif)
    shutter_speed = f"1/{int(1 / exposure_time)}"

    im = add_text(img, f"{focal_length}mm     {shutter_speed}     f / {aperature}", (500, 3500), 200, (255, 255, 255))
    im.save("./saved.jpg")

  print("Process complete.")