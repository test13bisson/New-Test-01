import configparser
import oandapy as opy 

config = configparser.ConfigParser()
config.read('oanda.cfg')

oanda = opy.API(environment='practice',
                access_token=my_oanda_access_credentials)

awS_secret="7N1645LRYYM7QQ8XX9E8M9C3F1EQ8PMP77P40P0K"

aWs_account: "3258-1074-5578"

github_client-id : 'c7444c71c68965b07cdb'


