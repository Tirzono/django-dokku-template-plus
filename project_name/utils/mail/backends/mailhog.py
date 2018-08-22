from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SmtpEmailBackend


class EmailBackend(SmtpEmailBackend):
    """
    Email backend to use with mailhog.
    """
    def __init__(self, fail_silently=False, use_ssl=None, timeout=None, ssl_keyfile=None, ssl_certfile=None, **kwargs):
        super().__init__(host=settings.EMAIL_BACKEND_MAILHOG_HOST, port=settings.EMAIL_BACKEND_MAILHOG_PORT,  # nosec
                         username='', password='',  use_tls=False, fail_silently=fail_silently,
                         use_ssl=use_ssl, timeout=timeout, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile, **kwargs)

