from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        author='Matthew Collins',
        author_email='mcollin4@citadel.edu',
        description='A utility for backing up PostgreSQL databases.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/mcollinsece/pgbackup.git',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=['boto3'],
        python_requires='>=3.6',
        entry_points={
            'console_scripts': [
            'pgbackup=pgbackup.cli:main',
            ],
        }
        )



