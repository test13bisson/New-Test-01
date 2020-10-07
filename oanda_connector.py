
import configparser
import oandapy as opy 

config = configparser.ConfigParser()
config.read('oanda.cfg')

my_oanda_access_credentials = "$pa33W0rd!"
my_second_oanda_access_credentials = "$pa33W0rd2!"
my_third_oanda_access_credentials = "$pa33W0rd3!"

oanda = opy.API(environment='practice',
                access_token=my_oanda_access_credentials)

awS_secret="7N1645LRTRM7PP8IO9E9T9C3F1EQ8PMP90P40P0K"

aWs_account: "3258-1066-6211"

github_client-id : 'c7674c71c75965b07yyb'

  aWs_account: "3118-2274-6211"

github_client-id : 'c7044c71c75965b07yyb'
