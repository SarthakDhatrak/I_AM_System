from db import get_db

def authenticate(username, password):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()
    db.close()

    return user

def get_permissions(role):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT permission FROM permissions WHERE role=%s",
        (role,)
    )
    perms = [p[0] for p in cursor.fetchall()]
    db.close()

    return perms
