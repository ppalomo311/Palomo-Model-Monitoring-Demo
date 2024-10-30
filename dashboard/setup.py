from setuptools import setup, find_packages

setup(
    name='modelMonitoring',
    python_requires='>=3.10.0',
    version='0.0.1',
    description='Monitoring compliance models with Cognition datalabs API',
    long_description='',
    url='',
    author='Kevin Keenan',
    author_email='kevin.keenan@smarsh.com',
    license='',
    packages=find_packages(where="."),
    include_package_data=True,
    package_dir={
        '': './',
        'img': 'modelMonitoring/img'
    },
    package_data={
        '': ['*.svg', '*.png', '*.jpg'],
    },
    install_requires=[
        'streamlit', 
        'click',
        'plotly',
        'pandas',
    ],
    zip_safe=False,  # install source files not egg
    entry_points={
        'console_scripts': [
            'modelMonitoring=modelMonitoring.cli:main'
        ]
    },
)