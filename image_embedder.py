from PIL import Image, ExifTags
from functions import parse_exif, add_text, generate_filename

class ImageEmbedder:
  def process_image(source):
    image = Image.open(source)
    exif = { ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS }
    focal_length, exposure_time, aperature = parse_exif(exif)
    text_to_add = f"{focal_length}mm     1/{int(1 / exposure_time)}     f/{aperature}"
    output = add_text(image, text_to_add, (500, 3500), 200, (255, 255, 255))
    output_filename = generate_filename(source)
    output.save(output_filename)
    print(f'Process complete. {output_filename} created.')

  def process_directory(recursive):
    print(f'recursive: {recursive}')
