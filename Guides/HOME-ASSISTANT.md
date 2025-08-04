![Logo](https://sys1823.pt/ir2mqtt/files/logo.png)

# Creating Home Assistant Sensors

This guide shows how to manually create binary and MQTT sensors in Home Assistant.

---

## Step 1: Open Your `configuration.yaml`

Use your preferred editor to open the `configuration.yaml` file, usually located in the Home Assistant config folder.

---

## Step 2: Add MQTT Sensors

Add the following [yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml) to create sensors for iR2mqtt telemetry data.

[sensors-example.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml)

Replace `iracing` (default) with the MQTT topic prefix you configured in the iR2mqtt app.


## Step 3: Ready!
You can now use ir2mqtt sensors in automations, dashboards etc. Here are some examples: 

[dashboard-view.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/dashboard_view.yaml)

[rgblight-blueprint.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/rgblight-blueprint.yaml)
