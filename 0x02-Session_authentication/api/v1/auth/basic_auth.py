#!/usr/bin/env python3
"""Modules of BasicAuth class"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def __init__(self) -> None:
        """init method"""
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header method"""
        if not authorization_header or \
                not isinstance(authorization_header, str):
            return None

        if authorization_header[:6] != 'Basic ':
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header method"""
        if not base64_authorization_header:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials method"""
        if not decoded_base64_authorization_header:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        idx = decoded_base64_authorization_header.find(':')
        email = decoded_base64_authorization_header[:idx]
        pwd = decoded_base64_authorization_header[idx + 1:]
        return (email, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials method"""
        if not user_email or not isinstance(user_email, str):
            return None

        if not user_pwd or not isinstance(user_pwd, str):
            return None

        user = User()
        valid_users = user.search({"email": user_email})

        if valid_users:
            if valid_users[0].is_valid_password(user_pwd):
                return valid_users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        authorization_header = self.authorization_header(request)
        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header)
        decoded = self.decode_base64_authorization_header(
            base64_authorization_header)
        user_credentials = self.extract_user_credentials(decoded)
        user_email = user_credentials[0]
        user_pwd = user_credentials[1]
        return self.user_object_from_credentials(user_email, user_pwd)
