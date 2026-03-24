from django.utils import timezone
from .checkin import Checkin

def buscar_checkouts_pendentes():
    agora = timezone.now()
    return Checkin.objects.filter(
        checkout__isnull=True,
        expected_checkout_date__lt=agora, 
        notificado=False                  
    )
def notificar_pendentes(pendentes):
    for checkin in pendentes:
        print(f"Check-out pendente: {checkin.person.name}")

        checkin.notificado = True
        checkin.save()

        send_mail(
            subject="Check-out pendente",
            message=f"O paciente {checkin.person.name} ainda não fez check-out.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],  # ou lista de admins
        )