from setuptools import setup, find_packages

setup(
    name='emotion_detection',
    version='1.0.0',
    description='Emotion Detection web app using Watson NLP',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'ibm-watson',
        'pytest',
        'pylint'
    ],
    python_requires='>=3.6'
)from setuptools import setup, find_packages

