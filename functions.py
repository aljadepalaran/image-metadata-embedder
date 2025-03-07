from PIL import ImageFont, ImageDraw
import os

# Add text into the image
def add_text(image, text, topleft, size, colour):
  font = ImageFont.truetype("./fonts/Montserrat.ttf", size)
  draw = ImageDraw.Draw(image)
  draw.text(topleft, text, font=font,fill=colour)
  return image

# Generate the output filename based on the input filename
# todo: fix up supported extension list
def generate_filename(filename):
  if filename.endswith('.jpg') | filename.endswith('.jpeg'):
    return f'{filename}_with_metadata.jpg'
  elif filename.endswith('.png'):
    return f'{filename}_with_metadata.png'
  else:
    return f'{filename}_with_metadata.jpg'

# Return specific exif data
def parse_exif(exif):
  return exif['FocalLength'], float(exif['ExposureTime']), exif['FNumber'], exif['ISOSpeedRatings']

# Return a list of the filepaths to process from a directory
def list_valid_filepaths(directory):
  paths = []
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(('.jpg', '.jpeg', '.png')):
      paths.append(os.path.join(directory.decode("utf-8"), filename))
  return paths

def list_valid_filepaths_recursively(directory):
  print()