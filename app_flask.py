from flask import Flask,render_template, request
import twitterAPI, map_generator


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map', methods=['POST', 'GET'])
def map_friend():
    nickname = request.form['name']
    twitterAPI.generate(nickname)
    map_generator.main()
    return render_template('Map.html')


if __name__ == '__main__':
    app.run(debug=True)