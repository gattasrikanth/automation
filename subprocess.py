#  Copyright (c) 2019
#  Author: Srikanth Gatta

import subprocess
import constants

def execute_process(command):
  process = subprocess.Popen(command, stdout=subprocess.PIPE)
  out, _ = process.communicate()
  return out

def plist_buddy(app_path, info_identifier):
  return [constants.PLIST_BUDDY, '-c', 'Print %s' % info_identifier,
          '%s/Info.plist' % app_path].strip()
