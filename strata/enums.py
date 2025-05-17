from abc import ABC
from dataclasses import dataclass
from enum import Enum, StrEnum, auto
import datetime as dt
from typing import Optional


# High Level Idea

class OpenGammaCCP(StrEnum):
    LCH = auto()
    EUREX = auto()
    CME = auto()
    JSCC = auto()
    SPAN = auto()
    ISDA_SIMM = auto()



# Portfolio formats
# CCPs own format
# Open Gamma's standard forwards

# Data classes for CSV types

class StrataAssetClass(StrEnum):
    FRA = auto()
    SWAP = auto()
    SWAPTION = auto()
    BULLET_PAYMENT = auto()
    TERM_DEPOSIT = auto()
    FX_SINGLE = auto()
    FX_SWAP = auto()
    FX_VANILLA_OPTION = auto()
    CDS = auto()
    CDS_INDEX = auto()
    SECURITY = auto()

class Side(StrEnum):
    BUY = auto()
    SELL = auto()

class StrataBusinessDayAdjustment(StrEnum):
    NO_ADJUST = "NoAdjust"
    FOLLOWING = "Following"
    MODIFIED_FOLLOWING = "ModifiedFollowing"
    PRECEDING = "Preceding"
    MODIFIED_PRECEDING = "ModifiedPreceding"

class StrataCalendar(StrEnum):
    pass

    










