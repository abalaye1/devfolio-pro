# context_processors.py

from .models import ContactMessage

def unread_messages(request):
    return {
        "unread_count": ContactMessage.objects.filter(read=False).count()
    }