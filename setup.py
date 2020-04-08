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
        base_path = str(Path(os.getcwd()) / 'verilog_langserver' / 'verilog_parser')
        base_cmd = 'java -cp antlr-4.8-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 '

        diagnosis_cmd = base_cmd + f'-o  {base_path}/antlr_build/diagnosis {base_path}/grammar/diagnosis/SystemVerilog.g4'
        symbol_cmd = base_cmd + f'-visitor -o {base_path}/antlr_build {base_path}/grammar/SystemVerilogSymbol.g4'

        for cmd in [diagnosis_cmd, symbol_cmd]:
            subprocess.check_call(
                cmd.split()
            )


setuptools.setup(
    name='verilog-langserver',
    version='0.1',
    author='Eirik Prestegårdshus',
    author_email='eirikpre@gmail.com',
    description='Language Server for Verilog/SystemVerilog',
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
