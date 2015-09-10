from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response


class CicloList(APIView):

    def get(self, request, *args, **kwargs):

        cursor = connections['default'].cursor()
        cursor.execute('SELECT * FROM CARGA_CICLO')
        rs = cursor.fetchall()
        usernames = [user[1] for user in rs]
        return Response(usernames)
