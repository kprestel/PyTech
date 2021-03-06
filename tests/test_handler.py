import pytest
from pytest import approx
import pandas as pd
import pytech.utils.pandas_utils as pd_utils
import pytech.utils.dt_utils as dt_utils
from pytech.data.handler import DataHandler, Bars


# noinspection PyTypeChecker
class TestDataHandler(object):
    """Test the base abstract class"""

    def test_constructor(self):
        """Should always raise a TypeError because it is an abstract class."""
        with pytest.raises(TypeError):
            DataHandler()


# noinspection PyTypeChecker
class TestYahooDataHandler(object):
    """Test the :class:`YahooDataHandler`"""

    def test_constructor(self, events, ticker_list, start_date, end_date):
        """Test the constructor"""
        handler = Bars(events, ticker_list, start_date, end_date)
        assert handler is not None
        handler.update_bars()

        for t in ticker_list:
            df = handler.latest_ticker_data[t][0]
            assert isinstance(df, pd.Series)

    def test_get_latest_bar_value(self, yahoo_data_handler):
        """
        Test getting the latest bar values.

        This test tests two days (a day is when update_bars() is called)
        and asserts that the correct values are present for the tickers.

        :param Bars yahoo_data_handler:
        """
        assert yahoo_data_handler is not None
        # yahoo_data_handler.update_bars()
        aapl_close = (yahoo_data_handler.get_latest_bar_value('AAPL',
                                                                  pd_utils.CLOSE_COL))
        aapl_close_expected = 101.17
        assert aapl_close == approx(aapl_close_expected)
        aapl_open = (yahoo_data_handler
                     .get_latest_bar_value('AAPL', pd_utils.OPEN_COL))
        aapl_open_expected = 101.410004
        assert aapl_open == approx(aapl_open_expected)

        fb_close = (yahoo_data_handler
                        .get_latest_bar_value('FB', pd_utils.CLOSE_COL))
        fb_close_expected = 107.32
        assert fb_close == approx(fb_close_expected)

        fb_open = (yahoo_data_handler
                   .get_latest_bar_value('FB', pd_utils.OPEN_COL))
        fb_open_expected = 107.910004
        assert fb_open == approx(fb_open_expected)

        yahoo_data_handler.update_bars()

        aapl_close = (yahoo_data_handler.get_latest_bar_value(
                'AAPL', pd_utils.CLOSE_COL))
        aapl_close_expected = 102.26
        assert aapl_close == approx(aapl_close_expected)

        fb_close = (yahoo_data_handler.get_latest_bar_value(
                'FB', pd_utils.CLOSE_COL))
        fb_close_expected = 109.410004
        assert fb_close == approx(fb_close_expected)

        with pytest.raises(KeyError):
            yahoo_data_handler.get_latest_bar_value('FAKE', pd_utils.OPEN_COL)

    def test_get_latest_bar_dt(self, yahoo_data_handler):
        """
        Test that the latest date returned is correct.

        :param Bars yahoo_data_handler:
        """
        test_date = yahoo_data_handler.get_latest_bar_dt('AAPL')
        assert test_date == dt_utils.parse_date('2016-03-10')

        yahoo_data_handler.update_bars()

        test_date = yahoo_data_handler.get_latest_bar_dt('AAPL')
        assert test_date == dt_utils.parse_date('2016-03-11')

        yahoo_data_handler.update_bars()

        test_date = yahoo_data_handler.get_latest_bar_dt('AAPL')
        assert test_date == dt_utils.parse_date('2016-03-14')

    def test_get_latest_bar(self, yahoo_data_handler):
        """
        Test getting the latest bar.

        :param Bars yahoo_data_handler:
        :return:
        """
        bar = yahoo_data_handler.get_latest_bar('AAPL')
        dt = dt_utils.parse_date(bar.name)
        adj_close = bar[pd_utils.CLOSE_COL]
        aapl_close_expected = 101.17
        assert dt == dt_utils.parse_date('2016-03-10')
        assert adj_close == approx(aapl_close_expected)
        yahoo_data_handler.update_bars()
        bar = yahoo_data_handler.get_latest_bar('AAPL')
        dt = dt_utils.parse_date(bar.name)
        assert dt == dt_utils.parse_date('2016-03-11')

    def test_make_agg_df(self, yahoo_data_handler: Bars):
        """Test creating the agg df"""
        df = yahoo_data_handler.make_agg_df()

        if 'SPY' not in yahoo_data_handler.tickers:
            # it is expected for there to be 1 more column if the market
            # ticker isn't in the data_handler
            assert len(df.columns) == len(yahoo_data_handler.tickers) + 1
        else:
            assert len(df.columns) == len(yahoo_data_handler.tickers)

