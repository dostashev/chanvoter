from flask import Flask, render_template
app = Flask(__name__)

test_girls = [
        {
            'name' : 'Юлия Тарасенко', 
            'instagram' : 'cloudlet_jt',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 1
        }, 
        {
            'name' : 'Инна Глущенко', 
            'instagram' : 'inna_glushenko',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 2
        }, 
        {
            'name' : 'Ева Степанова', 
            'instagram' : 'stepaschaa',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 3
        }, 
        {
            'name' : 'Неля Блинова', 
            'instagram' : 'neonelka',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 4
        }] 

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
                'first_girl' : test_girls[0], 
                'second_girl' : test_girls[1],
                'end' : '10.02.2002 9PM',
                'id' : 1
            }, 

            {
                'first_girl' : test_girls[2],
                'second_girl' : test_girls[3],
                'end' : '10.03.2002 9PM',
                'id' : 2
            },

            {
                'first_girl' : test_girls[1], 
                'second_girl' : test_girls[3],
                'end' : '10.02.2002 9PM',
                'id' : 3
            }]

    return render_template('index.html', active_contests=active_contests)

@app.route('/rating')
def hello_rating():
    return render_template('rating.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
