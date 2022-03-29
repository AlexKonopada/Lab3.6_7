import random 

class Item:
    '''
    Initilizing an item 
    '''
    def __init__(self, name, price):
        '''
        init of item
        >>> phone = Item('Samsung10', 10000)
        >>> print(phone.price)
        10000
        '''
        self.name = name
        self.price = price
    


class Vehicle:
    '''
    Creating vehicles 
    '''
    def __init__(self, vehicleNo, isAvailable = True):
        '''
        init of Vehicle
        >>> vehicle1 = Vehicle(1)
        >>> print(vehicle1.vehicleNo)
        1
        '''
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

class Location:
    '''
    Location
    '''
    def __init__(self, city, postoffice):
        '''
        location init
        >>> location1 = Location('Lviv', 83)
        >>> print(location1.city)
        Lviv
        '''
        self.city = city
        self.postoffice = postoffice

class Order:
    '''
    Creating order
    '''
    def __init__(self, user_name, city, postoffice, items):
        '''
        order init
        >>> items1 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
        >>> order1 = Order('Andrii', 'Odessa', 3, items1)
        >>> print(order1.user_name)
        Andrii
        >>> print(order1.city)
        Odessa
        '''
        self.orderId = random.randint(1,10)
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items

    def __str__(self):
        '''
        str of item
        order1 = Order('Andrii', 'Odessa', 3, items1)
        print(order1) -> Your order number is (random value from 1 to 10)
        '''
        return f'Your order number is {self.orderId}'
 
    def calculateAmount(self):
        '''
        Calculating the price of the order
        >>> items1 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
        >>> order1 = Order('Andrii', 'Odessa', 3, items1)
        >>> print(order1.calculateAmount())
        164.33
        '''
        summ = 0
        for item in self.items:
            summ += item.price
        return summ

    def assignVehicle(self, vehicle):
        '''
        Using the transport and making it unavailable
        '''
        vehicle.isAvailable = False
        
class LogisticsSystem:
    '''
    The process of sending an order
    '''
    def __init__(self, vehicles = []):   
        """
        logistic system init
        """
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order):
        '''
        Placing the order, by checking the availability of transport
        '''
        for transport in self.vehicles:
            if transport.isAvailable:
                self.orders.append(order) 
                order.assignVehicle(transport)
                break
        else:
            print('There is no available vehicle to deliver an order.')


    def trackOrder(self, orderId):
        '''
        Tracking the order
        '''
        for ord in self.orders:
            if ord.orderId == orderId:
                return f"Your order #{orderId} is sent to {ord.city}. Total price: {ord.calculateAmount()} UAH."
        return 'No such an order'

# if __name__ == '__main__':
#     vehicles = [Vehicle(1), Vehicle(2)]
#     LogSystem = LogisticsSystem(vehicles)
#     my_items1 = [Item('book',110), Item('chupachups',44)]
#     my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items1)
#     print(my_order)
#     LogSystem.placeOrder(my_order)
#     print(LogSystem.trackOrder(my_order.orderId))

#     my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
#     my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
#     print(my_order2)
#     LogSystem.placeOrder(my_order2)
#     print(LogSystem.trackOrder(my_order2.orderId))

#     my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
#     my_order3 = Order('Olesya', "Kyiv", 17, my_items3)
#     print(my_order3)
#     LogSystem.placeOrder(my_order3)
#     print(LogSystem.trackOrder(my_order3.orderId))
if __name__ == '__main__':
    import doctest
    doctest.testmod()