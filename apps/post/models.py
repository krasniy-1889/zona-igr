from django.db import models
from django_extensions.db.models import AutoSlugField

from rest_framework.authentication import get_user_model


class GameDeveloper(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class LANGUAGE(models.TextChoices):
        RU = "русский", "Русский"
        EN = "english", "English"

    class PLATRFORM(models.TextChoices):
        PC = "pc", "PC"
        PS4 = "ps4", "PS4"
        PS5 = "ps5", "PS5"
        XBOX = "xbox", "Xbox"

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title")  # type: ignore
    poster = models.ImageField(upload_to="posters/")
    likes = models.ManyToManyField(
        get_user_model(), related_name="post_likes", blank=True
    )
    dislikes = models.ManyToManyField(
        get_user_model(), related_name="post_dislikes", blank=True
    )
    developer = models.ForeignKey("GameDeveloper", on_delete=models.CASCADE)
    voiceover_language = models.CharField(
        max_length=10,
        choices=LANGUAGE.choices,
        default=LANGUAGE.RU,
    )
    interface_language = models.CharField(
        max_length=10,
        choices=LANGUAGE.choices,
        default=LANGUAGE.RU,
    )

    genres = models.ManyToManyField("Genre", related_name="posts")
    content = models.TextField()

    # System requiements
    operating_system = models.CharField(
        max_length=200, default="XP / Vista / 7 / 8 / 10"
    )
    processor = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    video_card = models.CharField(max_length=200)
    sound_card = models.CharField(
        max_length=200, default="Звуковое устройство DirectX® 9.0с"
    )
    disk_space = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.user} - {self.post}"
