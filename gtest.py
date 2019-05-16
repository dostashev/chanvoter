from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('/contest.html', 
            first_girl = { 'name' : 'Hello', 'instagram' : 'Hello123', 'id' : 228 },
            second_girl = { 'name' : 'Julia', 'instagram' : 'cloudlet_jt', 'id' : 27 },
            contest_id = 14)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
