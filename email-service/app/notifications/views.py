from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ContactMessage, NotificationLog
from .serializers import ContactMessageSerializer, NotificationLogSerializer
from app.utils.mailer import send_email

class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        # Simulación de envío de correo
        send_email(
            to_email=contact.email,
            subject="Gracias por contactarnos",
            body=contact.message
        )
        return Response({"status": "queued"}, status=status.HTTP_202_ACCEPTED)


class NotifyViewSet(viewsets.ModelViewSet):
    queryset = NotificationLog.objects.all()
    serializer_class = NotificationLogSerializer
