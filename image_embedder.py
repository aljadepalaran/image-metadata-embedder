from PIL import Image, ExifTags
from functions import *
import os

class ImageEmbedder:
  def process_image(source, opts):
    image = Image.open(source)
    exif = { ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS }
    focal_length, exposure_time, aperature = parse_exif(exif)
    space = int(opts['space']) * ' '
    text_to_add = f"{focal_length}mm{space}1/{int(1 / exposure_time)}{space}f/{aperature}"
    position = tuple(map(int, opts['pos'].split(',')))
    size = int(opts['size'])
    output = add_text(image, text_to_add, position, size, (255, 255, 255))
    output_filename = generate_filename(source)
    output.save(output_filename)
    print(f'Process complete. {output_filename} created.')

  @staticmethod
  def process_directory(source, recursive):
    directory = os.fsencode(source)
    if recursive:
      print('Recursively running.')
      for filepath in list_valid_filepaths_recursively(directory):
        ImageEmbedder.process_image(filepath)
    else:
      for filepath in list_valid_filepaths(directory):
        ImageEmbedder.process_image(filepath)
