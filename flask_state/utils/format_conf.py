import os
import platform


def format_sec(secs):
    """
    Format incoming time
    :param secs: initial time
    :return: format time
    """
    if not isinstance(secs, int) or secs < 10:
        return 60
    else:
        return secs


def format_address(address):
    """
    Format incoming database address
    :param address: initial database address
    :return: format database address
    """
    if not isinstance(address, str):
        address = str(address)
    if platform.system() == 'Windows':
        index = max(address.rfind('\\'), address.rfind('/'))
    else:
        index = address.rfind('/')
    if os.access(address[:index] if index != -1 else './', os.W_OK):
        path = address
    else:
        path = './'
    return 'sqlite:///' + path
