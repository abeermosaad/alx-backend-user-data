#!/usr/bin/env python3
"""Modules of SessionAuth class"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def __init__(self) -> None:
        """init method"""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """create_session method"""
        if not user_id:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
