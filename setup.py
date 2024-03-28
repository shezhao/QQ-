from cx_Freeze import setup, Executable

executables = [
    Executable('main.py', base='Win32GUI', icon='favicon.ico')
]

includes = ['menu.ui', 'qq.ui', 'phone.ui', 'web.ui']

build_exe_options = {
    'include_files': includes
}

setup(name='QQtoPhone',
      version='1.0',
      description='find_qq_to_phone_number',
      options={'build_exe': build_exe_options},
      executables=executables)