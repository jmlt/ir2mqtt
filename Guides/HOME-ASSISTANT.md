![Logo](https://sys1823.pt/ir2mqtt/files/logo.png)

# Creating Home Assistant Sensors

This guide shows how to manually create binary and MQTT sensors in Home Assistant.

---

## Step 1: Open Your `configuration.yaml`

Use your preferred editor to open the `configuration.yaml` file, usually located in the Home Assistant config folder.

---

## Step 2: Add MQTT Sensors

Add the following YAML to create sensors for iR2mqtt telemetry data.

Replace `iracing` (default) with the MQTT topic prefix you configured in the iR2mqtt app.

```yaml
# ===========================
# iR2mqtt sensors
# ===========================
mqtt:
  sensor:

    # Speed sensor - car speed in km/h
    - name: "iR2mqtt Speed"
      unique_id: iracing_speed
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.speed | float | round(1) }}"
      unit_of_measurement: "mph"
      device_class: "speed"
      icon: mdi:speedometer
      expire_after: 30

    # Engine RPM sensor
    - name: "iR2mqtt RPM"
      unique_id: iracing_rpm
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.rpm | int }}"
      unit_of_measurement: "RPM"
      icon: mdi:engine
      expire_after: 30

    # Current Gear sensor
    - name: "iR2mqtt Gear"
      unique_id: iracing_gear
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.gear }}"
      icon: mdi:car-shift-pattern
      expire_after: 30

    # Fuel Level sensor
    - name: "iR2mqtt Fuel Level"
      unique_id: iracing_fuel
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.fuel_level | float | round(2) }}"
      unit_of_measurement: "L"
      icon: mdi:gas-station
      expire_after: 30

    # Current Lap sensor
    - name: "iR2mqtt Lap"
      unique_id: iracing_lap
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.lap | int }}"
      unit_of_measurement: "lap"
      icon: mdi:flag-checkered
      expire_after: 30

    # Session Elapsed Time sensor (minutes)
    - name: "iR2mqtt Session Time"
      unique_id: iracing_session_time
      state_topic: "iracing/telemetry"
      value_template: "{{ (value_json.session_time | float / 60) | round(2) }}"
      unit_of_measurement: "min"
      device_class: "duration"
      icon: mdi:clock
      expire_after: 30

    # Session Remaining Time sensor (minutes)
    - name: "iR2mqtt Time Remaining"
      unique_id: iracing_time_remain
      state_topic: "iracing/telemetry"
      value_template: >
        {% if value_json.session_time_remain is defined %}
            {{ (value_json.session_time_remain | float / 60) | round(2) }}
        {% else %}
            {{ states('sensor.iracing_time_remain') | default(0) }}
        {% endif %}
      unit_of_measurement: "min"
      device_class: "duration"
      icon: mdi:clock-end
      expire_after: 30  

    # Session Type sensor
    - name: "iR2mqtt Session Type"
      unique_id: iracing_session_type
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.session_type }}"
      icon: mdi:trophy
      expire_after: 30

    # Session Name sensor
    - name: "iR2mqtt Session Name"
      unique_id: iracing_session_name
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.session_name }}"
      icon: mdi:format-title
      expire_after: 30

    # Active Flags sensor - main active flag or "No Flag"
    - name: "iR2mqtt Active Flag"
      unique_id: iracing_flags
      state_topic: "iracing/telemetry"
      value_template: >
        {{ value_json.active_flags[0] if value_json.active_flags else 'No Flag' }}
      icon: mdi:flag
      json_attributes_topic: "iracing/telemetry"
      json_attributes_template: >
        {
          "all_flags": {{ value_json.active_flags | tojson }},
          "session_flags": {{ value_json.session_flags }}
        }
      expire_after: 30

    # Telemetry Timestamp sensor
    - name: "iR2mqtt Timestamp"
      unique_id: iracing_timestamp
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.timestamp }}"
      icon: mdi:clock-digital
      expire_after: 30

    # Raw flags sensors (True/False for each flag)
    - name: "iR2mqtt Checkered Flag Raw"
      unique_id: iracing_flag_checkered_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Checkered' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt White Flag Raw"
      unique_id: iracing_flag_white_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'White' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Green Flag Raw"
      unique_id: iracing_flag_green_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Green' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Yellow Flag Raw"
      unique_id: iracing_flag_yellow_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Yellow' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Red Flag Raw"
      unique_id: iracing_flag_red_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Red' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Blue Flag Raw"
      unique_id: iracing_flag_blue_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Blue' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Debris Flag Raw"
      unique_id: iracing_flag_debris_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Debris' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Crossed Flag Raw"
      unique_id: iracing_flag_crossed_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Crossed' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Yellow Waving Flag Raw"
      unique_id: iracing_flag_yellow_waving_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Yellow Waving' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Black Flag Raw"
      unique_id: iracing_flag_black_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Black' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Repair Flag Raw"
      unique_id: iracing_flag_repair_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Repair' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Caution Flag Raw"
      unique_id: iracing_flag_caution_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Caution' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt Caution Waving Flag Raw"
      unique_id: iracing_flag_caution_waving_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ 'Caution Waving' in value_json.active_flags }}"
      expire_after: 30

    - name: "iR2mqtt On Pit Road Raw"
      unique_id: iracing_on_pit_road_raw
      state_topic: "iracing/telemetry"
      value_template: "{{ value_json.on_pit_road }}"
      expire_after: 30

binary_sensor:
  - platform: template
    sensors:
      ir2mqtt_checkered_flag:
        friendly_name: "iR2MQTT Checkered Flag"
        value_template: "{{ is_state('sensor.iracing_checkered_flag_raw', 'True') }}"
        icon_template: mdi:flag-checkered

      ir2mqtt_white_flag:
        friendly_name: "iR2MQTT White Flag"
        value_template: "{{ is_state('sensor.iracing_white_flag_raw', 'True') }}"
        icon_template: mdi:flag-outline

      ir2mqtt_green_flag:
        friendly_name: "iR2MQTT Green Flag"
        value_template: "{{ is_state('sensor.iracing_green_flag_raw', 'True') }}"
        icon_template: mdi:flag-variant

      ir2mqtt_yellow_flag:
        friendly_name: "iR2MQTT Yellow Flag"
        value_template: "{{ is_state('sensor.iracing_yellow_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_red_flag:
        friendly_name: "iR2MQTT Red Flag"
        value_template: "{{ is_state('sensor.iracing_red_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_blue_flag:
        friendly_name: "iR2MQTT Blue Flag"
        value_template: "{{ is_state('sensor.iracing_blue_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_debris_flag:
        friendly_name: "iR2MQTT Debris Flag"
        value_template: "{{ is_state('sensor.iracing_debris_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_crossed_flag:
        friendly_name: "iR2MQTT Crossed Flag"
        value_template: "{{ is_state('sensor.iracing_crossed_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_yellow_waving_flag:
        friendly_name: "iR2MQTT Yellow Waving Flag"
        value_template: "{{ is_state('sensor.iracing_yellow_waving_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_black_flag:
        friendly_name: "iR2MQTT Black Flag"
        value_template: "{{ is_state('sensor.iracing_black_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_repair_flag:
        friendly_name: "iR2MQTT Repair Flag"
        value_template: "{{ is_state('sensor.iracing_repair_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_caution_flag:
        friendly_name: "iR2MQTT Caution Flag"
        value_template: "{{ is_state('sensor.iracing_caution_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_caution_waving_flag:
        friendly_name: "iR2MQTT Caution Waving Flag"
        value_template: "{{ is_state('sensor.iracing_caution_waving_flag_raw', 'True') }}"
        icon_template: mdi:flag

      ir2mqtt_on_pit_road:
        friendly_name: "iR2MQTT On Pit Road"
        value_template: "{{ is_state('sensor.iracing_on_pit_road_raw', 'True') }}"
        icon_template: mdi:pit

# ===========================
# End of iR2mqtt sensors
# ===========================

```
As seen at [sensors-example.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/sensors-example.yaml)


## Step 3: Ready!
You can now use ir2mqtt sensors in automations, dashboards etc. Here are some examples: 

[dashboard-view.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/dashboard_view.yaml)

[rgblight-blueprint.yaml](https://github.com/jmlt/ir2mqtt/blob/main/Guides/yaml/rgblight-blueprint.yaml)
