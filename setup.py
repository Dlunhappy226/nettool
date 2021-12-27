from setuptools import setup

setup(
    name="nettool",
    version="1.1",
    packages=["nettool"],
    url="https://github.com/Dlunhappy226/nettool",
    license="MIT",
    author="Dlunhappy226",
    author_email="dlunhappy226@gmail.com",
    description="Nettool",
    download_url= "https://github.com/Dlunhappy226/nettool/archive/1.1.tar.gz",
    entry_points = {
        "console_scripts": [
            "nettool = nettool.nettool:main"
        ]
    }
)