import contextlib
import sys
from io import StringIO
from js2py import eval_js


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


# TODO: Adjust based on data type
def sandbox(toexec):
    response = {'success': False, 'result': None}
    with stdoutIO() as s:
        try:
            eval_js(toexec)
            result = s.getvalue().replace("'", '').replace('"', '').strip() or None
            response = {
                'success': True,
                'result': result
            }
            return response

        except Exception as e:
            response['result'] = e
            return response
