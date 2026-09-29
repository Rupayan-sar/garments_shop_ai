from pydantic import BaseModel


class Tool(BaseModel):
    product: str | None = None
    cost_per_unit: float | None = None
    total_cost_price: float | None = None
    sell_per_unit: float | None = None
    total_selling_price: float | None = None
    profit: float | None = None
    loss: float | None = None
    loss_per_unit: float | None = None
    quantity: int | None = None
    profit_per_unit: float | None = None


def check(cost_per_unit, sell_per_unit, quantity):

    total_cost_price = cost_per_unit * quantity
    total_selling_price = sell_per_unit * quantity

    if total_selling_price > total_cost_price:
        return "Profit"

    elif total_selling_price == total_cost_price:
        return "No Profit or Loss"

    else:
        return "Loss"


def calculate_profit(cost_per_unit, sell_per_unit, quantity):

    total_cost_price = cost_per_unit * quantity
    total_selling_price = sell_per_unit * quantity

    profit = total_selling_price - total_cost_price

    return profit


def calculate_loss(cost_per_unit, sell_per_unit, quantity):

    total_cost_price = cost_per_unit * quantity
    total_selling_price = sell_per_unit * quantity

    loss = total_cost_price - total_selling_price

    return loss


def calculate_profit_per_unit(cost_per_unit, sell_per_unit):

    profit_per_unit = sell_per_unit - cost_per_unit

    return profit_per_unit


def calculate_loss_per_unit(cost_per_unit, sell_per_unit):

    loss_per_unit = cost_per_unit - sell_per_unit

    return loss_per_unit