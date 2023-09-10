from flask import Flask, request
from flask_cors import CORS
from openaiapi import chat_completion

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/verbose', methods=['POST'])
def verbose():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("clearer to understand", sentence)} )


@app.route('/concise', methods=['POST'])
def concise():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("less wordy and easier to read", sentence)} )
    

@app.route('/rectify', methods=['POST'])
def rectify():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("grammatically correct", sentence)} )
    
    
@app.route('/formalize', methods=['POST'])
def formalize():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("formalize", sentence)} )


if __name__ == "__main__":
    app.run(debug=True, port=8000)