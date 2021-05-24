from setuptools import find_packages, setup

setup(
    name="lisa",
    version="0.2.0",
    description="簡短的描述",
    long_description="詳細的描述",
    long_description_content_type='text',
    author="Lisa",
    author_email="lisalin0601@gmail.com",
    url="https://github.com/Lisa06010416/PythonPackaging",

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    install_requires=["requests"],
    # 可以在cmd下直接執行的檔案
    scripts=['bin/script1'],
    entry_points={
        'console_scripts': ['script1=package_a.cmdline:script1_entry_point'],
    },

    classifiers={
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Environment :: MacOS X",
        "Programming Language :: Python",
    }
)
