# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['fortuneWheel.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
    a.binaries,
    a.datas,
    [],
    name='fortuneWheel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Disabilita UPX
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\icon.ico'],
)


import shutil
shutil.copyfile('fortuneWheel.json', '{0}/fortuneWheel.json'.format(DISTPATH))