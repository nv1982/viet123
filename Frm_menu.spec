# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Frm_menu.py'],
    pathex=[],
    binaries=[],
    datas=[('form_csdl.py', '.'), ('employee_management.py', '.'), ('employee_add.py', '.'), ('db_connection.py', '.'), ('find_form.py', '.')],
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
    name='Frm_menu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['F:\\PYTHON-APP\\PYTHON-GUI\\FORM1\\app_icon.ico'],
)
