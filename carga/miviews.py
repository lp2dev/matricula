from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0].lower() for col in desc],  row))
        for row in cursor.fetchall()
    ]


class CicloList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):

        cursor = connections['default'].cursor()
        cursor.execute('SELECT id, abrev, descr FROM CARGA_CICLO')
        #rs = cursor.fetchall()
        usernames = dictfetchall(cursor)
        # result = dict(zip([col[0] for col in cursor.description], row)) for
        # row in cursor.fetchall()

        # return Response(result)
        # usernames = "hola"
        return Response(usernames, content_type='application/json')
