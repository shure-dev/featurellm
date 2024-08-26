from setuptools import setup, find_packages

setup(
    name='weighted_token_sampler',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'numpy',
        'matplotlib',
        'pillow',
    ],
    author='Yusuke Mikami',
    author_email='your_email@example.com',
    description='A package to generate and analyze images using OpenAI API',
    url='https://github.com/your_username/weighted_token_sampler',
)