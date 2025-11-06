from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create(email='tony@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='steve@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='bruce@marvel.com', name='Hulk', team=marvel),
            User.objects.create(email='clark@dc.com', name='Superman', team=dc),
            User.objects.create(email='diana@dc.com', name='Wonder Woman', team=dc),
            User.objects.create(email='barry@dc.com', name='Flash', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(name='Running', user=users[0], duration=30, date='2025-11-06')
        Activity.objects.create(name='Cycling', user=users[1], duration=45, date='2025-11-06')
        Activity.objects.create(name='Swimming', user=users[2], duration=60, date='2025-11-06')
        Activity.objects.create(name='Running', user=users[3], duration=25, date='2025-11-06')
        Activity.objects.create(name='Cycling', user=users[4], duration=40, date='2025-11-06')
        Activity.objects.create(name='Swimming', user=users[5], duration=55, date='2025-11-06')

        # Crear workouts
        Workout.objects.create(name='Pushups', description='Upper body', user=users[0], date='2025-11-06')
        Workout.objects.create(name='Squats', description='Lower body', user=users[1], date='2025-11-06')
        Workout.objects.create(name='Plank', description='Core', user=users[2], date='2025-11-06')
        Workout.objects.create(name='Pushups', description='Upper body', user=users[3], date='2025-11-06')
        Workout.objects.create(name='Squats', description='Lower body', user=users[4], date='2025-11-06')
        Workout.objects.create(name='Plank', description='Core', user=users[5], date='2025-11-06')

        # Crear leaderboard
        Leaderboard.objects.create(name='Marvel Leaderboard', team=marvel, points=100)
        Leaderboard.objects.create(name='DC Leaderboard', team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
