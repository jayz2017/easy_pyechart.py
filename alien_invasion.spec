# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\haochenhu\\Documents\\easy_pyechart.py\\easy_pyechart\\_main_.py'],
    pathex=[
		'c:\\Users\\haochenhu\\Documents\\easy_pyechart.py\\easy_pyechart',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\lib',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37', 
		'C:\\Users\\haochenhu\\AppData\\Roaming\\Python\\Python37\\site-packages',
		'C:\\Users\\haochenhu\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32',
		'C:\\Users\\haochenhu\\AppData\\Roaming\\Python\\Python37\\site-packages\\win32\\lib', 
		'C:\\Users\\haochenhu\\AppData\\Roaming\\Python\\Python37\\site-packages\\Pythonwin',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pyecharts',
		'C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pyecharts-2.0.0.dist-info',
		'c:\\Users\\haochenhu\\Documents\\easy_pyechart.py'
	],
    binaries=[],
    datas=['C:\\Users\\haochenhu\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\*.*;pyecharts'],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='alien_invasion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='alien_invasion',
)
