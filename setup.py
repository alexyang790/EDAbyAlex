from setup import setup, find_packages

setup(
    name="edabyalex", 
    version="0.1.0",  
    author="Zhe Yang",
    author_email="zy7ts@virginia.edu",
    description="A Python package for data extraction and analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alexyang790/EDAbyAlex",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "glob2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)