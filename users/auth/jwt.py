from rest_framework_jwt.utils import jwt_payload_handler


def school_management_jwt_payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['groups'] = user.get_groups()
    if user.is_superuser:
        payload['superuser'] = True
    return payload
