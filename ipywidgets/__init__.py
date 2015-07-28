import os

from IPython import get_ipython
from .widgets import *


def find_static_assets():
    """Return the path to static assets for widgets (js, css)"""
    here = os.path.abspath(__file__)
    return os.path.join(os.path.dirname(path), 'static')


def load_ipython_extension(ip):
    """Set up IPython to work with widgets"""
    if not hasattr(ip, 'kernel'):
        return
    register_comm_target(ip.kernel)


def register_comm_target(kernel=None):
    """Register the ipython.widget comm target"""
    if kernel is None:
        ip = get_ipython().kernel
    kernel.comm_manager.register_target('ipython.widget', Widget.handle_comm_opened)

# deprecated alias
handle_kernel = register_comm_target

def _handle_ipython():
    """register with the comm target at import if running in IPython"""
    ip = get_ipython()
    if ip is None:
        return
    load_ipython_extension(ip)

_handle_ipython()
