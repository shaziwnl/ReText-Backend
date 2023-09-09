from flask import Flask, request
from openaiapi import chat_completion

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/restructure', methods=['POST'])
def restructure():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("restructure", sentence)} )

@app.route('/rectify', methods=['POST'])
def rectify():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("correct the grammar of", sentence)} )


if __name__ == "__main__":
    app.run(debug=True, port=8000)