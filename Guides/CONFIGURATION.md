# Configuring iR2mqtt

![Logo](https://sys1823.pt/ir2mqtt/files/logo.png)

This guide explains how to configure and use the iR2mqtt app to bridge iRacing telemetry to your MQTT broker, with full control via an intuitive graphical interface.

---

## Requirements

- Python 3.x (for development version) or the compiled executable (`iR2mqtt.exe`).
- A running MQTT broker (local or cloud).
- iRacing installed and running on the same Windows machine as iR2mqtt.

---

## MQTT Broker Setup

We recommend the **official Mosquitto broker add-on for Home Assistant**:

- Go to **Settings > Add-ons** in Home Assistant.
- Click **Add-on Store**, search for **Mosquitto broker**, install and start it.
- Set up credentials under **Settings > People > Users**, and use them in iR2mqtt.

Other supported brokers:

- [Mosquitto (manual)](https://mosquitto.org/download/)
- [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/)

---

## Initial Configuration (via GUI)

When you launch `iR2mqtt.exe` for the first time, the graphical interface opens automatically and allows you to configure all settings, which are saved in a `config.json` file.

### Donation Key

- Optional key generated via donation:
  - [Donate via PayPal](https://www.paypal.com/donate/?hosted_button_id=CYPAHB9LRC4TN)
- Unlocks access to:
  - `on_pit_road` status
  - `active_flags` (e.g., yellow, blue)

> Only your **email address** is stored to associate donations with your key and donation total. No personal data or telemetry is stored or shared.

### iRacing Settings

- **Process name**: Defaults to `iRacingSim64DX11.exe`
- ✅ **Auto detect**: Starts publishing automatically when iRacing is detected
- **Update interval**: How frequently telemetry is sent (default: 1000 ms)

### MQTT Broker Settings

- **Host**: Broker IP or hostname (e.g., `192.168.1.100`)
- **Port**: Default is 1883
- **Username / Password**: If required
- **Topic prefix**: MQTT root topic, e.g. `ir2mqtt`

### General Options (Checkboxes)

- ✅ **Minimize to system tray on close** (enabled by default)
- ⬜ **Start with Windows** (disabled by default)
- ✅ **Auto start publishing when iRacing is detected** (enabled by default)

### Buttons

- 💾 **Save**: Stores settings into `config.json`
- ♻️ **Reset**: Reverts all options to default values
- 🔌 **Test MQTT Connection**: Checks connectivity and credentials

---

## Dashboard Overview

After saving, the app enters the **Dashboard** tab, the main control and monitoring center.

### Controls Section

- ▶️ **Start Publishing**: Begins telemetry publishing (auto-starts if auto-detect is enabled)
- ❌ **Shutdown**: Closes the app completely (not just to tray)

### Status and Telemetry

- 🟢 **iRacing Connection Status**: Displays whether iRacing is currently running and detected
- 📊 **Real-time Telemetry**: Displays current data values as they are sent to MQTT
- 📝 **System Log**: Shows real-time logs of app activity (telemetry sent, errors, broker status, etc.)

---

## Start Publishing (Step-by-Step)

1. Launch `iR2mqtt.exe`.
2. If **Auto detect** is enabled, telemetry publishing starts automatically when iRacing is running.
3. If not, use the **Start Publishing** button in the **Dashboard** tab manually.
4. The app will publish to your MQTT broker using the topic prefix (e.g., `ir2mqtt/speed`, `ir2mqtt/rpm`).

You can monitor everything in real-time from the Dashboard.

---

## Verifying Output

On Home Assistant, navigate to: **Settings > Add-ons > Mosquitto broker** - **Logs**.
You should see entries like:
- `172.30.32.1: Received PUBLISH from ir2mqtt (d0, q0, r0, m0, 'iracing/speed', ...)`

Alternatively use MQTT tools like [MQTT Explorer](http://mqtt-explorer.com/) to check the telemetry.

---

## Logging

The app logs all activity to a file:

- Location: `ir2mqtt.log`
- Includes connection events, telemetry, errors, etc.

---

## Troubleshooting

- **iRacing not detected**: Check the process name matches your iRacing executable.
- **No data on MQTT**: Ensure broker is reachable, credentials are correct, and topics are being published.
- **App closes unexpectedly**: Use the `ir2mqtt.log` file to review the issue.

---

## Useful Links

- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)
- [Mosquitto Broker (Official HA Add-on)](https://github.com/home-assistant/addons/tree/master/mosquitto)
- [iRacing SDK (pyirsdk)](https://github.com/kutu/pyirsdk)
- [Paho MQTT Python](https://github.com/eclipse/paho.mqtt.python)
