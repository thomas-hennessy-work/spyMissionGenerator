from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

@app.route('/dossierletter)
def get_letters():

    char_list = []
    letter_list = string.ascii_lowercase
    count = 0

    while count < 6:
        char_list.append(random.choice(letter_list))
        count += 1

    return jsonify({data:char_list})

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')
