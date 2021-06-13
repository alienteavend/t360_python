from io import StringIO 
import sys
from IPython.core.magic import (Magics, magics_class, line_magic)


class PrintingStringIO(StringIO):
    def __init__(self, stdout, *args, **kwargs):
        super(PrintingStringIO, self).__init__(*args, **kwargs)
        self._stdout = stdout

    def write(self, *args, **kwargs):
        super(PrintingStringIO, self).write(*args, **kwargs)
        sys.stdout = self._stdout
        print(*args, end='', flush=True)
        sys.stdout = self


@magics_class
class Training360Testloader(Magics):
    def __init__(self, shell, data):
        super(Training360Testloader, self).__init__(shell)
        self.shell = shell
        self.solution = data
        self._stringio = None
        self._stdout = None

    def pre_run_cell(self, info):
        if '= %solution' in info.raw_cell:
            return

        self.solution = []
        self._stdout = sys.stdout
        sys.stdout = self._stringio = PrintingStringIO(self._stdout)

    def post_run_cell(self, result):
        if '= %solution' in result.info.raw_cell:
            return

        self.solution.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

    @line_magic
    def solution(self, line):
        return self.solution
        

solution = []


def load_ipython_extension(ip):
    test_loader = Training360Testloader(ip, solution)
    ip.events.register('pre_run_cell', test_loader.pre_run_cell)
    ip.events.register('post_run_cell', test_loader.post_run_cell)
    ip.register_magics(test_loader)