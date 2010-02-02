#!/usr/bin/python
#TODO: 	* Listar uploaders
#	* Filtrar sources nunca vistas


from subprocess import *
from re import *

def get_active_downloads():
  '''get active downloads from mldonkey server;
  return a list of downloads IDs'''
  get_downloads_cmd = '/usr/lib/mldonkey/mldonkey_command -u admin -p 0 vd downloading \
                       |cut -d] -f1 |grep "\[D" |grep [D.*0-9] |sed -e "s/[^0-9]//g" \
                       |sed "s/^2370//g"' 
  downloads = Popen(get_downloads_cmd, shell=True, stdout=PIPE)
  return downloads.communicate()[0].split('\n')

def get_download_info(d):
  '''get detailed information of a given download ID;
  return a list with such information'''
  download_info = Popen('/usr/lib/mldonkey/mldonkey_command -u admin -p 0\
                          "vd '+ d +'" |grep -v ML|grep -v "^>"',\
                          shell=True, stdout=PIPE)
  return download_info.communicate()[0].split('\n')

def get_active_clients(d):
  '''get active clients from a given download ID; 
  return a list of clients IDs who are sources for that download'''
  active_clients = []
  download_info = get_download_info(d)
  proc = Popen('/usr/lib/mldonkey/mldonkey_command -u admin -p 0 "vd ' + d + ' "|grep -v ML|grep -v "^>" |grep "  \[" |grep -v "(last_ok <never>)" |sed -e "s/\t//g\" |sed -e "s/ //g" |cut -d] -f1 |cut -d[ -f2',shell=True, stdout=PIPE)
#  for i in download_info:
#    if search(r'^  \[[0-9]+]',i):
#      active_clients.append(sub(r'\].*','',sub(r'  \[','',i)))
  return proc.communicate()[0].split('\n')

def get_client_info(c):
  '''get detailed information of a given client ID;
  return a list with such information'''
  client_info = Popen('/usr/lib/mldonkey/mldonkey_command -u admin -p 0\
                          "vc '+ c +'" |grep -v ML|grep -v "^>"',\
                          shell=True, stdout=PIPE)
  return client_info.communicate()[0].split('\n')

def download_info_parser():
  '''get...'''

def client_info_parser():
  '''get...'''

def set_session():
  '''get...'''

# testing
download_info_list = []
active_clients = []
client_info_list = []

active_downloads = get_active_downloads()
for d in active_downloads:
  download_info_list.append(get_download_info(d))
  active_clients = get_active_clients(d)
  for c in active_clients:
    print get_client_info(str(c))[0] + ' --> ' + get_download_info(d)[2]

