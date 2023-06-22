import cx_Freeze


executables = [cx_Freeze.Executable('main.pyw')]

cx_Freeze.setup (
    name = 'DivisorSilabas',
    options = {'build_exe': {'packages': ['PySimpleGUI', 'divisor', 'hyphen', 'abc', 'email', 'smtplib'],
                             'include_files': ['files']}},
    executables = executables
)
