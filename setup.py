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
        path = Path(os.getcwd()) / 'server' / 'parser' / 'grammar'
        classpath = '.;antlr-4.8-complete.jar'
        command = [
            'java',
            '-cp', classpath,
            'org.antlr.v4.Tool',
            '-Dlanguage=Python3',
            'VerilogParser.g4',
            ]

        subprocess.check_call(
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
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'antlr4-python3-runtime'
    ],
    cmdclass={
        'antlr': AntlrCompile
    }
)
