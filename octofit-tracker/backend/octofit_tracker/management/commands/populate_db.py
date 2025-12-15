from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Очистка данных
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Создание команд
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Создание пользователей
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@rogers.com', team=marvel)
        bruce = User.objects.create(name='Bruce Banner', email='bruce@banner.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@kent.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@prince.com', team=dc)

        # Создание активностей
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='fly', duration=120, date=timezone.now().date())
        Activity.objects.create(user=diana, type='fight', duration=90, date=timezone.now().date())

        # Создание воркаутов
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        w2 = Workout.objects.create(name='Situps', description='Do 30 situps')
        w1.suggested_for.set([tony, steve, clark])
        w2.suggested_for.set([diana, bruce])

        # Создание лидерборда
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=80)
        Leaderboard.objects.create(user=clark, score=110)
        Leaderboard.objects.create(user=diana, score=105)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated!'))
