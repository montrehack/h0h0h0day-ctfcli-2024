from flask import Flask, render_template
from dataclasses import dataclass
import uuid
from random import randint

def random_uuid():
    return str(uuid.uuid4())


app = Flask(__name__)

@dataclass
class Video:
    path: str
    img: str
    status: str = 'Offline'
    naughty: int = 0
    nice: int = 0
    subtitle: bool = False

    def __post_init__(self):
        nice = randint(0, 100)
        naughty = 100 - nice
        
        self.nice = nice
        self.naughty = naughty

videos = {
    'Timmy\'s House': Video('42b376b9-32f5-5bf3-a131-bbdba4b2614f', 'house', 'Online'), # Flag 1
    'Carter\'s Manor': Video(random_uuid(), 'manor'), # Noop
    'James\'s Boat': Video(random_uuid(), 'boat'), # Noop
    'Riley\'s Shed': Video(random_uuid(), 'shed'), # Noop
    'Camila\'s Room': Video('2aa2f106-d72a-5b44-82f8-8d2453e018d2', 'room', 'Online'), # Flag 2
    'Mateo\'s Garden': Video(random_uuid(), 'garden'), # Noop
    'Avery\'s Kitchen': Video('b4f3c547-fe93-5fd9-8418-51d705fee48e', 'kitchen', 'Online', subtitle=True), # Flag 3
}

mapping = { video.path: name for name, video in videos.items() }

@app.route('/')
def hello():
    return render_template('home.html', page="Home", videos=videos.items())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/video/<video_id>')
def video(video_id):
    video_name = mapping.get(video_id)
    if not video_name:
        return render_template('404.html'), 404

    video = videos.get(video_name)
    if not video or video.status != 'Online':
        return render_template('404.html'), 404

    return render_template('viewer.html', page=video_name, video=video)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)