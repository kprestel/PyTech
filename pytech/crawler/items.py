# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ReportItem(Item):
    # Trading symbol
    symbol = Field()

    # If this doc is an amendment to previously filed doc
    amend = Field()

    # Quarterly (10-Q) or annual (10-K) report
    doc_type = Field()

    # Q1, Q2, Q3, or FY for annual report
    period_focus = Field()

    fiscal_year = Field()
    end_date = Field()

    revenues = Field()
    investment_revenues = Field()
    op_income = Field()
    net_income = Field()
    gross_profit = Field()
    interest_expense = Field()
    research_and_dev_expense = Field()

    eps_basic = Field()
    eps_diluted = Field()

    dividend = Field()

    # Taxes
    tax_expense = Field()
    net_taxes_paid = Field()

    # Balance sheet stuffs
    assets = Field()
    cur_assets = Field()
    acts_pay_current = Field()
    acts_receive_current = Field()
    acts_receive_noncurrent = Field()
    total_liabilities = Field()
    total_liabilities_equity = Field()
    shares_outstanding = Field()
    shares_outstanding_diluted = Field()
    common_stock_outstanding = Field()
    depreciation_amortization = Field()
    cogs = Field()
    comprehensive_income_net_of_tax = Field()
    accrued_liabilities_current = Field()
    warranty_accrual = Field()
    warranty_accrual_payments = Field()
    cur_liab = Field()
    equity = Field()
    cash = Field()
    property_plant_equipment = Field()
    inventory_net = Field()

    # Cash flow from operating, investing, and financing
    cash_flow_op = Field()
    cash_flow_inv = Field()
    cash_flow_fin = Field()


class PriceItem(Item):
    # Trading symbol
    symbol = Field()

    # YYYY-MM-DD
    date = Field()

    open = Field()
    close = Field()
    high = Field()
    low = Field()
    adj_close = Field()
    volume = Field()


class SymbolItem(Item):
    symbol = Field()
    name = Field()