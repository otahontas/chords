from flask import render_template
from application import app
from application.stats import stats


@app.route("/")
def index():

    stats_for_index = stats.get_all_stats()

    print(stats_for_index)

    return render_template("index.html", stats=stats_for_index)
