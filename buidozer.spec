[app]

# (str) Title of your application
title = ProCalc

# (str) Package name
package.name = procalc

# (str) Package domain (needed for android packaging)
package.domain = org.procalc

# (list) Source files to include (let it be empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) Source files to exclude (let it be empty to exclude none)
source.exclude_exts = spec

# (list) List of directory to exclude (let it be empty to exclude none)
source.exclude_dirs = tests bin venv .git .github

# (list) List of inclusions
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,plyer,android,certifi,urllib3

# (str) Custom source folders for requirements
#requirements.source.dir = ../local_requirements

# (list) Permissions
android.permissions = VIBRATE,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
android.ant_path =

# (bool) Use --private data storage (True) or --public storage (False)
android.private_storage = True

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
#android.services = 

#
# iOS specific
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/kivy-ios
ios.minsdk = 12.0
