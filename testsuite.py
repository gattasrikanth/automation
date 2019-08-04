#  Copyright (c) 2019
#  Author: Srikanth Gatta

import constants
import appinfo

def execute_tests(args):
  if args.platform == constants.IOS:
    app_info = appinfo.GetIOSAppInfomation(args.app)