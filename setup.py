from setuptools import setup, find_packages

setup(
    name="AutoBotsGenerator",
    version="1.0.0",
    author="ChauhanDun Industries",
    description="Modular Telegram bot platform with licensing, vault, and multilingual support",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psycopg2",
        "cx_Oracle",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "autobots-launcher = main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
    ]
)