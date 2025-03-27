from flaskr.db import get_db

def get_current_api_client():
    db = get_db()
    cursor = db.execute(
        'SELECT id, public_key FROM api_client WHERE id=1;'
    ).fetchone()
    return cursor


def add_api_client(clientId: str):
    db = get_db()
    db.execute(
        'INSERT INTO api_client (id, public_key) VALUES (?,?);', (1, clientId)
    )
    db.commit()


def update_api_client(clientId: str):
    db = get_db()
    db.execute(
        'UPDATE api_client SET public_key=? WHERE id=?', (clientId, 1)
    )
    db.commit()
