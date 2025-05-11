# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

# Include mediapipe runtime data
mediapipe_data = collect_data_files(
    'mediapipe',
    includes=['**/*.tflite', '**/*.pbtxt', '**/*.binarypb', '**/*.json'],
)

a = Analysis(
    ['run.py'],  # Entry point
    pathex=[],
    binaries=[],
    datas=mediapipe_data + [
        ('alert.wav', '.'),  # include sound file
        ('templates/index.html', 'templates'),  # include HTML file
    ],
    hiddenimports=[
        'mediapipe.python._framework_bindings',
        'mediapipe.python.solutions.pose',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # set to True if you want a debug window
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
    name='run'
)

app = BUNDLE(
    coll,
    name='run',
    icon=None,
    onefile=True  # <-- this creates a single .exe
)
