from zigpy.quirks import CustomDevice
from zigpy.quirks.v2 import CustomCluster
import zigpy.types as t
from zigpy.zcl.clusters import general, security, homeautomation
from zigpy.profiles import zha

class ManuSpecificSengledMotionSensor(CustomCluster):
    cluster_id = 0xfc01
    manufacturer_id = 0x1160
    name = "ManuSpecificSengledMotionSensor"
    attributes = {
        0x0001: ("enable_auto_on_off", t.Bool),
        # Optional: add these later if you want them as entities
        # 0x0000: ("trigger_condition", t.uint8_t),
        # 0x0002: ("off_delay", t.uint16_t),
    }

class SengledE13N11(CustomDevice):
    signature = {
        "manufacturer": "sengled",
        "model": "E13-N11",
        "endpoints": {
            1: {
                "profile_id": 0x0104,
                "device_type": 0x0101,
                "input_clusters": [
                    0x0000,  # Basic
                    0x0003,  # Identify
                    0x0004,  # Groups
                    0x0005,  # Scenes
                    0x0006,  # OnOff
                    0x0008,  # LevelControl
                    0x0500,  # IAS Zone (motion sensor)
                    0x0702,  # Simple Metering
                    0x0b05,  # Diagnostics
                    0xfc01,  # Sengled custom motion cluster
                ],
                "output_clusters": [0x0019],  # OTA
            }
        }
    }
    replacement = {
        "endpoints": {
            1: {
                "input_clusters": [
                    general.Basic,
                    general.Identify,
                    general.Groups,
                    general.Scenes,
                    general.OnOff,
                    general.LevelControl,
                    security.IasZone,
                    homeautomation.SimpleMetering,
                    general.Diagnostics,
                    ManuSpecificSengledMotionSensor,   # ← this is what exposes the switch
                ],
                "output_clusters": [general.Ota],
            }
        }
    }
