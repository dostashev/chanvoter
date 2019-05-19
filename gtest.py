from flask import Flask, render_template
app = Flask(__name__)

@app.route('/contest')
def hello_world():
    return render_template('/contest.html', 
            first_girl = { 'name' : 'Hello', 'instagram' : 'Hello123', 'id' : 228 },
            second_girl = { 'name' : 'Julia', 'instagram' : 'cloudlet_jt', 'id' : 27 },
            contest_id = 14)

@app.route('/')
def hello_julia():
    active_contests = [
            {
                'first_girl' : { 'name' : 'Julia' }, 
                'second_girl' : { 'name' : 'Inna' },
                'end' : '10.02.2002 9PM',
                'id' : 1
            }, 

            {
                'first_girl' : { 'name' : 'Eve' }, 
                'second_girl' : { 'name' : 'Neli' },
                'end' : '10.03.2002 9PM',
                'id' : 2
            },

            {
                'first_girl' : { 'name' : 'Arina' }, 
                'second_girl' : { 'name' : 'Alexandra' },
                'end' : '10.02.2002 9PM',
                'id' : 3
            }]

    return render_template('index.html', active_contests=active_contests)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
