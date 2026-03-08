from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()


        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users (store team_id as string)
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team_id=str(marvel.id)),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team_id=str(marvel.id)),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_id=str(dc.id)),
            User.objects.create(name='Batman', email='batman@dc.com', team_id=str(dc.id)),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout', suggested_for='Marvel'),
            Workout.objects.create(name='Stealth Training', description='Stealth and agility', suggested_for='DC'),
        ]

        # Create Activities (store user_id as string)
        Activity.objects.create(user_id=str(users[0].id), type='Web Swinging', duration=30, date=timezone.now().date())
        Activity.objects.create(user_id=str(users[1].id), type='Suit Upgrade', duration=45, date=timezone.now().date())
        Activity.objects.create(user_id=str(users[2].id), type='Lasso Practice', duration=40, date=timezone.now().date())
        Activity.objects.create(user_id=str(users[3].id), type='Detective Work', duration=50, date=timezone.now().date())

        # Create Leaderboard (store user_id as string)
        Leaderboard.objects.create(user_id=str(users[0].id), score=100)
        Leaderboard.objects.create(user_id=str(users[1].id), score=90)
        Leaderboard.objects.create(user_id=str(users[2].id), score=95)
        Leaderboard.objects.create(user_id=str(users[3].id), score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
