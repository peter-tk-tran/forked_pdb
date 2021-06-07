import sys
import pdb


class ForkedPdb(pdb.Pdb):
    """https://stackoverflow.com/questions/4716533/how-to-attach-debugger-to-a-python-subproccess
    A Pdb subclass that may be used from a forked multiprocessing child."""

    def interaction(self, *args, **kwargs):
        _stdin = sys.stdin
        try:
            sys.stdin = open("/dev/stdin")
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = _stdin
