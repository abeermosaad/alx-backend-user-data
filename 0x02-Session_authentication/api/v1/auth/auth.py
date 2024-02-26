#!/usr/bin/env python3
"""Modules of Auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """Auth class"""

    def __init__(self) -> None:
        """init method"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None:
            return True

        if path in excluded_paths or f'{path}/' in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if excluded_path[:-1] in path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        if not request or 'authorization' not in request.headers:
            return None
        return request.headers['authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None

    def session_cookie(self, request=None):
        """session_cookie method"""
        if not request:
            return None

        session_name = getenv('SESSION_NAME')
        if session_name:
            return request.cookies.get(session_name)
        return None
