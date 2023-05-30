from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..application.services.product_services import ProductServices


class ProductApi(APIView):

    def post(self, request):
        try:

            data = JSONParser().parse(request)
            product = ProductServices().execute(data)

            return Response(status=status.HTTP_201_CREATED, data={
                "id": product.id
            })

        except Exception as ex:
            return Response(data={"result": "error", "message": "Internal Error"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
