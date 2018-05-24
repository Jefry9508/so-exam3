import psutil

class Stats():

  @classmethod
  def cpuUsed(cls):
    cpuPercent = psutil.cpu_percent()    
    return  cpuPercent

  @classmethod
  def ramUsed(cls):
    ramMemory = psutil.virtual_memory()[1]
    return  ramMemory

  @classmethod   
  def diskUsed(cls):
    diskete = psutil.disk_usage('/')[3]
    return  diskete
