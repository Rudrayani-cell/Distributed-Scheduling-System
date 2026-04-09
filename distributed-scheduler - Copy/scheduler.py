# ================= FCFS =================
def fcfs(tasks):
    tasks.sort(key=lambda x: x['arrival_time'])
    time = 0
    result = []
    timeline = []

    for task in tasks:
        if time < task['arrival_time']:
            time = task['arrival_time']

        start = time

        for _ in range(task['burst_time']):
            timeline.append({"task": task['task_id'], "time": time})
            time += 1

        finish = time

        result.append({
            "task": task['task_id'],
            "start": start,
            "finish": finish,
            "waiting_time": start - task['arrival_time'],
            "turnaround_time": finish - task['arrival_time']
        })

    return {"result": result, "timeline": timeline}


# ================= SJF =================
def sjf(tasks):
    tasks = sorted(tasks, key=lambda x: x['arrival_time'])
    time = 0
    result = []
    timeline = []
    ready = []

    while tasks or ready:
        while tasks and tasks[0]['arrival_time'] <= time:
            ready.append(tasks.pop(0))

        if ready:
            ready.sort(key=lambda x: x['burst_time'])
            task = ready.pop(0)

            start = time

            for _ in range(task['burst_time']):
                timeline.append({"task": task['task_id'], "time": time})
                time += 1

            finish = time

            result.append({
                "task": task['task_id'],
                "start": start,
                "finish": finish,
                "waiting_time": start - task['arrival_time'],
                "turnaround_time": finish - task['arrival_time']
            })
        else:
            timeline.append({"task": "Idle", "time": time})
            time += 1

    return {"result": result, "timeline": timeline}


# ================= SRJF =================
def srjf(tasks):
    tasks = sorted(tasks, key=lambda x: x['arrival_time'])
    remaining = {t['task_id']: t['burst_time'] for t in tasks}
    time = 0
    result = []
    timeline = []
    done = set()

    while len(done) < len(tasks):
        available = [t for t in tasks if t['arrival_time'] <= time and t['task_id'] not in done]

        if available:
            task = min(available, key=lambda x: remaining[x['task_id']])

            timeline.append({"task": task['task_id'], "time": time})
            remaining[task['task_id']] -= 1

            if remaining[task['task_id']] == 0:
                finish = time + 1
                start = finish - task['burst_time']

                result.append({
                    "task": task['task_id'],
                    "start": start,
                    "finish": finish,
                    "waiting_time": finish - task['arrival_time'] - task['burst_time'],
                    "turnaround_time": finish - task['arrival_time']
                })

                done.add(task['task_id'])
        else:
            timeline.append({"task": "Idle", "time": time})

        time += 1

    return {"result": result, "timeline": timeline}


# ================= ROUND ROBIN =================
def round_robin(tasks, quantum):
    tasks = sorted(tasks, key=lambda x: x['arrival_time'])
    time = 0
    queue = []
    result = []
    timeline = []

    remaining = {t['task_id']: t['burst_time'] for t in tasks}
    i = 0

    while i < len(tasks) or queue:
        while i < len(tasks) and tasks[i]['arrival_time'] <= time:
            queue.append(tasks[i])
            i += 1

        if queue:
            task = queue.pop(0)
            exec_time = min(quantum, remaining[task['task_id']])

            start = time

            for _ in range(exec_time):
                timeline.append({"task": task['task_id'], "time": time})
                time += 1

            remaining[task['task_id']] -= exec_time

            if remaining[task['task_id']] > 0:
                while i < len(tasks) and tasks[i]['arrival_time'] <= time:
                    queue.append(tasks[i])
                    i += 1
                queue.append(task)
            else:
                finish = time
                result.append({
                    "task": task['task_id'],
                    "start": start,
                    "finish": finish,
                    "waiting_time": finish - task['arrival_time'] - task['burst_time'],
                    "turnaround_time": finish - task['arrival_time']
                })
        else:
            timeline.append({"task": "Idle", "time": time})
            time += 1

    return {"result": result, "timeline": timeline}