import app.Instagram.usuario
import app.Instagram.funciones_auxiliares as fa
import urllib3
urllib3.disable_warnings()

def get_unfollowers(user):
    logger = "nachonitz"
    api = fa.login(logger)
    usuario1 = app.Instagram.usuario.Usuario(api,user)

    return usuario1.get_unfollowers()
