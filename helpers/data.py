import uuid

PASSWORD = "Gfhjkm0001"
NAME = "abzal"

def generate_email():
    unique_id = uuid.uuid4().hex[:12]
    return f"abzal_rakhymbayev_{unique_id}@yandex.ru"
