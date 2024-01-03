from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from apps.post.models import Post, Genre, GameDeveloper


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
        posts = [
            {
                "title": "Skyrim",
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
            {
                "title": "Fallout 4",
                "poster": "posters/poster2.jpg",
                "developer": GameDeveloper.objects.order_by("?").first(),
                "voiceover_language": "english",
                "interface_language": "english",
                "content": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem.",
                "operating_system": "Windows 10",
                "processor": "AMD Ryzen 7",
                "memory": "16 GB RAM",
                "video_card": "AMD Radeon RX 5700",
                "sound_card": "DirectX® compatible sound card",
                "disk_space": "100 GB",
            },
        ]

        posts = Post.objects.bulk_create([Post(**post) for post in posts])
        for post in posts:
            post.genres.set(Genre.objects.order_by("?")[:4])
        self.stdout.write(self.style.SUCCESS("Database seed succes"))
