#!/usr/bin/env python

import json
import os
import re
import signal

from IPython.kernel.zmq.kernelbase import Kernel
import pexpect

class RailsConsole(Kernel):
    implementation = 'RailsConsole'
    implementation_version = '0.1'
    language = 'ruby'
    language_version = '0.1'
    language_info = {
            'mimetype': 'text/plain',
            'name': 'rails_console',
            'file_extension': '.rb',
            }
    banner = "Rails Console kernel"
    settings = {}

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)

        self.prompt = '>'
        self._start_process()
    
    def _start_process(self):
        # make childprocess interuptible by SIGINT
        sig = signal.signal(signal.SIGINT, signal.SIG_DFL)
        try:
            self.ch =  pexpect.spawn("rails console")
            
        finally:
            signal.signal(signal.SIGINT, sig)

        if self.ch.echo:
            self.ch.setecho(False)
            self.ch.waitnoecho()

        self.ch.expect(self.prompt)    

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        """Send code to rails console via pexpect and get result
        """
        error_msg = []

        if not code.strip():
            return {'status': 'ok',
                    'execution_count': self.execution_count,
                    'payload': [],
                    'user_expressions': {}}
        code = code.strip()
        interrupted = False
        try:
            self.ch.sendline(code)
            self.ch.expect(self.prompt)
            output = self.ch.before
        except KeyboardInterrupt:
            self.ch.sendintr()
            self.ch.expect(self.prompt)
            interrupted = True
            output = self.ch.before
        except pexpect.EOF:
            output = self.ch.before + 'Restarting Process...'
            self._start_process()

        if interrupted:
            return {'status': 'abort', 'execution_count': self.execution_count}

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_complete(self, code, cursor_pos):
        default = {'matches': [], 'cursor_start': 0,
                   'cursor_end': cursor_pos, 'metadata': dict(),
                   'status': 'ok'}
        #todo change default content here
        return default

if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=MySQLKernel)
