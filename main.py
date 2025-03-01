from PIL import Image, ExifTags
from modules.text_processor import add_text, generate_filename
import sys

def parse_exif(exif_data):
  return exif['FocalLength'], float(exif['ExposureTime']), exif['FNumber']

if __name__ == "__main__":
  file = sys.argv[1]
  new_filename = generate_filename(file)
  print(f"Adding metadata as text to {file}.")

  with Image.open(file) as img:
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    focal_length, exposure_time, aperature = parse_exif(exif)
    shutter_speed = f"1/{int(1 / exposure_time)}"

    im = add_text(img, f"{focal_length}mm     {shutter_speed}     f / {aperature}", (500, 3500), 200, (255, 255, 255))
    im.save(new_filename)

  print("Process complete.")
