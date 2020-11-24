from flask import Flask, jsonify
import random
app = Flask(__name__)

@app.route('/dossiernum')
def get_numbers():
    num_list = []
    count = 0

    while count < 6:
        num_list.append(random.randint(0,19))
        count += 1
    
    return jsonify({'data':num_list})

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')