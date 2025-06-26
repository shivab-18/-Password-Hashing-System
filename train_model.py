
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from feature_extractor import extract_features


safe_urls = [
    'https://www.google.com',
    'https://www.amazon.com',
    'https://www.facebook.com',
    'https://www.microsoft.com',
    'https://www.apple.com',
    'https://www.youtube.com',
    'https://www.linkedin.com',
    'https://www.wikipedia.org',
    'https://www.instagram.com',
    'https://www.github.com',
    'https://www.netflix.com',
    'https://www.adobe.com',
    'https://www.nytimes.com',
    'https://www.bbc.com',
    'https://www.reddit.com',
    'https://www.stackoverflow.com',
    'https://www.dropbox.com',
    'https://www.tesla.com',
    'https://www.airbnb.com',
    'https://www.quora.com'
]

phishing_urls = [
    'http://login-facebook.com-security-alert.tk',
    'http://paypal.verification-update-account.com',
    'http://secure-login.google.drive-confirmation.com',
    'http://appleid.apple.com.verify-login.in',
    'http://update-account.netflix.user-login-alert.com',
    'http://amazon-account-verification-check.in',
    'http://dropbox-secure-login.com/account-check',
    'http://secure-paypal.com-account-alert.tk',
    'http://bankofamerica-update-login-info.com',
    'http://www.chase-login-verification.net',
    'http://secure.instant-check-hostinglogin.com',
    'http://microsoft.login.verify-user-alert.com',
    'http://confirm-payment-gateway.online-bill.tk',
    'http://verify-airbnb-support.account-check.com',
    'http://icloud.login-alert-reverify.com',
    'http://update-password-paypal-support.tk',
    'http://malicious-phish-url-confirm.com',
    'http://secureform-fill-identityalert.com',
    'http://verifybankaccount-recoverycheck.net',
    'http://yahoo.login.access-update.tk'
]

urls = safe_urls + phishing_urls
labels = [0] * len(safe_urls) + [1] * len(phishing_urls)

data = {'url': urls, 'label': labels}
df = pd.DataFrame(data)


df['features'] = df['url'].apply(lambda x: extract_features(x))
X = list(df['features'])
y = df['label']


model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('phish_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained with", len(X), "URLs and saved as phish_model.pkl.")
