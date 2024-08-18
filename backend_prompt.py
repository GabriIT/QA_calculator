from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ai', methods=['POST'])
def back():
    data = request.get_json()
    number = data.get('Prompt')

    if not number:
        return jsonify({'error': 'Missing "number" parameter'}), 400

    answer = str(int(number) + 2)
    print(answer)
    return jsonify({'answer': answer}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on port 5001