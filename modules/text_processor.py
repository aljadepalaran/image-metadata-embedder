from PIL import ImageFont, ImageDraw

# Add text into the image
def add_text(image, text, topleft, size, colour):
  font = ImageFont.truetype("./fonts/Montserrat.ttf", size)
  draw = ImageDraw.Draw(image)
  draw.text(topleft, text, font=font,fill=colour)
  return image

# Generate the output filename based on the input filename
def generate_filename(filename):
  if filename.endswith('.jpg') | filename.endswith('.jpeg'):
    return f'{filename}_with_metadata.jpg'
  elif filename.endswith('.png'):
    return f'{filename}_with_metadata.png'
  else:
    return f'{filename}_with_metadata.jpg'
