from login import models

def auth(username, password):
    try:
        user = models.Users.objects.get(username=username)
        return user.check_password(password)
    except models.Users.DoesNotExist:
        return False
    
def create_admin():
    user = models.Users(username="ad.admin", email="admin@admin.com", role_id_id=1)
    user.set_password("12345678")  # Hash the password
    user.save()

def create_user():
    user = models.Users(username="ad.user", email="user@user.com", role_id_id=2)
    user.set_password("12345678")  # Hash the password
    user.save()