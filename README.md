
# 📧 Email Account Compromise Detection Tool

This project demonstrates how to simulate and detect suspicious activity in corporate email accounts through real-time log generation. Using Python and the `Faker` library, it mimics user behavior across various locations, devices, and MFA statuses to help identify patterns that could indicate account compromise (e.g., brute-force attempts, MFA bypass, location-based anomalies).

---

## 🚀 Features

* **Simulated Real-Time Logs**: Generates logs using randomly synthesized user data.
* **Suspicious Activity Detection**: Detects anomalies based on:

  * Location mismatch (e.g., access from outside India),
  * Disabled Multi-Factor Authentication (MFA),
  * Critical actions like password changes.
* **Audio Alerts**: Plays a beep sound when suspicious behavior is detected.
* **Log Visualization**: Live printed logs with highlights for anomalies.
* **Export to CSV**: All simulated logs are saved locally for audit or further analysis.

---

## 📁 File Structure

| File Name                                       | Description                                  |
| ----------------------------------------------- | -------------------------------------------- |
| `Email Account Compromise Detection Tool.ipynb` | Main script that performs the simulation.    |
| `simulated_icici_logs.csv`                      | Output log file generated during simulation. |

---

## 🛠️ Requirements

Make sure you have the following Python libraries installed:

```bash
pip install faker openpyxl
```

These are used for:

* `faker`: Generating fake but realistic user log data.
* `openpyxl`: Supporting Excel export (if extended in future versions).

---

## 🧠 Logic Behind Suspicion Detection

Each log entry is evaluated based on a few simple but effective rules:

| Parameter | Rule to Flag Suspicion                     |
| --------- | ------------------------------------------ |
| Location  | Not equal to `India`                       |
| MFA       | Status is `Disabled`                       |
| Action    | Action is `Change` (e.g., password change) |

If any of the above conditions are met, an alert is triggered.

---

## 💡 How It Works

1. The script uses the `Faker` library to create pseudo-random email access logs.
2. Each log includes:

   * Timestamp
   * Email address (`@icicibank.com`)
   * Access location
   * Device used
   * MFA status
   * Action performed
3. Each entry is printed live.
4. If the entry is flagged suspicious:

   * A warning is displayed in the console.
   * An audio alert is played using NumPy and IPython.

---

## 📦 Output

After the simulation ends, all 500 generated logs are exported to a file:

```
simulated_icici_logs.csv
```

This can be used for further analysis or visualization.

---

## 🔒 Purpose

The project is purely educational and designed to help understand:

* How account access patterns can indicate compromise.
* The value of MFA and geo-based access control.
* How to simulate and monitor logs in a security audit environment.

---

## 📌 Notes

* Designed for **educational/cybersecurity awareness** purposes only.
* All data is randomly generated and does **not** reflect any real ICICI Bank infrastructure or user data.
* Can be extended to support real-time dashboarding or integrate with SOC tools.

---

## 🤝 Contributing & Extending

You're welcome to fork the notebook and modify it to:

* Integrate email alerting via SMTP.
* Add IP address and browser fingerprinting.
* Store logs in a database for live dashboarding.

---

## 👨‍💻 Author

**Karan Shukla**
