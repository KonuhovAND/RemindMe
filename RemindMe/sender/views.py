from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import smtplib
import datetime
from email.message import EmailMessage


def send_scheduled_email(subject, recipient, message, schedule_time):
    """Your email sending function"""
    print(
        f"Scheduling email:\nTo: {recipient}\nSubject: {subject}\nTime: {
            schedule_time
        }\nMessage: {message}"
    )
    """Actual email sending with scheduling"""
    # Calculate delay in seconds
    now = datetime.now()
    delay = (schedule_time - now).total_seconds()

    if delay > 0:
        print(f"Waiting {delay} seconds to send email...")
        time.sleep(delay)

    # Create email
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = "andreykonuhov8@example.com"
    msg["To"] = recipient

    # Send email (using Gmail example)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("andreykonuhov8@example.com", "auvh nxkj ehpb lbfq ")
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    # Add your actual email sending logic here
    # For production: Use Django's send_mail() or SMTP lib


@csrf_exempt  # Disable CSRF for simplicity (enable in production)
def send_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Extract form data
            subject = data.get("subject")
            recipient = data.get("recipient")
            message = data.get("message")
            schedule_time = data.get("schedule")  # Format: "YYYY-MM-DDTHH:MM"

            # Convert to datetime object
            scheduled_datetime = datetime.strptime(
                schedule_time, "%Y-%m-%dT%H:%M")

            # Call your email sending function
            send_scheduled_email(
                subject=subject,
                recipient=recipient,
                message=message,
                schedule_time=scheduled_datetime,
            )

            return JsonResponse({"message": "Email scheduled successfully!"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
