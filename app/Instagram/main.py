import app.Instagram.usuario
import app.Instagram.funciones_auxiliares as fa
import urllib3
import app.Instagram.InstagramAPI as InstagramAPI
urllib3.disable_warnings()


def get_profile(username, username_id, token, rank_token, uuid, sessionid):
    api = InstagramAPI.InstagramAPI("asd", "asd")
    api.sync_api(username_id, token, rank_token, uuid, sessionid)
    usuario1 = app.Instagram.usuario.Usuario(api, username)
    unfollowers = usuario1.get_unfollowers()
    fans = usuario1.get_fans()
    seguidores = usuario1.get_seguidores()
    seguidos = usuario1.get_seguidos()
    #id_medias = usuario1.get_id_posts()
    user_info = usuario1.get_user_info()
    return {"unfollowers": unfollowers,
            "fans": fans,
            "followers": seguidores,
            "followings": seguidos,
            #"medias": id_medias,
            "user_info": user_info
            }


def login(username, password):
    api = InstagramAPI.InstagramAPI(username, password)
    api.login()
    return api.get_portable_data()