[app]

title = TdG
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = spec,py,kv,png
version = 0.1
requirements = python3,kivy,kivymd,pandas,plyer,sqlalchemy,datetime,psycopg2,pillow,pygments
orientation = portrait
fullscreen = 0
presplash.filename = images/splash.png
icon.filename = images/icon.png
android.permissions = INTERNET, GPS
android.archs = arm64-v8a, armeabi-v7a



[buildozer]

log_level = 2
warn_on_root = 1