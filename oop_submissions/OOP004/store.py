class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        if self.price <= 0:
            raise ValueError(f'ValueError: Invalid value for price, got {self.price}')
        self.category = category
    
    def __str__(self):
        return f'{self.name}@{self.price}-{self.category}'
    
class Query:
    
    def __init__(self, field, operation, value):
        self.field = field
        self.operation = operation
        self.value = value
        OPERATIONS = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if self.operation not in OPERATIONS:
            raise ValueError('Invalid value for operation, got random')
        
    
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'

class Store:
    
    def __init__(self):
        self.items = []
        self.counter = 0
    
    def add_item(self,item):
        self.counter += 1
        self.items.append(item)
    
    def count(self):
        return self.counter
    
    def __str__(self):
        x = self.items
        e = []
        for i in x:
            e.append(str(i))
        if e:
            return '\n'.join(e)
        else:
            return 'No items'
        
    def filter(self,query):
        
        query_items = Store()
        
        for item in self.items:
            
            get_attr = getattr(item,query.field)
            
            if query.operation == 'IN' and get_attr in query.value :
                    query_items.add_item(item)
                    
            if query.operation == 'EQ' and get_attr == query.value :
                    query_items.add_item(item)
                    
            elif query.operation == 'STARTS_WITH' and get_attr.startswith(query.value):
                    query_items.add_item(item)
                    
            elif query.operation == 'ENDS_WITH' and get_attr.endswith(query.value):
                    query_items.add_item(item)
            
            elif query.operation == 'CONTAINS' and query.value in get_attr:
                    query_items.add_item(item)
            
            elif query.operation == 'GT' and get_attr > query.value:
                    query_items.add_item(item)
                    
            elif query.operation == 'GTE' and get_attr >= query.value:
                    query_items.add_item(item)
            
            elif query.operation == 'LT' and get_attr < query.value:
                    query_items.add_item(item)
                    
            elif query.operation == 'LTE'and get_attr <= query.value:
                    query_items.add_item(item)
        
        return query_items
            
    def exclude(self,query):
        excluded_list = Store()
        x = self.filter(query)
        for i in self.items:
            if i not in x.items:
                excluded_list.add_item(i)
        return excluded_list
    
    def __add__(self,other):
        x = list(map(str,self.items + other.items))
        return '\n'.join(x)