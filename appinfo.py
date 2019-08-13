#  Copyright (c) 2019
#  Author: Srikanth Gatta

import constants
import subprocess

def GetIOSAppInfomation(app_path):
  '''
  Get information about the specified iOS App.
  Example: Name, Bundle Id, Version of the app.
  :param app_path:
  :return:
  '''
  bundle_id = subprocess.execute_process(
                        subprocess.plist_buddy(app_path,
                                               constants.IOS_BUNDLE_ID))