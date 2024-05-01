from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OrderView(APIView):
    def get(self, request):
        # Your logic for handling GET requests goes here
        return Response("GET request received", status=status.HTTP_200_OK)

    def post(self, request):
        # Your logic for handling POST requests goes here
        return Response("POST request received", status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        # Your logic for handling PUT requests goes here
        return Response(
            f"PUT request received for order with id {pk}", status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        # Your logic for handling DELETE requests goes here
        return Response(
            f"DELETE request received for order with id {pk}",
            status=status.HTTP_204_NO_CONTENT,
        )
