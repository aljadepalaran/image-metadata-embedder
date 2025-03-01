from PIL import Image, ExifTags
from modules.text_processor import add_text, generate_filename
import sys
import argparse
import os

def parse_exif(exif_data):
  return exif['FocalLength'], float(exif['ExposureTime']), exif['FNumber']

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
  parser.add_argument("-r", "--recursive", action="store_true", help="enable to run on directories recursively. this includes child directories")
  parser.add_argument("src", help="source file or directory")
  args = parser.parse_args()
  config = vars(args)
  debug_mode = config['debug']
  if debug_mode:
    print(f"Input arguments: {config}")

  file = config['src']
  print(f'isfile: {os.path.isfile(file)}')
  print(f'isdir: {os.path.isdir(file)}')
  # if isfile
  #   process file
  # elif isdir
  #   process directory, top level or recursive based on options
  # else
  #   return error

  new_filename = generate_filename(file)
  if debug_mode:
    print(f"New filename: {new_filename}")
  print(f"Adding metadata as text to {file}.")

  with Image.open(file) as img:
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    if debug_mode:
      print(f"Metadata: {exif}")
    focal_length, exposure_time, aperature = parse_exif(exif)
    shutter_speed = f"1/{int(1 / exposure_time)}"

    text_to_add = f"{focal_length}mm     {shutter_speed}     f / {aperature}"
    if debug_mode:
      print(f"Text: {text_to_add}")
    output = add_text(img, text_to_add, (500, 3500), 200, (255, 255, 255))
    output.save(new_filename)

  print("Process complete.")
