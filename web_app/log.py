# pylint: disable=too-few-public-methods
import logging
import os


class SyslogFilter(logging.Filter):
    """
    Sys log filter
    """
    hostname = os.getenv('HOSTNAME')

    def filter(self, record):
        record.hostname = SyslogFilter.hostname
        return True


class ColoredFormatter(logging.Formatter):
    """
    Colored formatter
    """
    COLOR_MAPPING = {
        'INFO': '\33[32m',
        'WARNING': '\33[33m',
        'CRITICAL': '\33[35m',
        'ERROR': '\33[31m'
    }

    def format(self, record):
        time = self.formatTime(record)
        level = record.levelname
        line = record.lineno
        color = self.COLOR_MAPPING.get(level) or '\33[34m'  # blue
        default_color = '\33[0m'
        msg = str(record.msg)
        if record.args:
            msg = msg % record.args
        return f'{color}{time} {level}\n{record.pathname} line {line}{default_color}\n{msg}\n'
