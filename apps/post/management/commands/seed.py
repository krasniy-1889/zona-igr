import logging
import random
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from apps.post.models import Post, Genre, GameDeveloper, Comment
from cuid import cuid

from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):
        # Genre seed
        genres = [
            {"name": "Хоррор"},
            {"name": "Приклчение"},
            {"name": "RPG"},
            {"name": "Стратегия"},
            {"name": "Открытый мир"},
            {"name": "Фэнтези"},
        ]
        Genre.objects.bulk_create([Genre(**genre) for genre in genres])

        # Developer seed
        developers = [
            {"name": "Rockstar Games"},
            {"name": "Activision"},
            {"name": "Ubisoft"},
            {"name": "Electronic Arts"},
            {"name": "Bethesda"},
            {"name": "Square Enix"},
        ]
        GameDeveloper.objects.bulk_create(
            [GameDeveloper(**developer) for developer in developers]
        )
        # Post seed
        posts = []
        for _ in range(100):
            posts.append(
                {
                    "title": f"Game - {cuid()}",
                    "poster": "posters/poster1.jpg",
                    "developer": GameDeveloper.objects.order_by("?").first(),
                    "voiceover_language": "русский",
                    "interface_language": "русский",
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "operating_system": "XP / Vista / 7 / 8 / 10",
                    "processor": "Intel Core i5",
                    "memory": "8 GB RAM",
                    "video_card": "NVIDIA GeForce GTX 1060",
                    "sound_card": "Звуковое устройство DirectX® 9.0с",
                    "disk_space": "50 GB",
                },
            )

        posts = Post.objects.bulk_create([Post(**post) for post in posts])
        for post in posts:
            post.genres.set(Genre.objects.order_by("?")[:4])
            for _ in range(random.randint(20, 100)):
                user = get_user_model().objects.first()
                text = cuid()
                parent = random.choice([None] + list(Comment.objects.filter(post=post)))

                comment = Comment.objects.create(
                    post=post,
                    user=user,
                    text=text,
                    parent=parent,
                )

                if parent:
                    parent.children.add(comment)

        self.stdout.write(self.style.SUCCESS("Database seed succes"))
