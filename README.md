<h1 align="center">
  Image Metadata Embedder
  <br>
</h1>

### Summary
Image metadata embedder is a CLI tool written in Python to allow the user to add the metadata from a photo as text.
This allows the user to share the settings under which a photo was taken.

### Example
Input Image:
![Base Image](test.jpg "Base Image")

Output Image:
![Result Image](saved.jpg "Result")

### Requirements
To run this, you will need:
- Python3
- Pillow

You can install Pillow using `pip install pillow`

### Usage
To run the embedder on a single image, simply pass in the image name: `python3 main.py image.jpeg`

To run the embedder on a set of images, simply pass in the directory: `python3 main.py testdir`

### Arguments
There are various arguments that can be passed in to customise the output.
These are:
- Position (where the metadata will be placed in the image) `--pos=x,y`
- Size (the size of the metadata in pixel height) `--size=200`
- Space (the gap between the metadata - measured in number of spaces) `--space=5`

To get a full list of arguments, run `python3 main.py --help`

### Contributing
This project will remain open-source to allow the public to utilise this. To contribute, please submit a PR for review. Please include a description of the PR, what new features it implements or what bugs it fixes.