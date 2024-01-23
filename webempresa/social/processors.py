from social.models import Link

# manejo de las redes sociales por link
def ctx_contex(request):
    ctk ={}
    links = Link.objects.all()
    for link in links:
        ctk[link.key]=link.url
    return ctk