import setuptools
import distutils
import subprocess
import os
from pathlib import Path


with open('README.md', 'r') as fh:
    long_description = fh.read()


class AntlrCompile(distutils.cmd.Command):
    description = 'Compile ANTLR4 grammar'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        path = Path(os.getcwd()) / 'verilog_langserver' / 'verilog_parser' / 'grammar'
        classpath = '.;antlr-4.8-complete.jar'
        command = [
            'java',
            '-cp', classpath,
            'org.antlr.v4.Tool',
            '-Dlanguage=Python3',
            '-visitor',
            '-o', str(path.parent / 'antlr_build'),
            'SystemVerilog.g4'
            ]
        subprocess.call(
            command,
            cwd=str(path),
        )


setuptools.setup(
    name='verilog-langserver',
    version='0.1',
    author='Eirik Prestegårdshus',
    author_email='eirikpre@gmail.com',
    description='Language server for Verilog/SystemVerilog',
    long_description=long_description,
    url='https://github.com/eirikpre/verilog-langserver',
    packages=setuptools.find_packages(
        exclude=['test', 'docs']
    ),
    python_requires='>=3.7',
    install_requires=[
        'antlr4-python3-runtime',
        'pygls'
    ],
    cmdclass={
        'antlr': AntlrCompile
    }
)
