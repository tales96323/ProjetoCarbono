#setup.py
from setuptools import setup, find_packages

setup(
    name='carbon-monitoring-saas',
    version='0.1',
    description='SaaS para monitoramento de carbono e sustentabilidade',
    author='Tales Santos',
    author_email='tales96323@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask',
        'pytest',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'monitor-carbon=main:run',  # Exemplo de entrada para CLI
        ],
    },
)