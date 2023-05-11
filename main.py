#Симулятор магазину одягу
class Clothing:
    def __init__(self, material, name, price, size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def search_items(self, keyword):
        result = []
        for item in self.inventory:
            if keyword.lower() in item.name.lower():
                result.append(item)
        return result
    def info_inventory(self):
        if len(self.inventory) == 0:
            print("Інвентар пустий")
        else:
            print("Інвентар:")
            for item in self.inventory:
                print(f"- {item.name} ({item.size}): ${item.price}")
class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self,item):
        if item.price <= self.budget:
            self.cart.append(item)
            self.budget -= item.price
            print(f'{item.name} додано до кошика')
        else:
            print('Недостатньо коштів.')
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.budget += item.price
            print(f'{item.name} видалено з кошика')
        else:
            print(f'{item.name} немає в кошику')
    def view_cart(self):
        if len(self.cart) == 0:
            print('Кошик порожній')
        else:
            print('Кошик:')
            for item in self.cart:
                print(f'{item.name} ({item.size}): {item.price}')
    def checkout(self):
        total_price = sum(item.price for item in self.cart)
        if total_price <= self.budget:
            self.cart = []
            self.budget -= total_price
            print('Оплата пройшла успішно!')
        else:
            print('Недостатньо коштів для оформлення замовлення.')

clothing1 = Clothing("Синтетика", "Футболка", 20, "M")
clothing2 = Clothing("Тканина", "Штани", 70, "L")
clothing3 = Clothing("Тканина", "Футболка", 40, "S")
store = Store("Clothing Store", "вул.Соборна 10")
store.add_item(clothing1)
store.add_item(clothing2)
store.add_item(clothing3)
customer = Customer("Олександр", 130)
search_keyword = "футболка"
search_results = store.search_items(search_keyword)
if len(search_results) > 0:
    item_to_add = search_results[0]
    customer.add_to_cart(item_to_add)
else:
    print("По даному ключу немає товару")
customer.view_cart()
total_purchase_price = sum(item.price for item in customer.cart)
print(f"Сума покупки: {total_purchase_price}")
item_to_remove = clothing1
customer.remove_from_cart(item_to_remove)
customer.view_cart()
customer.checkout()
