import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        proc = subprocess.Popen(
            ['dmesg'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

app.run(debug=True, port=5000, host='0.0.0.0')
