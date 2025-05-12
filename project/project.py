from binance.client import Client
import time

API_Key = "KWWNkjs5zRDhZrh86xFyqC0D7LZGfq5KUpMYSlg5dyKJPPyNOQmx0tdP5PyMMVKL"
Secret_Key = "cPCbe8J2LR2B3COlJ8d0rPBPTOzutqjm9ntDdh5tf9sUMUVykwcN5BwrFIwgTOGr"

client = Client(API_Key, Secret_Key, testnet = True)
client.get_account()
