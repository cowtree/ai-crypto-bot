import numpy as np
from pycoingecko import CoinGeckoAPI
import requests
import snscrape.modules.twitter as sntwitter
import pandas as pd
import textwrap
import datetime as dt
import openai
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import re
import time
import pinecone