from flask import Flask, send_file, Response
import radarr
import ffmpeg
import tempfile

prepared_videos = {}


app = Flask(__name__)


def prepare_movie(mid):
    inp = ffmpeg.input(radarr.return_path_fixed(mid))

    tf = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
    tf.close()

    out = inp.output(tf.name, acodec='copy', vcodec='copy', movflags="frag_keyframe+empty_moov", format="mp4")

    out.run(overwrite_output=True)

    prepared_videos[mid] = tf.name


@app.route("/movies/<mid>")
def radarr_stream(mid):
    return send_file(prepared_videos[int(mid)])


if __name__ == "__main__":
    prepare_movie(2808)
    # out, _ = inp.output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000) \
    #     .run(cmd=[ffmpeg_path, "-nostdin"], capture_stdout=True, capture_stderr=True)

    app.run(threaded=True)
