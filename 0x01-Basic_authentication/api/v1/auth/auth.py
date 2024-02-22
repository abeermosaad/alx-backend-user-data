#!/usr/bin/env python3
"""Modules of Auth class"""
from flask import request
from typing import List, TypeVar


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
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None
