from distutils.core import setup

setup(
    name='tsl_email_utils',
    version='0.1.0',
    author='Francesco Pischedda',
    author_email='francesco.pischedda@gmail.com',
    packages=['tsl_email_utils'],
    license='LICENSE.md',
    description='Provides some utilities to interact with an imap server.',
    long_description=open('README.md').read(),
    install_requires=[
        "imbox",
    ],
)
