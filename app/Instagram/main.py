import app.Instagram.usuario
import app.Instagram.funciones_auxiliares as fa
import urllib3
urllib3.disable_warnings()

def get_profile(user):
    logger = "nacho.n.n"
    api = fa.login(logger)
    usuario1 = app.Instagram.usuario.Usuario(api,user)
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
