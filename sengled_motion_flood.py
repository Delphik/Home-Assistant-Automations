from zigpy.quirks import CustomDevice
from zigpy.quirks.v2 import CustomCluster
from zigpy.zcl.foundation import DataTypeId
from zigpy.zcl.clusters import general
from zigpy.profiles import zha

class ManuSpecificSengledMotionSensor(CustomCluster):
    cluster_id = 0xfc01
    manufacturer_id = 0x1160
    name = "ManuSpecificSengledMotionSensor"
    attributes = {
        0x0001: ("enable_auto_on_off", DataTypeId.bool_),
        # You can add more attributes later if needed, e.g.:
        # 0x0002: ("off_delay", DataTypeId.uint16),
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
                    0xfc01,  # your manufacturer-specific cluster
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
