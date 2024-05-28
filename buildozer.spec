[app]
source.dir = .

# Title of your application
title = ClipboardShare

# Package name
package.name = clipboardshare

# Package domain (needed for Android/iOS packaging)
package.domain = org.example

# Source code where the main.py file is located
source.include_exts = py,kv

# Application versioning (method 1)
version = 0.1

# Application requirements
requirements = python3,kivy,kivymd,requests

# Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# Permissions
android.permissions = INTERNET

# Entry point of the application
entrypoint = main.py

# Supported screen orientations
orientation = portrait

# Indicate whether the application should be fullscreen or not
fullscreen = 1

# List of patterns to include in the application package
source.include_patterns = assets/*,data/*

# List of patterns to exclude from the application package
source.exclude_patterns = tests/*,*.md,*.gitignore

# Presplash screen used for the application
presplash.filename = %(source.dir)s/data/presplash.png

# Title of the window in desktop mode
window.title = ClipboardShare

# The initial window width in pixels (default is 640)
window.width = 720

# The initial window height in pixels (default is 480)
window.height = 1280

# Additional arguments passed to the application
android.add_arguments = --debug
