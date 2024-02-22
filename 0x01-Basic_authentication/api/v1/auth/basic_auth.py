#!/usr/bin/env python3
"""Modules of BasicAuth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class"""

    def __init__(self) -> None:
        """init method"""
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if not authorization_header or \
                not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
