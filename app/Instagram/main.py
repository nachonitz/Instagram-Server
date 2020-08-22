import app.Instagram.usuario
import app.Instagram.funciones_auxiliares as fa
import urllib3
urllib3.disable_warnings()

def get_profile(user):
    logger = "nachonitz"
    api = fa.login(logger)
    usuario1 = app.Instagram.usuario.Usuario(api,user)
    unfollowers = usuario1.get_unfollowers()
    fans = usuario1.get_fans()
    seguidores = usuario1.get_seguidores()
    seguidos = usuario1.get_seguidos()
    id_medias = usuario1.get_id_posts()
    return {"unfollowers": unfollowers,
            "fans": fans,
            "followers": seguidores,
            "followings": seguidos,
            "medias": id_medias}
