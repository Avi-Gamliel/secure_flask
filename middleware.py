from flask import request, jsonify, session
from uuid import uuid4

class SessionMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = environ['werkzeug.request']

        # Skip session validation for login route
        if request.path == '/login':
            return self.app(environ, start_response)

        # Check for session UUID in headers
        session_uuid = request.headers.get('uuid')
        if session_uuid:
            print('has', session_uuid)
            
        session = {}
        # If no session UUID, create one and add it to session
        if 'session_uuid' not in session:
            session_uuid = str(uuid4())
            session['session_uuid'] = session_uuid
        elif session_uuid != session['session_uuid']:
            session_uuid = session['session_uuid']

        # Add or update the session UUID in headers
        environ['HTTP_SESSION_UUID'] = session_uuid

        return self.app(environ, start_response)

