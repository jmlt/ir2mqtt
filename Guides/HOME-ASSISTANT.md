![Logo](https://sys1823.pt/ir2mqtt/files/logo.png)

# iR2mqtt Home Assistant Integration

No more manual configuration, all sensors are now created automatically.

---

## 🚀 What Is iR2mqtt Integration?

This integration connects [iR2mqtt](https://github.com/jmlt/ir2mqtt) directly with Home Assistant.  
It automatically discovers and creates all telemetry sensors from your iRacing sessions including flags, session data, car telemetry, and more, without the need to edit `configuration.yaml`.

---

## 🧩 Installation

1. Delete the [sensors](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml) section from your configuration.yaml if it was previously added.
2. Install the integration:  
   [https://github.com/jmlt/ir2mqtt_integration](https://github.com/jmlt/ir2mqtt_integration)

---

## 📡 Features

- Automatic sensor discovery (no YAML needed)  
- Organized “iRacing Telemetry” entity group  
- Supports flags, session state, lap data, and more  
- Works with automations and dashboards instantly

---

## 🧠 Manual Setup (Legacy)

If you still prefer manual configuration, you can create MQTT sensors using the example below:

[sensors-example.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml)

But it is **no longer required**.

---

## 💬 Support

- App: [https://github.com/jmlt/ir2mqtt](https://github.com/jmlt/ir2mqtt)  
- Integration: [https://github.com/jmlt/ir2mqtt_integration](https://github.com/jmlt/ir2mqtt_integration)

Join the project, report issues, and help improve iR2MQTT.
