from django.core.management.base import BaseCommand
from login.models import Users, Roles  # Adjust import based on your app name
# import Faker

# fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample users and roles'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=0, help='Number of users to create')

    def handle(self, *args, **options):
        self.stdout.write(f'Seeding users and roles...')
        # Roles
        role_admin = Roles( role_name='Admin', role_desc='Admin')
        role_admin.save()

        role_user = Roles( role_name='User', role_desc='User')
        role_user.save()


        # AD Admin
        user = Users(
            username='ad.admin',
            email='admin@admin.com',
            role_id_id=1 
        )
        user.set_password('12345678') 
        user.save()

        # AD User
        user = Users(
            username='ad.user',
            email='user@user.com',
            role_id_id=2
        )
        user.set_password('12345678') 
        user.save()

        return