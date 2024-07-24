from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bid', methods=['POST'])
def analyze_bid():
    bid_data = request.json
    print(f"Analyzing bid: {bid_data['bid']}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
