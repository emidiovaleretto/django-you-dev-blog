from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

from .models_post import Post
from .models_comment import Comment