#  Copyright (c) 2019
#  Author: Srikanth Gatta

'''
This is the first file to start the with.
The idea is to implement a framework that supports Mobile Automation
using Appium.
'''


import argparse
import constants
import testsuite

def parse_arguments():
  args_parser = argparse.ArgumentParser(description="Run Native Mobile Apps")
  args_parser.add_argument('-p', '--platform',
                           choices=[constants.ANDROID, constants.IOS],
                           help='Choose platform to run against')
  args_parser.add_argument('-d', '--device',
                           choices=[constants.DEVICE_TYPE_REAL,
                                    constants.DEVICE_TYPE_SIM],
                           help='Choose platform to run against')
  args_parser.add_argument('-host', '--appium-host',
                           default=constants.APPIUM_DEFAULT_HOST,
                           help='Host addresses to run appium port on.')
  args_parser.add_argument('-port', '--appium-port',
                           default=constants.APPIUM_DEFAULT_PORT,
                           help='Port to run appium server on')
  args_parser.add_argument('-app', '--app_path', help='Full path of the app to be installed on the device.')
  args = args_parser.parse_args()
  return args

def main(passed_args=None):
  '''This will be the first function that gets called.
  The goal here is to read all the arguments that are passed to the script.
  '''
  args = parse_arguments()
  testsuite.execute_tests(args)

if __name__ == '__main__':
  main()