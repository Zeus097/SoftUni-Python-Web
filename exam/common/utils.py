from organizer.models import Organizer


def get_organizer():
    return Organizer.objects.first()
