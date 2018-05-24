from flask import Flask
import json
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/cpu')
def get_cpu_used():
  cpuInfo = Stats.cpuUsed()
  return json.dumps({'cpu_used': cpuInfo})

@app.route('/ram')
def get_ram_used():
  ramInfo= Stats.ramUsed()
  return json.dumps({'ram_used': ramInfo})

@app.route('/disk')
def get_disk_used():
  diskInfo = Stats.diskUsed()
  return json.dumps({'disk_used': diskInfo})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
