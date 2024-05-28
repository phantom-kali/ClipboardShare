[app]
# (str) Title of your application
title = ClipboardShare

# (str) Package name
package.name = clipboardshare

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,kv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,requests

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
android.permissions = INTERNET

# (str) Entry point of the application
entrypoint = main.py

# (str) Supported screen orientations
orientation = portrait

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 1

# (list) List of patterns to include in the application package
source.include_patterns = assets/*,data/*

# (list) List of patterns to exclude from the application package
source.exclude_patterns = tests/*,*.md,*.gitignore

# (str) Presplash screen used for the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Title of the window in the desktop mode
window.title = ClipboardShare

# (int) The initial window width in pixels (default is 640)
window.width = 720

# (int) The initial window height in pixels (default is 480)
window.height = 1280

# (str) Additional arguments passed to the application
android.add_arguments = --debug
