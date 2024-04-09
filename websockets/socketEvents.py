from enum import Enum

class SocketOnEvent(Enum):
    LOGIN_STATUS = "loginStatus"
    RESPONSE_USER_COUNT = "responseUserCount"
    DELETE_USER_DATA = "deleteUserData"
    EMIT_FROM_CLIENT = "emit_from_client"
    JOIN = "join"
    FORCE_STOP_UPGRADE_PROCESS = "ForceStopUpgradeProcess"
    FORCE_STOP_CONFIG_PROCESS = "ForceStopConfigProcess"
    
class SocketEmitEvent(Enum):
    EMIT_FROM_SESSION_USER = "emit_from_SessionUser"
    EMIT_FROM_SERVER = "emit_from_server"
    FORCE_STOP_UPGRADE_PROCESS_CLIENT = "ForceStopUpgradeProcessClient"
    FORCE_STOP_CONFIGURE_PROCESS_CLIENT = "ForceStopConfigProcessClient"
