from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    

    def __str__(self):
        return f"Title => {self.title}, Content => {self.content}"




# Routes
# GET, PUT, PATCH, POST, DELETE

# GET /posts => Get all posts
# POST /posts => Create a post
# GET /posts/:id => Get a post by id
# DELETE /posts/:id => Delete a post by id
# PUT /posts/:id => update a post by id

# GET /books => Get all books
# GET /books/:id => 