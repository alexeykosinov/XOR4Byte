from setuptools import setup

setup(
    name='xor4byte',
    version='1.0',
    py_modules=['xor4byte'],
    install_requires=['Click','progress'],
    entry_points='''
        [console_scripts]
        xor4byte=xor4byte:f
    ''',
)