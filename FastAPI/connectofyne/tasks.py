import logging
import ssl
from email.message import EmailMessage

import aiosmtplib
import certifi
from config import config

ssl_context = ssl.create_default_context(cafile=certifi.where())


logger = logging.getLogger(__name__)


class APIResponseError(Exception):
    pass


async def send_mail_async(to: str, subject: str, body: str):
    logger.debug(f"sending mail to {to[:10]}, with subject : {subject[:20]}")
    sender = config.MAIL_APP_SENDER  # os.getenv("DEV_MAIL_APP_SENDER")
    app_password = config.MAIL_APP_PASSWORD  # os.getenv("DEV_MAIL_APP_PASSWORD")

    logger.debug(f"{sender}, {app_password}")

    msg = EmailMessage()
    msg["subject"] = subject
    msg["from"] = sender
    msg["to"] = to
    msg.set_content(f"{body}")
    try:
        await aiosmtplib.send(
            msg,
            hostname="smtp.gmail.com",
            port=465,
            username=sender,
            password=app_password,
            use_tls=True,
            tls_context=ssl_context,
        )
    except Exception as e:
        logger.error(f"{e}")

        raise APIResponseError("problem sending mail") from e

    return {"detail": "mail send successfully"}


async def send_user_registration_email(email: str, confirmation_url: str):
    return await send_mail_async(
        email,
        "Successfully signed up",
        (
            f"hello {email}! you have successfully signed up to connectofyne,"
            f"please confirm your email by clicking on the below link {confirmation_url}"
        ),
    )
