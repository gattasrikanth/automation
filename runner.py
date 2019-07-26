'''
This is the first file to start the with.
The idea is to implement a framework that supports Mobile Automation
using Appium.
'''


def parse_arguments(args):
  pass

def run(args=None):
  '''This will be the first function that gets called.
  The goal here is to read all the arguments that are passed to the script.
  '''
  if args:
    parse_arguments(args)
  else:
    print('You need to supply arguments.')

if __name__ == '__main__':
  run()