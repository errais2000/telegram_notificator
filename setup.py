from setuptools import setup, find_packages



VERSION = '1.0.0'
DESCRIPTION = 'A basic telegram notifications sender.'
LONG_DESCRIPTION = 'Send telegram notifications or alerts from your python programs.'

# Setting up
setup(
    name="TelegramNotificator",
    version=VERSION,
    author="Cryptoroid",
    author_email="",
    license='MIT',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['telegram', 'message', 'notification', 'alert', 'send message', 'telegram message', 'telegram bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)