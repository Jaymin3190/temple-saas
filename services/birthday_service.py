from api.whatsapp import send_text_message
from database.db import get_connection
from datetime import datetime

MESSAGE_TEMPLATE = (
    "Hare Krishna {name} 🙏\n\n"
    "Wishing you a very happy birthday! "
    "May Sri Sri Radha Krishna bless you always."
)

def process_birthdays():

    conn = get_connection()

    today = datetime.now().strftime("%d-%m")

    query = '''
        SELECT rowid, *
        FROM devotees
    '''

    rows = conn.execute(query).fetchall()

    for row in rows:

        rowid = row[0]
        name = row[2]
        phone = row[3]
        birthday = str(row[4])

        if today in birthday:

            message = MESSAGE_TEMPLATE.format(name=name)

            result = send_text_message(phone, message)

            print(result)

            conn.execute(
                '''
                UPDATE devotees
                SET last_sent_date=?
                WHERE rowid=?
                ''',
                (
                    datetime.now().strftime("%Y-%m-%d"),
                    rowid
                )
            )

            conn.commit()
