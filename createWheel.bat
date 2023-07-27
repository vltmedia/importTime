rmdir /s /q dist

call python.exe setup.py bdist_wheel --universal

call pip.exe install dist\importTime-1.0.0-py2.py3-none-any.whl --force-reinstall --upgrade