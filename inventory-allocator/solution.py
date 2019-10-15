class InventoryAllocator:
    def __init__(self, order, warehouses):

        # Initializing order and warehouse variable
        self.order = order
        self.warehouses = warehouses

    def cheapest_shipment(self):
        '''
        Function for calculating
        the cheapest shipment
        based on an order and warehouses
        '''
        # Dictionary for storing total usage of each warehouse for the order
        inventory_usage = {}
        for warehouse in self.warehouses:
            inventory_usage[warehouse["name"]] = {}

        # Iterating over order
        for item in self.order.keys():
            # For each item iterating over warehouses
            for counter in range(len(self.warehouses)):
                total = 0
                # If the warehouse countains the item and the order quantity
                # for that item hasn't been met
                if item in self.warehouses[counter]["inventory"] \
                        and self.order[item] > 0:
                    # Loop over entire quantity untill quantity requirement is
                    # met.
                    while(self.warehouses[counter]["inventory"][item] > 0
                          and self.order[item] > 0):
                        # Subtract from warehouse
                        self.warehouses[counter]["inventory"][item] -= 1
                        # Add to total from warehouse
                        total += 1
                        # Subtract from order quantity
                        self.order[item] -= 1
                        # Set total
                    inventory_usage[self.warehouses[counter]
                                    ["name"]][item] = total
            # If quantity requirement of even a single item isn't met return
            # empty list
            if self.order[item] > 0:
                return []
        # Returns answer in required format
        answer = []
        for key, value in inventory_usage.items():
            if value != {}:
                temp = {key: value}
                answer.append(temp)
        return answer


def main():
    # Test1
    order = {"apple": 1}
    inventory = [{"name": "owd", "inventory": {"apple": 1}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [{'owd': {'apple': 1}}])

    # Test2
    order = {"apple": 1}
    inventory = [{"name": "owd", "inventory": {"apple": 0}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [])

    # Test3
    order = {"apple": 10}
    inventory = [{"name": "owd", "inventory": {"apple": 5}},
                 {'name': 'dm', 'inventory': {'apple': 5}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [
           {'owd': {'apple': 5}}, {'dm': {'apple': 5}}])

    # Test4
    order = {"apple": 10, "orange": 6}
    inventory = [{"name": "owd", "inventory": {"apple": 2, "orange": 3}}, {
        'name': 'dm', 'inventory': {'apple': 12, "orange": 3}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [
           {'owd': {'apple': 2, 'orange': 3}},
           {'dm': {'apple': 8, 'orange': 3}}])

    # Test5
    order = {"apple": 10, "orange": 6}
    inventory = [{"name": "owd", "inventory": {"apple": 2, "orange": 3}}, {
        'name': 'dm', 'inventory': {'apple': 12, "orange": 2}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [])

    # Test6
    order = {"apple": 0, "orange": 0}
    inventory = [{"name": "owd", "inventory": {"apple": 2, "orange": 3}}, {
        'name': 'dm', 'inventory': {'apple': 12, "orange": 2}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [])

    # Test7
    order = {"apple": 10, "orange": 6, "mango": 5}
    inventory = [{"name": "owd",
                  "inventory": {"apple": 2, "orange": 6, "mango": 5}}, {
        'name': 'dm', 'inventory': {'apple': 12, "orange": 3}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [
           {'owd': {'apple': 2, 'orange': 6, 'mango': 5}},
           {'dm': {'apple': 8}}])

    # Test8
    order = {"apple": 10, "orange": 6, "mango": 5}
    inventory = [{"name": "owd",
                  "inventory": {"apple": 8, "orange": 6, "mango": 5}}, {
        'name': 'dm', 'inventory': {'apple': 10, "orange": 3}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [
           {'owd': {'apple': 8, 'orange': 6, 'mango': 5}},
           {'dm': {'apple': 2}}])

    # Test9
    order = {"apple": 10, "orange": 6, "mango": 5}
    inventory = [{"name": "owd", "inventory": {}}]
    test = InventoryAllocator(order, inventory)
    assert(test.cheapest_shipment() == [])
    print("All Tests Passed")




if __name__ == '__main__':
    main()
