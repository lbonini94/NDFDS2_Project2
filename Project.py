#%%
import pandas as pd
import numpy as np
import tweepy
import requests
import json

#%%
from tweepy import OAuthHandler
from timeit import default_timer as timer
#%% 
"""
Download programmatically image_predictions.tsv
https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv
"""

#%%
