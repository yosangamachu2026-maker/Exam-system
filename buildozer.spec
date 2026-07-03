[app]
title = ExamSystem
package.name = examsystem
package.domain = org.gamachu

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# permissions (basic only)
android.permissions = INTERNET

# performance / stability
log_level = 2
warn_on_root = 1

[buildozer]