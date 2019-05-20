import datetime

girls = [
    {
        'name' : 'Julia Tarasenko',
        'instagram' : 'cloudlet_jt',
        'ELO' : 1500.9
    },
    {
        'name' : 'Inna Glushenko',
        'instagram' : 'inna_gluschenko',
        'ELO' : 1500.0
    },
    {
        'name' : 'Eve Stepanova',
        'instagram' : 'stapaschaa',
        'ELO' : 1499.9
    },
    {
        'name' : 'Neli Blinova',
        'instagram' : '_neonelka_',
        'ELO' : 1500.0
    }
]

contests = [
    {
        'first_girl_id' : 1,
        'second_girl_id' : 2,
        'begin' : datetime.datetime(2019,1,1),
        'end' : datetime.datetime(2019,12,1)
    },
    {
        'first_girl_id' : 3,
        'second_girl_id' : 4,
        'begin' : datetime.datetime(2019,1,1),
        'end' : datetime.datetime(2019,12,1)
    }
]

users = [
    {
        'address' : 'root',
        'private_key' : 'jojo',
        'coins' : 1000000000
    }
]