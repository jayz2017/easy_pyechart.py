# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

python_location_path='D:\\python3\\'
python_file_path='D:\\plg_resource\\'

main_path = python_file_path+'easy_pyechart.py\\easy_pyechart\\_main_.py'
L1=	python_file_path+'easy_pyechart.py\\easy_pyechart'
L2=python_location_path+'DLLs'
L3=	python_location_path+'lib'
L4=python_location_path
L5=python_location_path+'site-packages'
L6=python_location_path+'site-packages\\win32'
L7=python_location_path+'site-packages\\win32\\lib' 
L8=	python_location_path+'site-packages\\Pythonwin'
L9=	python_location_path+'lib\\site-packages'
L10=python_location_path+'Lib\\site-packages\\pyecharts'
L11=python_location_path+'Lib\\site-packages\\pyecharts-2.0.0.dist-info'
L12=python_file_path+'easy_pyechart.py' 
#datas_path = python_location_path+'Lib\\site-packages\\*.*;pyecharts'
a = Analysis(
    [main_path],
    pathex=[
		L1,
		L2, 
		L3,
		L4, 
		L5,
		L6,
		L7, 
		L8,
		L9,
		L10,
		L11,
		L12
	],
    binaries=[],
    datas=[('D:\\python3\\Lib\\site-packages\\*.*', '.\\')],
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
