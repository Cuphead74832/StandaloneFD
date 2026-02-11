# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Helper function to include folder recursively
def include_folder(folder_name):
    files = []
    if os.path.exists(folder_name):
        for root, dirs, filenames in os.walk(folder_name):
            for f in filenames:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(root, ".")
                files.append((full_path, rel_path))
    return files

datas = []

# =========================
# REQUIRED FILES
# =========================

# Include folders recursively
datas += include_folder("Roblox")
datas += include_folder("AssetCache")

# Include single files if they exist
optional_files = [
    "data.sqlite", 
    "RFD-windows-latest.exe", # NOT OPTIONAL
    "place.png", 
	"GameConfig.toml", 
    "place.rbxl" # NOT OPTIONAL
]

for file in optional_files:
    if os.path.exists(file):
        datas.append((file, "."))

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='StandaloneBlox',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True
)



