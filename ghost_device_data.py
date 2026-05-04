device_components = {
    "outputs": {
        "leds_status": {"led_I": "On", "led_II": "On", "led_III": "On", "led_IV": "On", "led_V": "On"},
        "motor_direction": 270
    },
    "inputs": {
        "tempriture": 23.2,
        "humidity": 60,
        "air_pressure": 101325,
        "acceleration": 1.2,
        "tilt_x": 12,
        "tilt_y": 60
    }
    
}

devices = [
    {"device_id": 1,"device_name": "device A", "components": device_components},
    {"device_id": 2,"device_name": "device B", "components": device_components},
    {"device_id": 3,"device_name": "device C", "components": device_components},
    {"device_id": 4,"device_name": "device D", "components": device_components},
    {"device_id": 5,"device_name": "device E", "components": device_components},
    {"device_id": 6,"device_name": "device F", "components": device_components},
]