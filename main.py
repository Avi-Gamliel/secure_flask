from flask import Flask, request, jsonify, session, render_template
from uuid import uuid4
from middleware import SessionMiddleware

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session management

app.wsgi_app = SessionMiddleware(app.wsgi_app)
@app.route('/')
def index():
    print( request.headers.get('Session-UUID'))
    return jsonify({"msg": "success"})
@app.route('/login', methods=['POST'])
def login():
    user = request.json.get('user')
    password = request.json.get('password')

    # Here you would check the user credentials (this is just a placeholder)
    if user == 'test' and password == 'test':
        session_uuid = str(uuid4())
        session['session_uuid'] = session_uuid
        return jsonify({'message': 'Login successful', 'session_uuid': session_uuid}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
def protected():
    session_uuid = request.headers.get('Session-UUID')
    return jsonify({'message': 'This is a protected route', 'session_uuid': session_uuid}), 200

if __name__ == '__main__':
    app.run(debug=True)
