from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django_ratelimit.decorators import ratelimit
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import ContactMessage
from ..projects.models import Project


@ratelimit(key='ip', rate='5/m', method='POST', block=False)
def contact(request):

    # =========================
    # 🚫 RATE LIMIT PROTECTION
    # =========================
    if getattr(request, 'limited', False):
        messages.error(request, "Too many requests. Please try again later.")
        return redirect("contact")

    # =========================
    # 📌 GET PROJECT FROM URL
    # =========================
    project_slug = request.GET.get("project")
    project = None

    if project_slug:
        try:
            project = Project.objects.get(slug=project_slug)
        except Project.DoesNotExist:
            project = None

    # =========================
    # 📩 HANDLE FORM
    # =========================
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            # 🛡️ Honeypot (anti-bot)
            if form.cleaned_data.get("honeypot"):
                return redirect("contact")  # silent spam drop

            message_obj = form.save(commit=False)

            # ✅ Attach project to DB
            if project:
                message_obj.project = project

            message_obj.save()

            # =========================
            # 🔗 BUILD PROJECT URL
            # =========================
            project_url = None
            if project:
                request_domain = request.build_absolute_uri('/')[:-1]
                project_url = f"{request_domain}/projects/{project.slug}"

            # =========================
            # 📧 EMAIL CONTEXT
            # =========================
            context = {
                "name": message_obj.name,
                "email": message_obj.email,
                "subject": message_obj.subject,
                "message": message_obj.message,
                "project": project,
                "project_url": project_url,
            }

            # =========================
            # 📧 ADMIN EMAIL
            # =========================
            try:
                html_admin = render_to_string(
                    "emails/contact_admin.html",
                    context
                )

                email_admin = EmailMultiAlternatives(
                    subject=f"New Contact: {message_obj.subject}",
                    body=message_obj.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.DEFAULT_FROM_EMAIL],
                )

                email_admin.attach_alternative(html_admin, "text/html")
                email_admin.send()

            except Exception as e:
                print("Admin email error:", e)

            # =========================
            # 📧 USER EMAIL
            # =========================
            try:
                html_user = render_to_string(
                    "emails/contact_user.html",
                    context
                )

                email_user = EmailMultiAlternatives(
                    subject="We received your message ✔",
                    body=message_obj.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[message_obj.email],
                )

                email_user.attach_alternative(html_user, "text/html")
                email_user.send()

            except Exception as e:
                print("User email error:", e)

            messages.success(request, "Message sent successfully. Please check your inbox (and spam folder just in case.")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {
        "form": form,
        "project": project,
    })

'''
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_message = f"""
From: {name} <{email}>

{message}
"""

            send_mail(
                subject,
                full_message,
                email,  # from
                ["abalaymaya@outlook.com"],  # to
            )

            messages.success(request, "Your message has been sent!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})

'''
'''
def contact(request):
    """
    Contact page with form handling
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            message_obj = form.save()

            # OPTIONAL: email notification
            send_mail(
                subject=f"New Contact: {message_obj.subject}",
                message=(
                    f"Name: {message_obj.name}\n"
                    f"Email: {message_obj.email}\n\n"
                    f"{message_obj.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Thank you for your message. I’ll get back to you soon."
            )
            return redirect("contact")

    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "contact/contact.html", context)
'''
'''
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            message_obj = form.save()  # ✅ save to DB

            try:
                send_mail(
                    subject=f"New Contact: {message_obj.subject}",
                    message=(
                        f"Name: {message_obj.name}\n"
                        f"Email: {message_obj.email}\n\n"
                        f"{message_obj.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                )
            except Exception as e:
                # Optional: log error
                print("Email error:", e)

            messages.success(
                request,
                "Thank you for your message. I’ll get back to you soon."
            )
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
'''
"""
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            # 🚨 Honeypot check
            if form.cleaned_data.get('honeypot'):
                messages.error(request, "Spam detected. Please try again later.")
                # silently ignore spam
                return redirect("contact")

            message_obj = form.save()

            context = {
                "name": message_obj.name,
                "email": message_obj.email,
                "subject": message_obj.subject,
                "message": message_obj.message,
            }

            # =========================
            # 1️⃣ EMAIL TO YOU (ADMIN)
            # =========================
            try:
                html_content = render_to_string(
                    "emails/contact_admin.html", context
                )

                email = EmailMultiAlternatives(
                    subject=f"New Contact: {message_obj.subject}",
                    body=message_obj.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.DEFAULT_FROM_EMAIL],
                )

                email.attach_alternative(html_content, "text/html")
                email.send()

            except Exception as e:
                print("Admin email error:", e)

            # =========================
            # 2️⃣ EMAIL TO USER
            # =========================
            try:
                html_content = render_to_string(
                    "emails/contact_user.html", context
                )

                email = EmailMultiAlternatives(
                    subject="We received your message ✔",
                    body=message_obj.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[message_obj.email],
                )

                email.attach_alternative(html_content, "text/html")
                email.send()

            except Exception as e:
                print("User email error:", e)

            messages.success(
                request,
                "Message sent successfully. Check your email."
            )
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})

"""



"""
@login_required
def contact_messages(request):
    messages_list = ContactMessage.objects.order_by("-created_at")

    return render(request, "contact/dashboard_list.html", {
        "messages_list": messages_list
    })


@login_required
def contact_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)

    # Mark as read
    if not message.is_read:
        message.is_read = True
        message.save()

    return render(request, "contact/dashboard_detail.html", {
        "message": message
    })
"""
@login_required
def contact_messages(request):
    messages_list = ContactMessage.objects.order_by("-created_at")

    return render(request, "contact/dashboard_list.html", {
        "messages_list": messages_list
    })


@login_required
def contact_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)

    # ✅ Mark as read
    if not message.read:
        message.read = True
        message.save()

    return render(request, "contact/dashboard_detail.html", {
        "message": message
    })

# ✅ Toggle read/unread (button action)
@login_required
def toggle_read(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)

    message.read = not message.read
    message.save()

    return redirect("contact_dashboard")