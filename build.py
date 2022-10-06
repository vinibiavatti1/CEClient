import os
import shutil
import sys


CURRENT_DIR = sys.path[0]
DEPENDENCIES_PATH = os.path.join(CURRENT_DIR, '.venv', 'Lib', 'site-packages')
BUILD_DIR = os.path.join(sys.path[0], 'dist')

print('Building app...')

# Delete dist dir
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

# Create EXE
os.system(
    f'pyinstaller --noconsole --paths {DEPENDENCIES_PATH} --name ceclient ' +
    f'--onefile src/main.py --icon=resources/icons/ce_icon.ico'
)

# Create dirs
os.mkdir(os.path.join(BUILD_DIR, 'resources'))
os.mkdir(os.path.join(BUILD_DIR, 'data'))

# Copy dir and files
shutil.copyfile(
    os.path.join(CURRENT_DIR, 'src', 'data', 'game.zip'),
    os.path.join(BUILD_DIR, 'data', 'game.zip'),
)
shutil.copyfile(
    os.path.join(CURRENT_DIR, 'src', 'auto_connect.bat'),
    os.path.join(BUILD_DIR, 'auto_connect.bat'),
)
shutil.copytree(
    os.path.join(CURRENT_DIR, 'resources', 'icons'),
    os.path.join(BUILD_DIR, 'resources', 'icons'),
)
shutil.copytree(
    os.path.join(CURRENT_DIR, 'resources', 'images'),
    os.path.join(BUILD_DIR, 'resources', 'images'),
)
shutil.copyfile(
    os.path.join(CURRENT_DIR, 'resources', 'resources.qrc'),
    os.path.join(BUILD_DIR, 'resources', 'resources.qrc'),
)

# Make zip
shutil.make_archive('ceclient', 'zip', BUILD_DIR)
shutil.move(os.path.join(CURRENT_DIR, 'ceclient.zip'), BUILD_DIR)

print('Build successfully!')
