from setuptools import setup, find_packages


# Setting up
setup(
    name="TelegramNotificator",
    version='1.0.4',
    author="Cryptoroid",
    author_email="",
    license='MIT',
    description='A basic telegram notifications sender.',
    long_description_content_type="text/markdown",
    long_description='Send telegram notifications or alerts from your python programs.',
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