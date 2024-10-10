# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files


tcl_tk_data = collect_data_files('tkinter')

a = Analysis(
    ['../../screenvivid/main.py'],
    pathex=[],
    binaries=[('ffmpeg', '.')],
    datas=[
        ('../../screenvivid/resources/images/wallpapers/hires', 'resources/images/wallpapers/hires'),
        ('../../screenvivid/resources/images/cursor/macos', 'resources/images/cursor/macos'),
        ('../../screenvivid/resources/images/cursor/default', 'resources/images/cursor/default'),
        ('../../screenvivid/resources/icons/screenvivid.ico', 'resources/icons/'),
        *tcl_tk_data,
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ScreenVivid',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="../../resources/icons/screenvivid.ico"
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ScreenVivid',
)

app = BUNDLE(
    coll,
    name="ScreenVivid.app",
    icon="../../screenvivid/resources/icons/screenvivid.icns",
    bundle_identifier="com.darkphoton.ScreenVivid",
    bundle_description="ScreenVivid is a cross-platform desktop application for screen recording and video editing, featuring options like background replacement and padding.",
)