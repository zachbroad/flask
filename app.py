from flask import Flask, render_template, request, send_from_directory
import pytube as yt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt.YouTube(url).streams.filter(only_audio=True, subtype='mp4').first().download()
    return render_template('download.html', url=url)
    # return send_from_directory(
    #         directory='downloads',
    #         filename='url.mp4'
    # )


if __name__ == '__main__':
    app.run()
