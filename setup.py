# Copyright 2016-2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For general information on the Pynini grammar compilation library, see
# pynini.opengrm.org.
"""Setup for Pynini."""

import os
import pathlib
import subprocess
import sys

from Cython.Build import cythonize
from setuptools import Extension
from setuptools import find_packages
from setuptools import setup

LIBRARIES = ["fstfarscript", "fstfar", "fstscript", "fst"]
LINKER_ARGS = None

if sys.platform.startswith("win32"):
    COMPILE_ARGS = [
        "/std:c++17"
    ]
    LINKER_ARGS = [
        "/WHOLEARCHIVE:fstfarscript",
        "/WHOLEARCHIVE:fstfar",
        "/WHOLEARCHIVE:fstscript",
        "/WHOLEARCHIVE:fst"
    ]
    openfst_dir = os.path.join(os.path.dirname(__file__),
                               "third_party", "openfst")
    include_dirs = [os.path.join(openfst_dir, "Release", "include")]
    library_dirs = [os.path.join(openfst_dir, "Release", "lib")]
else:
    LIBRARIES.extend(["m", "dl"])
    COMPILE_ARGS = [
        "-std=c++17",
        "-Wno-register",
        "-Wno-deprecated-declarations",
        "-Wno-unused-function",
        "-Wno-unused-local-typedefs",
        "-funsigned-char",
    ]
    include_dirs = None
    library_dirs = None

if sys.platform.startswith("darwin"):
    COMPILE_ARGS.append("-stdlib=libc++")
    COMPILE_ARGS.append("-mmacosx-version-min=10.12")

pywrapfst = Extension(
    name="_pywrapfst",
    language="c++",
    extra_compile_args=COMPILE_ARGS,
    extra_link_args=LINKER_ARGS,
    libraries=LIBRARIES,
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    sources=["extensions/_pywrapfst.pyx"],
)
pynini = Extension(
    name="_pynini",
    language="c++",
    extra_compile_args=COMPILE_ARGS,
    extra_link_args=LINKER_ARGS,
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    libraries=["fstmpdtscript", "fstpdtscript"] + LIBRARIES,
    sources=[
        "extensions/_pynini.pyx",
        "extensions/cdrewritescript.cc",
        "extensions/concatrangescript.cc",
        "extensions/crossscript.cc",
        "extensions/defaults.cc",
        "extensions/getters.cc",
        "extensions/lenientlycomposescript.cc",
        "extensions/optimizescript.cc",
        "extensions/pathsscript.cc",
        "extensions/stringcompile.cc",
        "extensions/stringcompilescript.cc",
        "extensions/stringfile.cc",
        "extensions/stringmapscript.cc",
        "extensions/stringprintscript.cc",
        "extensions/stringutil.cc",
    ],
)


this_directory = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
with (this_directory / "README.md").open(encoding="utf8") as source:
    long_description = source.read()


def get_version(rel_path):
    # Searches through a file to find a `__version__ = "X.Y.Z"` string.
    # From https://packaging.python.org/guides/single-sourcing-package-version/.
    with (this_directory / rel_path).open(encoding="utf8") as fp:
        for line in fp:
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")

__version__ = get_version("pynini/__init__.py")


def compute_num_jobs():
    num_jobs = os.environ.get("MAX_JOBS", None)
    if num_jobs is not None:
        num_jobs = int(num_jobs)
    else:
        try:
            num_jobs = len(os.sched_getaffinity(0))
        except AttributeError:
            num_jobs = os.cpu_count()
    return num_jobs


def build_openfst():
    num_jobs = compute_num_jobs()

    subprocess.check_call(["git", "submodule", "update", "--init", "--recursive"], cwd=os.path.dirname(__file__))

    build_args = [
        "-G",
        "Ninja",
        "-DCMAKE_INSTALL_PREFIX:PATH=../Release",
        "-DCMAKE_BUILD_TYPE=Release",
        "-DBUILD_SHARED_LIBS=OFF",
        "-DHAVE_BIN=OFF",
        "-DHAVE_TEST=OFF",
        "-B", "build",
        "."
    ]
    subprocess.check_call(["cmake", *build_args], cwd=openfst_dir)

    install_args = [
        "--build",
        "build",
        "--target",
        "install",
        "--config",
        "Release",
        "-j", str(num_jobs)
    ]
    subprocess.check_call(["cmake", *install_args], cwd=openfst_dir)


def main() -> None:
    if sys.platform.startswith("win32"):
        build_openfst()
    setup(
        name="pynini",
        version=__version__,
        author="Kyle Gorman",
        author_email="kbg@google.com",
        description="Finite-state grammar compilation",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="http://pynini.opengrm.org",
        keywords=[
            "computational linguistics",
            "natural language processing",
            "speech recognition",
            "machine learning",
        ],
        classifiers=[
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Development Status :: 5 - Production/Stable",
            "Environment :: Other Environment",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Text Processing :: Linguistic",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Mathematics",
        ],
        license="Apache 2.0",
        ext_modules=cythonize([pywrapfst, pynini]),
        packages=find_packages(exclude=["scripts", "tests"]),
        package_data={
            "pywrapfst": ["__init__.pyi", "py.typed"],
            "pynini": ["__init__.pyi", "py.typed"],
            "pynini.examples": ["py.typed"],
            "pynini.export": ["py.typed"],
            "pynini.lib": ["py.typed"],
        },
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
