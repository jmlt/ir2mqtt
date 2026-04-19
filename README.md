# iR2mqtt - Home Assistant
![Release](https://img.shields.io/github/v/release/jmlt/ir2mqtt)

iR2mqtt is a simple, lightweight, fast, and easy to use bridge application that connects iRacing telemetry data to MQTT, enabling integration with Home Assistant. It uses the open-source [`pyirsdk`](https://github.com/kutu/pyirsdk) library for telemetry reading and [`paho-mqtt`](https://github.com/eclipse/paho.mqtt.python) for MQTT communication.

---

## Installation

### Step 1: Install and Configure MQTT Broker

1. **Install Mosquitto MQTT Broker:**
   - Navigate to **Settings - Add-ons** in Home Assistant
   - Click **Add-on Store**
   - Search for **Mosquitto broker**
   - Install and start the add-on
   
   [![MQTT configuration panel](https://my.home-assistant.io/badges/config_mqtt.svg)](https://my.home-assistant.io/redirect/config_mqtt/)

2. **Configure MQTT credentials:**
   - Go to **Settings - Logins**
   - Create credentials for MQTT
   - Use these credentials in iR2mqtt application

3. **Set up MQTT Integration:**
   
   [![MQTT integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=mqtt)

**Example MQTT Configuration:**

```yaml
logins:
  - username: user
    password: pass
require_certificate: false
certfile: fullchain.pem
keyfile: privkey.pem
customize:
  active: false
  folder: mosquitto
```

---

### Step 2: Download iR2mqtt Application

1. Download the [latest release](https://github.com/jmlt/ir2mqtt/releases/latest) of the iR2mqtt application
2. Configure your MQTT broker settings in the application
3. Run iRacing and the iR2mqtt executable to start sending telemetry data

**Configuration Example:**
<img width="802" height="685" alt="options" src="https://github.com/user-attachments/assets/4f0ecfb3-840a-4888-ad9b-e95cb4f612d1" />


**Running iR2mqtt:**
<img width="802" height="685" alt="dash" src="https://github.com/user-attachments/assets/428b7a77-be95-43d1-87d9-1929d931f710" />

---

### Step 3: Install Home Assistant Integration

#### Option A: Install via HACS (Recommended)

1. Go to **HACS - Integrations**
2. Click the **three-dot menu** (top right) → **Custom repositories**
3. Add the following repository:
   - **Repository URL:** `https://github.com/jmlt/ir2mqtt_integration/`
   - **Category:** `Integration`
4. Click **Add**
5. Search for **iR2mqtt** in HACS and install it

#### Option B: Manual Installation

<details>
<summary>Click to expand manual installation steps</summary>

1. Download the latest release from [GitHub Releases](https://github.com/jmlt/ir2mqtt_integration/releases)
2. Extract the downloaded files
3. Place the `ir2mqtt` folder in your `config/custom_components/` directory
4. Restart Home Assistant

</details>

---

### Step 4: Configure the Integration

1. **Restart Home Assistant** after installing the integration
2. Navigate to **Settings - Devices & Services**
3. Click **Add Integration** and search for **iR2mqtt**
   
   [![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ir2mqtt)

4. Enter the **MQTT Topic Prefix** (default: `iracing`)
5. Click **Submit**

<img width="1052" height="329" alt="HA" src="https://github.com/user-attachments/assets/a8f651ca-45e9-44ad-b35d-a3fe449af875" />

---

## Usage

Once configured, all sensors will be automatically created and available in Home Assistant!

<img width="1425" height="704" alt="sensores" src="https://github.com/user-attachments/assets/aa0cac39-9185-4957-9e80-4ffda812e69a" />

**Try this example automation:** [Flag-based lighting automation](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/automation-example.yaml)

This automation changes light entities according to racing flags with proper priority handling.

---

## Donations

Support the ongoing development of iR2mqtt! Donation keys unlock additional features.

**Donate via PayPal:**

[https://www.paypal.com/donate/?hosted_button_id=CYPAHB9LRC4TN](https://www.paypal.com/donate/?hosted_button_id=CYPAHB9LRC4TN)

**Or scan the QR code:**

![Donation QR Code](https://sys1823.pt/ir2mqtt/files/QR.png)

- Only your **email address** is stored to associate your donation key with the total donated amount
- No other personal data or payment details are stored or handled by iR2mqtt
- Donation keys are **optional** and support ongoing development
- Keys are automatically generated and sent via email (check your SPAM folder)

---

## Legacy Manual Configuration

If you prefer manual sensor configuration, you can still create MQTT sensors manually.

**Reference:** [sensors-example.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml)

**Note:** Manual configuration is **no longer required** with the integration installed.

---
## Requirements

- iR2mqtt app and integration
- MQTT broker (HA Addon and integration)
- iRacing

---

## Transparency: Lite Python Version

A **Lite version** of iR2mqtt is available in the `/python` folder. This version exists **solely** to demonstrate donation key validation and update checking logic transparently. It does **not** implement telemetry reading or MQTT publishing directly, these are handled by the external SDKs and libraries (`pyirsdk` and `paho-mqtt`).

The `main.py` in the Lite version:

- Validates donation keys entered by the user.
- Checks for program updates via GitHub releases.
- Does **not** handle telemetry or MQTT communication itself.

---

## Legal Notice

- **iR2mqtt** is an independent project, **not affiliated, endorsed, or sponsored by iRacing, iRacing.com, or their affiliates.**
- This project uses the open-source libraries [`pyirsdk`](https://github.com/kutu/pyirsdk) and [`paho-mqtt`](https://github.com/eclipse/paho.mqtt.python).
- We do **not** claim any ownership of iRacing software, telemetry data, or trademarks. All rights belong to their respective owners.
- Donations are processed securely via **PayPal**, and only the email provided during donation is stored to associate your donation key and track donations.
- No telemetry or other personal data is collected or shared by iR2mqtt itself.
- Use this software at your own risk. The author(s) disclaim all liability for any damage or loss arising from its use.


## Support

Need help? Found a bug? Have a feature request?

- **iR2mqtt Application:** [GitHub Issues](https://github.com/jmlt/ir2mqtt/issues)
- **Home Assistant Integration:** [GitHub Issues](https://github.com/jmlt/ir2mqtt_integration/issues)
- **Community Discussion:** [Home Assistant Community Forum](https://community.home-assistant.io/t/ir2mqtt-bring-iracing-live-telemetry-to-home-assistant/901589)

Join the project and help improve iR2mqtt!

---

## Useful Links

### Documentation & Examples
- [Automation Example YAML](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/automation-example.yaml)
- [Manual Sensor Configuration Example](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml)

### Project Repositories
- [iR2mqtt Application](https://github.com/jmlt/ir2mqtt)
- [iR2mqtt Home Assistant Integration](https://github.com/jmlt/ir2mqtt_integration)

### Related Resources
- [HACS Documentation](https://hacs.xyz/docs/use)
- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)
- [Home Assistant Community Discussion](https://community.home-assistant.io/t/ir2mqtt-bring-iracing-live-telemetry-to-home-assistant/901589)
