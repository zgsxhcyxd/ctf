from enum import Enum

class Area(Enum):
    BJ = "北京"
    SD = "山东"
    SX = "山西"
    HB = "河北"
    JB = "冀北"
    LN = "辽宁"
    JL = "吉林"
    MD = "蒙东"
    HLJ = "黑龙江"
    SXX = "陕西"
    ZSDW = "直属单位"

class TeamPermission(Enum):
    LEADER = "队长"
    MEMBER = "队员"

class Const(object):
    RESULT_KEY = 'result'
    RESULT_CODE = 'code'
    MESSAGE_KEY = 'message'
    STATUS_NOTFOUND = 404
    STATUS_ERROR = 400
    STATUS_DENIED = 401
    STATUS_FORBIDDEN = 403
    STATUS_OK = 200