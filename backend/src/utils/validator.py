import re

def valid_url(url):
    patron = re.compile(
        r'^(https?://)'                # http:// o https://
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,})|localhost)'  # Dominio o localhost
        r'(:\d+)?'                     # Puerto opcional
        r'(/.*)?$'                     # Ruta opcional
    )
    return re.match(patron, url) is not None