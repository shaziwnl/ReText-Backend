from flask import Flask, request
from waitress import serve
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
        return ( {"completion" : chat_completion("You are a writing assistant that adds detail to texts. Add details to the following text", sentence)} )


@app.route('/concise', methods=['POST'])
def concise():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("You are a writing assistant that helps make texts more concise. Make the following text more concise", sentence)} )
    

@app.route('/rectify', methods=['POST'])
def rectify():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("You are a writing assistant that helps the user with correcting grammatical mistakes in their text. Correct the mistakes in the following text", sentence)} )
    
    
@app.route('/formalize', methods=['POST'])
def formalize():
    if request.method == 'POST':
        sentence = request.get_json().get('sentence')
        # return jsonify({"sentence": sentence})
        return ( {"completion" : chat_completion("I need to send a message to my boss. Please make the following message more formal", sentence)} )


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=50100, threads=4)
    # app.run(debug=True, port=8000)
