init python:

    class Sms(store.object):
        selected = False
        def __init__(self, sname, simage="", sphoto="", sphoto1=False, mtext=""):
            self.sname = sname
            self.simage = simage 
            self.sphoto = sphoto
            self.sphoto1 = sphoto1
            self.mtext=mtext

    class Sms_box(store.object):
        def __init__(self):
            self.sms_s = []
        def add(self, sms):
            self.sms_s.append(sms)

    class Item(store.object):
        selected = False
        def __init__(self, name, image="", hover_i="", cost=0, note=False, note_image="" ):
            self.name = name
            self.image=image 
            self.cost=cost 
            self.hover_i=hover_i
            self.note=note
            self.note_image=note_image



    class Contact(store.object):
        def __init__(self, name, image_idle="", image_hover="" ):
            self.name = name
            self.image_idle = image_idle 
            self.image_hover = image_hover

    class testItem(Action):
        
        def __init__(self, item, switch, value, remove = True):
            self.item = item
            self.switch = switch
            self.value = value
            self.remove = remove
        
        def __call__(self):
            if store.active_item != None and store.active_item == self.item:
                setattr(store, self.switch, self.value)
                if self.remove:
                    inventory.items.remove(self.item)
                    store.active_item = None
            renpy.restart_interaction()


    class Inventory(store.object):
        def __init__(self, money=0):
            self.money = money
            self.items = []
            self.contact = []
        
        
        
        
        def add(self, item): 
            self.items.append(item)
        
        
        def drop(self, item):
            self.items.remove(item)
        
        def sell(self, item):
            self.money += item.cost
            self.items.remove(item)
        
        def add_contact(self, contact):
            self.contact.append(contact)
            renpy.restart_interaction()
        
        
        
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
                return True
            else:
                return False
        
        def earn(self, amount):
            self.money += amount
        
        def drop_money(self, amount):
            self.money -= amount
        renpy.restart_interaction()
    class selectItem(Action):
        
        def __init__(self, object):
            self.object = object
        
        def __call__(self):
            new_value = not self.object.selected
            for item in inventory.items:
                setattr(item, "selected", False)
            store.active_item = None
            setattr(self.object, "selected", new_value)
            if (new_value):
                store.active_item = self.object
            renpy.restart_interaction()
        
        def get_selected(self):
            return self.object.selected



    class addItem(Action):
        
        def __init__(self, item):
            self.item = item
        
        def __call__(self):
            inventory.items.append(self.item)
        renpy.restart_interaction()

    class addContact(Action):
        
        def __init__(self, contact):
            self.contact = contact
        
        def __call__(self):
            inventory.contact.append(self.contact)
        renpy.restart_interaction()

    class dropItem(Action):
        
        def __init__(self, item):
            self.item = item
        
        def __call__(self):
            inventory.items.remove(self.item)
            renpy.restart_interaction()
    class addSms(Action):
        
        def __init__(self, sms):
            self.sms = sms
        
        def __call__(self):
            sms_box.sms_s.append(self.sms)
            renpy.restart_interaction()