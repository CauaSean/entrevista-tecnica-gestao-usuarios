
from django.core.management.base import BaseCommand
from people.services import buscar_checkouts_pendentes, notificar_pendentes

class Command(BaseCommand):
    help = "Verifica check-outs pendentes"

    def handle(self, *args, **kwargs):
        pendentes = buscar_checkouts_pendentes()
        notificar_pendentes(pendentes)

        self.stdout.write(f"{pendentes.count()} pendentes encontrados.")