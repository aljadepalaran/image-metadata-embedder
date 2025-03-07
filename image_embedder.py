from PIL import Image, ExifTags
from functions import *
import os

class ImageEmbedder:
  def process_image(source, opts):
    image = Image.open(source)
    original_exif = image.info['exif']
    image_exif = image._getexif()

    if type(image_exif) == type(None):
      print(f'Skipping {source}, no exif data.')
    else:
      exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS }
      focal_length, exposure_time, aperature, iso = parse_exif(exif)
      space = int(opts['space']) * ' '
      text_to_add = f"{focal_length}mm{space}1/{int(1 / exposure_time)}{space}f/{aperature}{space}ISO{iso}"
      position = tuple(map(int, opts['pos'].split(',')))
      size = int(opts['size'])
      output = add_text(image, text_to_add, position, size, (255, 255, 255))
      output_filename = generate_filename(source)
      output.save(output_filename, exif=original_exif)
      print(f'Process complete. {output_filename} created.')

  @staticmethod
  def process_directory(source, recursive, opts):
    directory = os.fsencode(source)
    if recursive:
      print('Recursively running.')
      for filepath in list_valid_filepaths_recursively(directory):
        ImageEmbedder.process_image(filepath)
    else:
      for filepath in list_valid_filepaths(directory):
        ImageEmbedder.process_image(filepath, opts)
