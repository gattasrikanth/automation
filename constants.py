#  Copyright (c) 2019
#  Author: Srikanth Gatta

'''
ALL (if not MOST) of the framework constants need tobe delclared in this file.
This fill serves as main place to lookup all configurable constants.
'''

# Platforms
ANDROID = 'Android'
IOS = 'IOS'
WEB = 'Desktop'

APPIUM_DEFAULT_HOST = '127.0.0.1'
APPIUM_DEFAULT_PORT = '4723'

DEVICE_TYPE_REAL = 'Real'
DEVICE_TYPE_SIM = 'Simulator'

# PlistBuddy is a tool to read and modify values inside of a plist structure.
PLIST_BUDDY = '/usr/libexec/PlistBuddy'
# The unique string that identifies the iOS app under test.
IOS_BUNDLE_ID = 'CFBundleIdentifier'
# The name of the iOS app under test i.e: Chrome Canary.
IOS_APP_NAME = 'CFBundleDisplayName'
# The version name of the iOS app under test.
IOS_APP_VERSION = 'CFBundleVersion'

