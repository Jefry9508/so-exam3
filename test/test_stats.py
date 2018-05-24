import pytest
from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_used(mocker, client):
  mocker.patch.object(Stats, 'cpuUsed', return_value=100)
  response = client.get('/cpu')
  assert response.data.decode('utf-8') == '{"cpu_used": 100}'
  assert response.status_code == 200 



def test_get_ram_used(mocker, client):
  mocker.patch.object(Stats, 'ramUsed' , return_value=100)
  response = client.get('/ram')
  assert response.data.decode('utf-8') == '{"ram_used": 100}'
  assert response.status_code ==200 

def test_get_disk_used(mocker, client):
  mocker.patch.object(Stats, 'diskUsed' , return_value=100)
  response = client.get('/disk')
  assert response.data.decode('utf-8') == '{"disk_used": 100}'
  assert response.status_code ==200
