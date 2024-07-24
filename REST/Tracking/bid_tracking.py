from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/bid', methods=['POST'])
def track_bid():
    bid_data = request.json
    print(f"Tracking bid: {bid_data['bid']}")
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
