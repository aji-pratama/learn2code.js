import contextlib
import sys
from io import StringIO
from js2py import eval_js, PyJsException


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def exec_js(toexec):
    result = {'success': False, 'output': None}
    with stdoutIO() as s:
        try:
            eval_js(toexec)
            output = s.getvalue().replace("'", '').replace('"', '').strip() or None
            result = {
                'success': True,
                'output': output
            }
            return result

        except PyJsException as err:
            print(err)
            output = s.getvalue().replace("'", '').replace('"', '').strip() or None
            result['output'] = output
            return result
