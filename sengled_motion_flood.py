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
        0x0000: ("trigger_condition", t.uint8_t),
        0x0001: ("enable_auto_on_off", t.Bool),
    }

class SengledE13N11(CustomDevice):
    signature = {
        "manufacturer": "sengled",
        "model": "E13-N11",
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
