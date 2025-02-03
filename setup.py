from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='icommit',
    version='0.2.1',
    description='A CLI tool to generate commit messages from your code changes',
    # package_dir={'app': 'app'},
    packages=find_packages(),
        package_data={
        'app': ['*.py'],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/OMAR-AHMED-SAAD/icommit',
    author = 'Omar Ahmed Saad',
    author_email = 'omarahmedaww@gmail.com',
    license = 'MIT',
    classifiers=[ 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'groq >= 0.15.0',
        'pyperclip >= 1.9.0',
    ],
    extras_require={
        "dev": ["twine >= 6.1.0"]
    },
    python_requires='>=3.9',
     entry_points={
        'console_scripts': [
            'icommit=app.app:run',  
            'icommit-key=app.api_key:set_api_key',  
        ],
    },
)

