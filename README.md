#  Image Metadata Embedder

## Summary
This repository contains tools required to add metadata as text to images making it easy to share the settings used to capture the image.

## Example
Input Image:
![Base Image](test.jpg "Base Image")

Output Image:
![Result Image](saved.jpg "Result")

## Requirements
To run this, you will need:
- Python3
- Pillow

You can install Pillow using `pip install pillow`

## Usage
To run the embedder on a single image, simply pass in the image name: `python3 main.py image.jpeg`

To run the embedder on a set of images, simply pass in the directory: `python3 main.py testdir`

## Contributing
This project will remain open-source to allow the public to utilise this. To contribute, please submit a PR for review. Please include a description of the PR, what new features it implements or what bugs it fixes.