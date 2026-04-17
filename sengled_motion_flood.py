from zigpy.quirks import CustomDevice
from zigpy.quirks.v2 import CustomCluster
import zigpy.types as t
from zigpy.zcl.clusters import general
from zigpy.profiles import zha

class ManuSpecificSengledMotionSensor(CustomCluster):
    cluster_id = 0xfc01
    manufacturer_id = 0x1160
    name = "ManuSpecificSengledMotionSensor"
    attributes = {
        0x0001: ("enable_auto_on_off", t.Bool),
        # Add more later if you want (e.g. off_delay):
        # 0x0002: ("off_delay", t.uint16_t),
    }

class SengledE13N11(CustomDevice):
    signature = {
        "endpoints": {
            1: {
                "profile_id": zha.PROFILE_ID,
                "device_type": 0x0102,  # On/Off Light
                "input_clusters": [
                    general.OnOff.cluster_id,
                    general.LevelControl.cluster_id,
                    0xfc01,
                ],
                "output_clusters": [],
            }
        }
    }
    replacement = {
        "endpoints": {
            1: {
                "input_clusters": [
                    general.OnOff,
                    general.LevelControl,
                    ManuSpecificSengledMotionSensor,
                ],
            }
        }
    }
