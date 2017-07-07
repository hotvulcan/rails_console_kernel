#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install import install
from distutils import log

import json
import os
import sys

kernel_json = { 'argv': ['python', '-m' ,'ipython_mysql_kernel',
                         '-f', '{connection_file}'],
                'display_name': 'rails_console',
                'language': 'ruby',
               }

# this code from bash_kernel made by Thomas Kluyver
# (https://github.com/takluyver/bash_kernel)
class install_with_kernelspec(install):
    def run(self):
        # Regular installation
        install.run(self)

        # Now write the kernelspec
        from IPython.kernel.kernelspec import install_kernel_spec
        from IPython.utils.tempdir import TemporaryDirectory
        with TemporaryDirectory() as td:
            os.chmod(td, 0o755) # Starts off as 700, not user readable
            with open(os.path.join(td, 'kernel.json'), 'w') as f:
                json.dump(kernel_json, f, sort_keys=True)
            # TODO: Copy resources once they're specified

            log.info('Installing IPython kernel spec')
            install_kernel_spec(td, 'rails_console_kernel', user=self.user, replace=True)

with open('README.md','r') as f:
    readme = f.read()

svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
    sys.argv.remove(svem_flag)

setup(name='ipython_rails_console_kernel',
      version='0.1',
      description='A Rails Console kernel for IPython',
      long_description=readme,
      author='Sooo',
      author_email='hotvulcan@gmail.com',
      url='https://github.com/hotvulcan/rails_console_kernel',
      packages=['rails_console_kernel'],
      cmdclass={'install': install_with_kernelspec},
      install_requires=['pexpect>=3.3'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Shells :: Rails',
      ]
)

