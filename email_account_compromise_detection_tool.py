# -*- coding: utf-8 -*-
"""Email Account Compromise Detection Tool.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E_7yfp_0TgZHklDEJ-tuWIshwzMGJLkk

Simulated Real Time Logs
"""

!pip install faker
!pip install openpyxl

from google.colab import files
uploaded = files.upload()

import pandas as pd
from faker import Faker
from datetime import datetime
import random
import time
import numpy as np
from IPython.display import Audio, display, clear_output

# Initialize Faker and parameters
fake = Faker()
logs = []

# Predefined fields
locations = ['India', 'Japan', 'Canada', 'Nepal', 'Germany']
devices = ['Chrome on Windows', 'Edge on Windows', 'Safari on iPhone', 'Firefox on Linux']
mfa_status = ['Enabled', 'Disabled']
actions = ['Login', 'Change']

# Function to generate a log
def generate_log():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": fake.email(domain="icicibank.com"),
        "location": random.choice(locations),
        "device": random.choice(devices),
        "mfa": random.choice(mfa_status),
        "action": random.choice(actions)
    }

# Function to determine if a log is suspicious
def is_suspicious(log):
    if log['location'] != 'India' or log['mfa'] == 'Disabled' or log['action'] == 'Change':
        return True
    return False

# Function to play beep
def play_alert():
    frequency = 880  # Hz
    duration = 1.0   # Seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    display(Audio(wave, rate=sample_rate, autoplay=True))

# Main simulation loop
print("🔁 Starting real-time log stream...")
for i in range(500):
    log = generate_log()
    logs.append(log)

    clear_output(wait=True)
    print(f"🧾 Log #{i+1}: {log}")

    # Check for suspicious activity
    if is_suspicious(log):
        print("🚨 Suspicious activity detected! Playing alert...")
        play_alert()
    else:
        print("✅ Log is clean.")

    time.sleep(2)  # wait for 2 seconds

# Save all logs after simulation
df_logs = pd.DataFrame(logs)
df_logs.to_csv("simulated_icici_logs.csv", index=False)
print("\n✅ Simulation complete. Logs saved to simulated_icici_logs.csv")

