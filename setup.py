import numpy

from setuptools import setup, find_packages
from Cython.Distutils.extension import Extension
from Cython.Distutils import build_ext
import sys



if sys.platform == 'darwin':
    ext_modules = [Extension(
        name="fasttsne",
        sources=["fasttsne/orig-lvdm/quadtree.cpp",
                 "fasttsne/orig-lvdm/tsne.cpp", "fasttsne/fasttsne.pyx"],
        include_dirs=[numpy.get_include(), "fasttsne/orig-lvdm/"],
        extra_compile_args=[
            '-faltivec', '-I/System/Library/Frameworks/vecLib.framework/Headers'],
        extra_link_args=["-Wl,-framework", "-Wl,Accelerate", "-lcblas"],
        language="c++"
    )]
else:
    ext_modules = [Extension(
        name="fasttsne.fasttsne",
        sources=["fasttsne/orig-lvdm/quadtree.cpp",
                 "fasttsne/orig-lvdm/tsne.cpp", "fasttsne/fasttsne.pyx"],
        include_dirs=[numpy.get_include(),
                      "/home/dmitry/miniconda/pkgs/openblas-0.2.14-1/include",
                       "/usr/local/include", "fasttsne/orig-lvdm/"],
        library_dirs=["/usr/local/lib"],
        extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
        extra_link_args=["-lopenblas"],
       # data_files=["fasttsne/__init__.py"],
        language="c++"
    )]

setup(
    name="fasttsne",
    packages=find_packages(),
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)
