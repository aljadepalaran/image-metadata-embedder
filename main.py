import argparse, os
from image_embedder import ImageEmbedder

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
  parser.add_argument("-r", "--recursive", action="store_true", help="enable to run on directories recursively. this includes child directories")
  parser.add_argument("src", help="source file or directory")
  args = parser.parse_args()
  config = vars(args)
  debug_mode = config['debug']
  debug_mode and print(f"Input arguments: {config}")
  source = config['src']

  if os.path.isfile(source):
    debug_mode and print('File detected. Processing as file.')
    ImageEmbedder.process_image(source)
    print('Processing complete.')

  elif os.path.isdir(source):
    debug_mode and print('Directory detected. Processing all files inside directory.')
    ImageEmbedder.process_directory(source=source, recursive=config['recursive'])
    print('Processing of directory complete.')

  else:
    print('Invalid argument passed. Exiting...')
    quit()
