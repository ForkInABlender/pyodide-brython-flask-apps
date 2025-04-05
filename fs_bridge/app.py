from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pyodide/<path:filename>')
def pyodide_files(filename):
    return send_from_directory('pyodide', filename)

if __name__ == '__main__':
    app.run(debug=True)
