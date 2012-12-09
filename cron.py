from guidu.models import Guidu


def cronjob():
    guidus = Guidu.objects.all()
    for guidu in guidus:
        guidu.refresh()
