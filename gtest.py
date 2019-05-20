from flask import Flask, render_template
app = Flask(__name__)

test_girls = [
        {
            'name' : 'Юлия Тарасенко', 
            'instagram' : 'cloudlet_jt',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 1,
            'ELO' : 1515.0
        }, 
        {
            'name' : 'Инна Глущенко', 
            'instagram' : 'inna_glushenko',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 2, 
            'ELO' : 1500.0
        }, 
        {
            'name' : 'Ева Степанова', 
            'instagram' : 'stepaschaa',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 3,
            'ELO' : 1270.0
        }, 
        {
            'name' : 'Неля Блинова', 
            'instagram' : 'neonelka',
            'photo' : 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fv.img.com.ua%2Fb%2F1100x999999%2F5%2Fed%2Fefbc4030586f964def135ca78401ced5.jpg&f=1', 
            'id' : 4,
            'ELO' : 1499.0
        }] 

@app.route('/contest/<int:hello>')
def hello_world(hello):
    return render_template('/contest_.html', 
            first_girl = test_girls[0],
            second_girl = test_girls[1],
            contest_id = 1)

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
    girls = sorted(test_girls, key=lambda x : -x["ELO"])
    for i in range(len(girls)):
        girls[i]["rating"] = i + 1

    return render_template('rating.html', girls=girls)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
