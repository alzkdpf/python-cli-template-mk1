from setuptools import setup

setup(
    name='mycli1',
    version='0.0.1',
    description='cli sample',
    packages=['mycli'],
    author_email='code21032@gmail.com',
    install_requires=[
          'pyCLI',
      ],
    entry_points = {
        'console_scripts':[
            'mycli1 = mycli.__main__:main'
        ]
    }
)