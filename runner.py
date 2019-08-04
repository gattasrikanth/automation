'''
This is the first file to start the with.
The idea is to implement a framework that supports Mobile Automation
using Appium.
'''

import argparse

def parse_arguments():
  args_parser = argparse.ArgumentParser(description="Run Native Mobile Apps")
  args_parser.add_argument('-p', '--platform',
                           choices=['Android', 'iOS'],
                           help='Choose platform to run against')
  args_parser.add_argument('-d', '--device',
                           choices=['Simulator', 'Real'],
                           help='Choose platform to run against')
  args_parser.add_argument('-host', '--appium-host', default='127.0.0.1',
                           help='Host addresses to run appium port on.')
  args_parser.add_argument('-port', '--appium-port', default=4723,
                           help='Port to run appium server on')
  args = args_parser.parse_args()

def main(passed_args=None):
  '''This will be the first function that gets called.
  The goal here is to read all the arguments that are passed to the script.
  '''
  parse_arguments()

if __name__ == '__main__':
  main()