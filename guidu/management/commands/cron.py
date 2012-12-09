from django.core.management.base import BaseCommand, CommandError
from guidu.models import Guidu

class Command(BaseCommand):
    help = 'Atualiza Guidus'
    args = '<guidu_id guidu_id ...>'

    def handle(self, *args, **options):
        if args:
            for guidu_id in args:
                try:
                    guidu = Guidu.objects.get(pk=int(guidu_id))
                    guidu.refresh()
                    guidu.save()
                except Guidu.DoesNotExist:
                    raise CommandError('Guidu "%s" nao existe' % guidu_id)

                self.stdout.write('Atualizou o guidu: "%s" de nome: %s \n' % (guidu_id, guidu.nome))
        else:
            guidus = Guidu.objects.all()
            for guidu in guidus:
                guidu.refresh()
                guidu.save()
            self.stdout.write('Atualizou todos os guidus\n')
