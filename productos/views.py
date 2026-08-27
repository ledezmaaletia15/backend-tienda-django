from django.http import HttpResponse, JsonResponse

def inicio(request):
    return HttpResponse('Módulo de productos: ¡Activo!')

def acerca(request):
    return HttpResponse('API de ejemplo para la semana #3')

def api_productos(request):
    if request.method == 'GET':
        datos = [
            {'id':1, 'nombre':'Teclado'},
            {'id':2, 'nombre':'Mouse'},
        ]
        return JsonResponse(datos, safe=False)
    return JsonResponse(
        {'error':'Método no permitido'},
        status=405
    )