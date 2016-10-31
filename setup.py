try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Controle de Lojas Assistencia Tecnica',
    'author': 'Ricardo Portela',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ricaportela@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['app'],
    'scripts': [],
    'name': 'assistenciatecnica'
}

setup(**config)
