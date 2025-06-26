# feature_extractor.py
import re
from urllib.parse import urlparse

def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(url.count('@'))  # '@' symbol
    features.append(url.count('//') - 1)  # '//' after scheme
    features.append(url.count('-'))  # hyphens
    features.append(1 if url.startswith('https') else 0)  # HTTPS presence
    parsed = urlparse(url)
    domain = parsed.netloc.split(':')[0]
    features.append(len(domain))  # domain length
    return features
