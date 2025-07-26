from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    app.logger.info(f"Greeting requested for: {name}")
    return f'Hello, {name}'

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json(silent=True) or {}
    name = data.get('name')
    if not name or not isinstance(name, str):
        return jsonify({'error': 'Please provide a valid name.'}), 400
    app.logger.info(f"Personalized greeting for: {name}")
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)