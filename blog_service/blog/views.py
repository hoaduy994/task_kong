from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Blog
from .serializers import BlogSerializer

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

class BlogCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogUpdate(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.author != self.request.user:
            raise ValidationError({
                "error": "Permission Denied!",
                "detail" : "khong co quyen sua!"
            })
        serializer.save(author=self.request.user)

class BlogDelete(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, serializer):
        blog = self.get_object()
        if blog.author != self.request.user:
            raise ValidationError({
                "error": "Permission Denied!",
                "detail" : "khong co quyen xoa!"
            })
        serializer.delete()