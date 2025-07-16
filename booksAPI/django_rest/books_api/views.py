from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books_api.models import Book
from books_api.serializers import BookSerializer


class ListBooksView(APIView):

    def get(self, req):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

    def post(self, req):
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookView(APIView):

    def get(self, req, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response({"book": serializer.data})

    def put(self, req, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_200_OK)


















