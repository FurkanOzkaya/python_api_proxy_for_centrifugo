from user.models import UserModel


def get_user_by_id(id):
    try:
        user = UserModel.objects.get(id=id)
        return user
    except Exception as err:
        print("Exception when fetching user by id ", err)
        return None


def get_user_by_username(username):
    try:
        user = UserModel.objects.get(username=username)
        return user
    except Exception as err:
        print("Exception when fetching user by username ", err)
        return None
