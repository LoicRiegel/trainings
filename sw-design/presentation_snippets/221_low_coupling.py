def check_email_validity(email: Email):
    if not email.valid:
        raise Exception("Email is invalid")
