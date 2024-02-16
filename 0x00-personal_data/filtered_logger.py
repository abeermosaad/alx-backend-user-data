#!/usr/bin/env python3
""" Regex module """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: List[str], separator) -> str:
    """Returns the log message obfuscated """
    new_msg = message
    for field in fields:
        msg = re.sub(rf'(?<={field}=)(.*?)(?={separator})', redaction, new_msg)
    return msg
