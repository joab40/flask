from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('bip.html')
@app.route('/showDeploy')
def showSignUp():
    return render_template('deploy.html')
if __name__ == "__main__":
    app.run()
