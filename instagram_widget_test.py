from instagram.client import InstagramAPI

TOKEN = '6336060038.b520bf6.bd49e16b4bf1472091b50b4ea603e900'
SECRET = '1f439a2bf0294304b931c90a55f9d449'

api = InstagramAPI(access_token=TOKEN, client_secret=SECRET)
recent_media, next_ = api.user_recent_media(user_id="cloudlet_jt", count=5)

for media in recent_media:
    print(media.images['standard_resolution'].url)




