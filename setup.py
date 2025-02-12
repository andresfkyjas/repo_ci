from setuptools import setup, find_packages

setup(
    name='json_to_excel',
    version='1.0.0',
    description='Convierte un archivo JSON a Excel utilizando pandas.',
    author='Andrés Felipe Callejas Jaramillo',
    author_email='andres.callejas@iudigital.edu.co',
    packages=find_packages(),
    py_modules=['script'],
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'json_to_excel=script:main',
        ],
    },
)