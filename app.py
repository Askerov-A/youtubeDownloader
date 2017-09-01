from flask import Flask, request, render_template, redirect
from youtube_dl import YoutubeDL


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_front_page():
    return render_template('index.html')

@app.route('/getvideo', methods=['POST'])
def get_video():
    videoUrl = YoutubeDL().extract_info(request.form['url'], download=False)["requested_formats"][0]["url"]
    return redirect(videoUrl, code=302)

if __name__ == '__main__':
    app.debug = True
    app.run()
