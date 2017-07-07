# Rails Console kernel for IPython

![screenshot](https://raw.githubusercontent.com/wiki/mmisono/ipython_mysql_kernel/images/screenshot.png "screenshot")

This Kernel inspect by mmisono/ipython_mysql_kernel the initial codes is copied directly from it.
This requires IPython 3, pexpect.  
This kernel interact with [Rails Console]( http://guides.rubyonrails.org/command_line.html ) via
[pexpect](https://github.com/pexpect/pexpect).

## Install
* todo: Use pip: `pip install git+https://github.com/hotvulcan/rails_console_kernel`
* Checkout the source: `git clone
  https://github.com/hotvulcan/rails_console_kernel` then `python setup.py`

If you use `pip` or `python setup.py`, kernel files are created at ipython's
kernel directory.
(see [docs](https://ipython.org/ipython-doc/dev/development/kernels.html#kernelspecs)
for more detail).
Please don't forget to remove these files when uninstall this.

## Usage
`jupyter console --kernel rails_console` or `jupyter notebook` then select rails console kernel.

## License
new BSD license
