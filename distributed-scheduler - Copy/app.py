from flask import Flask, render_template, request, jsonify
from scheduler import fcfs, sjf, srjf, round_robin
import copy

app = Flask(__name__)

@app.route('/')
def welcome():
    """Welcome page route"""
    return render_template('welcome.html')

@app.route('/simulator')
def simulator():
    """Main scheduling simulator page"""
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.json
    tasks = data['tasks']
    algo = data['algorithm']
    quantum = data.get('quantum', 2)

    if algo == "FCFS":
        result = fcfs(tasks)
    elif algo == "SJF":
        result = sjf(tasks)
    elif algo == "SRJF":
        result = srjf(tasks)
    elif algo == "RR":
        result = round_robin(tasks, quantum)
    else:
        result = []

    return jsonify(result)


def calculate_avg(result):
    if len(result) == 0:
        return 0, 0
    avg_wait = sum(t['waiting_time'] for t in result) / len(result)
    avg_turn = sum(t['turnaround_time'] for t in result) / len(result)
    return avg_wait, avg_turn


@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    tasks = data['tasks']
    quantum = data.get('quantum', 2)

    fcfs_res = fcfs(copy.deepcopy(tasks))['result']
    sjf_res = sjf(copy.deepcopy(tasks))['result']
    srjf_res = srjf(copy.deepcopy(tasks))['result']
    rr_res = round_robin(copy.deepcopy(tasks), quantum)['result']

    comparison = {
        "FCFS": calculate_avg(fcfs_res),
        "SJF": calculate_avg(sjf_res),
        "SRJF": calculate_avg(srjf_res),
        "RR": calculate_avg(rr_res)
    }

    best_algo = min(comparison, key=lambda x: comparison[x][0])

    return jsonify({
        "comparison": comparison,
        "best": best_algo
    })


if __name__ == '__main__':
    app.run(debug=True)