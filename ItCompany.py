from abc import ABC, abstractmethod

class ShippingProvider(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ship(order : "Order") -> str:
        pass
    
    @abstractmethod
    def calaculate_shipping_cost(order: "Order") -> float:
        pass


class FedEx(ShippingProvider):
    def __init__(self):
        pass

    def ship(order : "Order") -> str:
        return "Shipped with FedEx"

    def calaculate_shipping_cost(order: "Order") -> float:
        pass

class UPS(ShippingProvider):
    def __init__(self):
        pass

    def ship(order : "Order") -> str:
        return "Shipped with UPS"

    def calaculate_shipping_cost(order: "Order") -> float:
        pass


class PaymentMethod(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def pay(amount: float) -> str:
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = card_number
        self._expiration_date = expiration_date
        self._cvv = cvv

    def pay(amount: float) -> str:
        print(f"{amount} payed with Credit Card")


class Cash(PaymentMethod):
    def __init__(self):
        pass

    def pay(amount: float) -> str:
        print(f"{amount} payed cash")


class Article(ABC):
    def __init__(self, price: float, description: str):
        self.price = price
        self.description = description

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description

class Software(Article):
    def __init__(self, price: float, description: str, version: str, download_link: str):
        super().__init__(price, description)
        self._version = version
        self._download_link = download_link

    #frei erfunden nicht im Diagramm
    def get_version(self) -> str:
        return self._version

    #frei erfunden nicht im Diagramm
    def get_download_link(self) -> str:
        return self._download_link


class Hardware(Article):
    def __init__(self, price: float, description: str, stock_quantity:int , model: str, weight: float):
        super().__init__(price, description)
        self._stock_quantity = stock_quantity
        self._model = model
        self._weight = weight

    #frei erfunden nicht im Diagramm
    def get_model(self) -> str:
        return self._model

    #frei erfunden nicht im Diagramm
    def get_stock_quantity(self) -> int:
        return self._stock_quantity

    def get_weight(self) -> float:
        return self._weight


class Customer():
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

class Order():
    def __init__(self, customer: "Customer"):
        self._customer = customer
        self._items = []

    def add_item(self, item: "Article"):
        if item:
            self._items.append(item)

    def remove_item(self, item: "Article"):
        if item and item in self._items:
            self._items.remove(item)

    def total_cost(self) -> float:
        total = 0.0
        for item in self._items:
            total += item.get_price()

        return total


    def total_weight(self) -> float:
        total = 0.0
        for item in self._items:
            if item is Hardware:
                total += item.get_weight()

    def calaculate_shipping_cost(shipping_provider: "Shipping_Provider") -> float:
        return shipping_provider.calaculate_shipping_cost(self)


class ComputerStore():
    def __init__(self, shipping_provider: "Shipping_Provider"):
        self._shipping_provider = shipping_provider
    
    def process_order(self, order: "Order"):
        print("Process Order")
        total_shipping_cost = order.calaculate_shipping_cost(self._shipping_provider)
        print(f"Total shipping cost {total_shipping_cost}")


my_customer = Customer("Tony")
my_order = Order(my_customer)
my_order.add_item(Hardware(120,"NIC", 200.0, "The best", 20.0))
