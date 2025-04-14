from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# إعدادات الإرسال
GMAIL_USER = os.environ.get("khaledalmnify1988@gmail.com")  # مثال: khaledalmnify1988@gmail.com
GMAIL_PASS = os.environ.get("tgyi iwid psny qzqd")  # كلمة مرور التطبيقات
TO_EMAIL = "khaled_alminfy@limu.edu.ly"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    subject = data.get("subject")
    message = data.get("message")

    if not subject or not message:
        return jsonify({"error": "subject and message are required"}), 400

    try:
        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = GMAIL_USER
        msg["To"] = TO_EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, TO_EMAIL, msg.as_string())

        return jsonify({"status": "Email sent successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
