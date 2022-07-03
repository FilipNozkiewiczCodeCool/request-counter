from flask import Flask, Response, request, jsonify, render_template, redirect
from data_handler import read_stats_from_file, write_stats_to_file

app = Flask(__name__)


@app.route("/statistics")
def statistics():
    stats = read_stats_from_file()
    return render_template('statistics.html', stats=stats)


@app.route("/method", methods=["GET"])
def method():
    return render_template('create_stat.html')


@app.route("/request-counter", methods=["GET", "POST", "DELETE", "PUT"])
def request_counter():
    stats = read_stats_from_file()
    stats[request.form.get('mymethod')] += 1
    write_stats_to_file(stats)
    return redirect("statistics")


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")