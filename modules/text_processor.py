from PIL import ImageFont, ImageDraw

def add_text(image, text, topleft, size, colour):
  font = ImageFont.truetype("./fonts/Montserrat.ttf", size)
  draw = ImageDraw.Draw(image)
  draw.text(topleft, text, font=font,fill=colour)
  return image
