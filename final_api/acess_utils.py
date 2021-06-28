from src.models import Users
from werkzeug.security import generate_password_hash

def insert_user(user, password):
    user_pass = Users(user=user,
                      password=generate_password_hash(password, "sha256"),
                      active=1)
    user_pass.save()
    print(f"User: {user} add")

def deactive_user(user):
    user_pass = Users.query.filter_by(user=user).first()
    user_pass.active = 0
    user_pass.save()

def list_all_users():
    user_pass = Users.query.all()
    for u in user_pass:
        if u.active == 1:
            flag_active = "active"
        else:
            flag_active = "deactive"
        print(f"User: {u.user} | Active: {flag_active}")

if __name__ == '__main__':
    #insert_user("ota", "123")
    #deactive_user("admin")
    list_all_users()