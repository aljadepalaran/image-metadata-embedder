from PIL import Image, ExifTags
print("Running...")

if __name__ == "__main__":
  with Image.open("./test.jpg") as img:
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    print(f"Lens: {exif['LensModel']}")
    print(f"FocalLength: {exif['FocalLength']}mm")
    exposure_time = float(exif['ExposureTime'])
    shutter_speed = f"1/{1 / exposure_time}"
    print(f"Shutter Speed: {shutter_speed}")
    print(f"Aperature: f{exif['FNumber']}")
    print(img.size)