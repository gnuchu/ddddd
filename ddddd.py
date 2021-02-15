import yaml 
import json

def read_config(config_file):
  with open(config_file, "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

  return config

config_file = '.config.yaml'
secrets_file= '.secrets.yaml'
secrets = read_config(secrets_file)
config = read_config(config_file)

for x in config['endpoints']:
  print(x)
