# https://strata.opengamma.io/trade_loader/
import datetime as dt
from abc import ABC
from dataclasses import dataclass
from typing import Optional

from strata.enums import Side, StrataAssetClass, StrataBusinessDayAdjustment, StrataCalendar

'''
For each instrument type, there's two methods of entry
* By Convention
* By Full details

Create a data class for each instrument type
* validation function for each entry type
* to_dict() function

For putting together as CSV
* Create list of instruments
* to_dict() on each one
* construct pandas dataframe
* dataframe to CSV



Can use CCP's own formats for their methodology (typically CSV files)
Or OpenGamma's standard formats (Trades, Positions) serialized as XML or JSON

Portfolio Formats
* Standard OTC CSV
* Standard Sensitivity CSV
* OpenGamma Strata
* FpML
* LCH OTC
* Eurex OTC
* Eurex ETD
* CME OTC
* CME ETD
* JSCC OTC
* SPAN
* SIMM


'''

@dataclass
class StrataTradeBase(ABC):
    strata_trade_type = None
    id_scheme: Optional[str]
    id: Optional[int]
    trade_date: Optional[dt.date]
    trade_time: Optional[dt.date]
    trade_zone: Optional[str]
    counterparty_scheme: Optional[str]
    convention: Optional[str]
    buy_sell: Optional[Side]


@dataclass
class StrataFRA(StrataTradeBase):
    strata_trade_type = StrataAssetClass.FRA
    start_date: Optional[dt.date]
    end_date: Optional[dt.date]

    # By Convention
    period_to_start: Optional[str]
    notional: float
    fixed_rate: float
    date_convention: Optional[StrataBusinessDayAdjustment]
    date_calendar: Optional[StrataCalendar]

    # By Full Details
    index: str
    interpolated_index: Optional[str]
    currency: Optional[str]
    notional: float
    day_count: Optional[str]
    fra_discounting_method: Optional[str]
    