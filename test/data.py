import datetime

girls = [
    {
        'name' : 'Julia Tarasenko',
        'instagram' : 'cloudlet_jt',
        'ELO' : 1500.9,
        'photo' : '/resources/girls/cloudlet_jt.png'
    },
    { 'name' : 'Inna Glushenko',
        'instagram' : 'inna_gluschenko',
        'ELO' : 1500.0,
        'photo' : '/resources/girls/inna_glushchenko.png'

    },
    {
        'name' : 'Eve Stepanova',
        'instagram' : 'stapaschaa',
        'ELO' : 1499.9,
        'photo' : '/resources/girls/stepaschaa.png'

    },
    {
        'name' : 'Neli Blinova',
        'instagram' : '_neonelka_',
        'ELO' : 1500.0,
        'photo' : '/resources/girls/_neonelka_.png'

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
    },
    {
        'first_girl_id' : 2,
        'second_girl_id' : 4,
        'begin' : datetime.datetime(2019, 6, 15),
        'end' : datetime.datetime(2019, 6, 17)
    },
    {
        'first_girl_id' : 1,
        'second_girl_id' : 3,
        'begin' : datetime.datetime(2019, 6, 16),
        'end' : datetime.datetime(2019, 6, 18)
    }
]

users = [
    {
        'address' : '1',
        'private_key' : '1',
        'coins' : 1000000000
    },
    {
        'address' : '2',
        'private_key' : '2',
        'coins' : 1000000000
    },
    {
        'address' : '3',
        'private_key' : '3',
        'coins' : 1000000000
    },
    {
        'address' : '4',
        'private_key' : '4',
        'coins' : 1000000000
    } 
]
