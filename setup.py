from setuptools import setup, find_packages

setup(
    name='run_date_info_gen',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'run_date_info = run_date_info_gen.cli:generate'
        ]
    },
    install_requires=[
        'click'
    ]
)
