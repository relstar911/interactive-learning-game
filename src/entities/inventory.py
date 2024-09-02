class Item:
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items