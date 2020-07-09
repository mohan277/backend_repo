class Item:
    
    def __init__(self, name=None, price=None, category=None):
        if price <= 0:
            raise ValueError(f'Invalid value for price, got {price}')
        self._name = name
        self._price = price
        self._category = category
        
        
    @property
    def name(self):
        return self._name
        
    @property
    def price(self):
        return self._price
        
    @property
    def category(self):
        return self._category
        
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'
    
class Query:
    
    def __init__(self, field=None, value=None, operation=None):
        
        if operation not in ['IN', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']:
            raise ValueError(f'Invalid value for operation, got {operation}')
        
        self._field = field
        self._value = value
        self._operation = operation
        
    @property
    def field(self):
        return self._field
        
    @property
    def operation(self):
        return self._operation
        
    @property
    def value(self):
        return self._value
        
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'

class Store:
    
    def __init__(self, items_in_store=None):
        
        if items_in_store is None:
            self.items_in_store = []
        else:
            self.items_in_store = items_in_store
    
    def __str__(self):
        if len(self.items_in_store) == 0:
            return 'No items'
        else:
            return '\n'.join(map(str,self.items_in_store))
    
    def add_item(self,item):
        self.items_in_store.append(item)
        
    def filter(self, query):
        
        filtered_items = []
        
        for item in self.items_in_store:
            
            get_attr = getattr(item, query.field)
            
            if  query.operation == 'EQ' and get_attr == query.value:
                filtered_items.append(item)
                
            elif  query.operation == 'GT' and get_attr > query.value:
                filtered_items.append(item)
                
            elif  query.operation == 'GTE' and get_attr >= query.value:
                filtered_items.append(item)
                
            elif  query.operation == 'LT' and get_attr < query.value:
                filtered_items.append(item)
                
            elif  query.operation == 'LTE' and get_attr <= query.value:
                filtered_items.append(item)
                
            elif  query.operation == 'STARTS_WITH' and get_attr.startswith(query.value):
                filtered_items.append(item)
                
            elif  query.operation == 'ENDS_WITH' and get_attr.endswith(query.value):
                filtered_items.append(item)
                
            elif  query.operation == 'CONTAINS' and query.value in get_attr:
                filtered_items.append(item)
                
            elif  query.operation == 'IN' and get_attr in query.value:
                filtered_items.append(item)
                
        return Store(filtered_items)
        
    def exclude(self,query):
        
        excluded_list = []
        filter_items = self.filter(query)
        for item in self.items_in_store:
            if item not in filter_items.items_in_store:
                excluded_list.append(item)
        return Store(excluded_list)
    
    def count(self):
        return len(self.items_in_store)