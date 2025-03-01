from PIL import ExifTags

def parse_exif(exif_data):
  return exif['FocalLength'], float(exif['ExposureTime']), exif['FNumber']
