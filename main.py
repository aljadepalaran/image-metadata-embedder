import argparse, os
from image_embedder import ImageEmbedder

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-d", "--debug", action="store_true", help="debug mode")
  parser.add_argument("-r", "--recursive", action="store_true", help="enable to run on directories recursively. this includes child directories")
  parser.add_argument("-p", '--pos', help="the position of the text in --pos=X,Y")
  parser.add_argument('--size', help="the size of the text in pixel height")
  parser.add_argument("-s", "--skip", action="store_true", help="skip logic")
  parser.add_argument("src", help="source file or directory")
  args = parser.parse_args()
  config = vars(args)
  debug_mode = config['debug']
  debug_mode and print(f"Input arguments: {config}")
  source = config['src']
  opts = { 'pos': config['pos'], 'size': config['size'] }

  if config['skip']:
    quit()

  if os.path.isfile(source):
    debug_mode and print('File detected. Processing as file.')
    ImageEmbedder.process_image(source=source, opts=opts)
    print('Processing complete.')

  elif os.path.isdir(source):
    debug_mode and print('Directory detected. Processing all files inside directory.')
    ImageEmbedder.process_directory(source=source, recursive=config['recursive'])
    print('Processing of directory complete.')

  else:
    print('Invalid argument passed. Exiting...')
    quit()
