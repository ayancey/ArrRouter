from flask import Flask, send_file, Response, jsonify
import radarr
import sonarr
import ffmpeg
import tempfile
import boto3
import uuid
import time
from flask_cors import CORS, cross_origin

s3 = boto3.resource("s3")



prepared_videos = {}


app = Flask(__name__)
CORS(app)


def transcode_content(f_name):
    print(f"transcoding {f_name}...")
    inp = ffmpeg.input(f_name)

    tf = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
    tf.close()

    out = inp.output(tf.name, acodec='copy', vcodec='copy', scodec='copy', movflags="frag_keyframe+empty_moov", ac=2, format="mp4")

    out.run(overwrite_output=True)

    print("done")

    return tf.name


def upload_content(f_name):
    print("uploading...")
    before = time.time()
    uid = str(uuid.uuid4())
    s3.Bucket("alexwatchparty").upload_file(f_name, f"{uid}.mp4")
    print(f"done. took {time.time() - before} seconds.")
    return f"https://alexwatchparty.s3.us-west-2.amazonaws.com/{uid}.mp4"


@app.route("/movie")
@cross_origin()
def movies():
    return jsonify(radarr.get_movies())


@app.route("/movie/prepare/<mid>")
def movie_prepare(mid):
    f_name = radarr.return_path_fixed(mid)
    trans_f_name = transcode_content(f_name)
    s3_url = upload_content(trans_f_name)
    return jsonify({"success": True, "url": s3_url})


@app.route("/tv/prepare/<eid>")
def tv_prepare(eid):
    f_name = sonarr.return_path_fixed(eid)
    trans_f_name = transcode_content(f_name)
    s3_url = upload_content(trans_f_name)
    return jsonify({"success": True, "url": s3_url})


@app.route("/tv")
def tv_show():
    return jsonify(sonarr.get_tv_shows())


@app.route("/tv/seasons/<sid>")
def tv_show_seasons(sid):
    return jsonify(sonarr.get_seasons(sid))

@app.route("/tv/episodes/<sid>")
def tv_show_episodes(sid):
    return jsonify(sonarr.get_episodes(sid))





@app.route("/tv/<tid>")
def radarr_stream(tid):
    return send_file(prepared_videos[f"tv_{tid}"])



if __name__ == "__main__":
    #prepare_movie(2808)
    # out, _ = inp.output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000) \
    #     .run(cmd=[ffmpeg_path, "-nostdin"], capture_stdout=True, capture_stderr=True)

    app.run(threaded=True)
