import requests
import logging
from threading import Thread
from queue import Queue
import json

def getData(req_data):
    data={}
    sups = ['url1','url2', 'url3', 'url4', 'url5', 'url6', 'url7', 'url8','url9', 'url10']
    q = Queue(maxsize=0)
    num_theads = min(50, len(sups))
    results = [{} for x in sups]
    for i in range(len(sups)):
        q.put((i, sups[i]))

    for i in range(num_theads):
        worker = Thread(target=fetch_data, args=(q, results,req_data))
        worker.setDaemon(True)
        worker.start()

    q.join()
    logging.info('All tasks completed.')
    return results


def fetch_data(q, result, req_data):
    while not q.empty():
        work = q.get()
        try:
            data = requests.post(work[1], json=req_data)
            result[work[0]] = data.json()
        except:
            result[work[0]] = {}
        q.task_done()
    return True

