import spacy
import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
from tqdm import tqdm
from collections import Counter
from pattern.text.de import singularize
import dash
import plotly.express as px
from dash_bootstrap_templates import load_figure_template