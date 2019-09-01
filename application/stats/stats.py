from sqlalchemy.sql import text
from application.auth.models import User
from application import db

# TODO: toisteista koodia, abstrahoi jos mahdollista

def get_userstats_for_chords():
    stmt = text(" SELECT account.id, COUNT(account.id) as counter"
                " FROM account"
                " LEFT JOIN chord ON chord.account_id = account.id"
                " GROUP BY account.id"
                " HAVING COUNT(chord.id) > 0"
                " ORDER BY counter DESC"
                " LIMIT 5")
    users = []
    for row in db.engine.execute(stmt):
        user = User.query.get(row[0])
        users.append({'username': user.username, 'count': row[1]})
    return users


def get_userstats_for_songs():
    stmt = text(" SELECT account.id, COUNT(account.id) as counter"
                " FROM account"
                " LEFT JOIN song ON song.account_id = account.id"
                " GROUP BY account.id"
                " HAVING COUNT(song.id) > 0"
                " ORDER BY counter DESC"
                " LIMIT 5")
    users = []
    for row in db.engine.execute(stmt):
        user = User.query.get(row[0])
        users.append({'username': user.username, 'count': row[1]})
    return users


def get_all_stats():
    stats = {
        "mostChords": get_userstats_for_chords(),
        "mostSongs": get_userstats_for_songs()
    }
    return stats
