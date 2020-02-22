"""Tools for reading and writing PKG-INFO / METADATA without caring
about the encoding."""

from email.parser import Parser
from email.generator import Generator


def read_pkg_info_bytes(bytestr):
    return Parser().parsestr(bytestr)


def read_pkg_info(path):
    with open(path, "r") as headers:
        message = Parser().parse(headers)
    return message


def write_pkg_info(path, message):
    with open(path, 'w') as metadata:
        Generator(metadata, mangle_from_=False, maxheaderlen=0).flatten(message)
