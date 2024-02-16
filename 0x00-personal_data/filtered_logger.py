#!/usr/bin/env python3
""" Regex module """
import re


def filter_datum(fields, redaction, message, separator):
    """Returns the log message obfuscated """
    new_msg = message
    for field in fields:
        msg = re.sub(rf'(?<={field}=)(.*?)(?={separator})', redaction, new_msg)
    return msg
