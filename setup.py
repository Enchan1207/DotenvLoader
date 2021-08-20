#
# setup script
#

import glob
import setuptools, os

setuptools.setup(
    name="DotenvLoader",
    version="1.0.0",
    license="MIT Licence",
    description="dotenv file (.env) loader",
    author="Enchan1207",
    url="https://github.com/Enchan1207/DotenvLoader",
    packages=setuptools.find_packages("src"),
    install_requires=["python-dotenv"],
    package_dir={"": "src"},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')],
    include_package_data=True,
    zip_safe=False
)