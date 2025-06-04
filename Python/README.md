# iR2mqtt Lite (Python Version)

This folder contains the **Lite** version of iR2mqtt, implemented as simple Python scripts.

---

## Purpose

This Lite version exists **only** to provide a transparent demonstration of:

- Donation key validation logic.
- Update checking against GitHub releases.

It does **not** implement telemetry reading or MQTT communication. Those are handled by the open-source libraries:

- [`pyirsdk`](https://github.com/kutu/pyirsdk) — to read iRacing telemetry.
- [`paho-mqtt`](https://github.com/eclipse/paho.mqtt.python) — to publish telemetry via MQTT.

---

## Included Scripts

- `main.py` — Demonstrates donation key validation and update checking.
- `license_manager.py` — Donation key validation logic.
- `updater.py` — GitHub release update checker.

---

## Donation Key and Privacy

The donation key used by iR2mqtt is generated through a donation made at the following PayPal link:

https://www.paypal.com/donate/?hosted_button_id=CYPAHB9LRC4TN

During the donation process, only your email address is stored to associate your donation key with your total amount donated. No other personal data is collected or stored.

## Legal Notice

- iR2mqtt is an independent project, **not affiliated, endorsed, or sponsored by iRacing or iRacing.com**.  
- This project uses the open-source libraries [`pyirsdk`](https://github.com/kutu/pyirsdk) and [`paho-mqtt`](https://github.com/eclipse/paho.mqtt.python).  
- Donation keys support this project; **only the email address provided during PayPal donation is stored**, solely to associate the donation key with the donor and track total donations.
- Donations are processed securely via **PayPal**, and no payment or personal data beyond the email is stored or handled by iR2mqtt.    
- No telemetry or other personal data is collected or shared.  
- Use at your own risk. No warranty is provided.

---

## Requirements

- Python 3.x
- `requests` (for update checking)
- `paho-mqtt`
- `pyirsdk`

Install dependencies with:

```bash
pip install -r requirements.txt
