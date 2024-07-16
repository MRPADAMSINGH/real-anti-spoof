from setuptools import setup, find_packages

setup(
    name='real-anti-spoof',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'opencv-python',
        'numpy'
    ],
    description='A library for anti-spoofing and streaming',
    author='Padam Singh',
    author_email='padam4030@gmail.com',
    url='https://github.com/MRPADAMSINGH/real-anti-spoof',  # Update this with your repo URL
)
