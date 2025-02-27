from PIL import Image
print("Running...")

if __name__ == "__main__":
  with Image.open("./test.jpg") as im:
    print("test")
    print(im.size)