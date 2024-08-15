from flask import Flask, request, jsonify

app = Flask(__name__)

# GET /
@app.route('/', methods=['GET'])
def home():
    """Return  JSON response when GET request."""
    return jsonify({"msg": "BC4M"})

# GET /health
@app.route('/health', methods=['GET'])
def health():
    """Return health status JSON response for health check endpoint."""
    return jsonify({"status": "healthy"})

# POST /echo
@app.route('/echo', methods=['POST'])
def echo():
    """Echo back the JSON received in the request body."""
    data = request.json
    return jsonify(data)

#  useful for local development.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
