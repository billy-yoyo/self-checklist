
class ScreenSet:
  def __init__(self, finish_url, screens):
    self.finish_url = finish_url
    self.screens = screens

class Screen:
  def __init__(self, items):
    self.items = items

class ScreenItem:
  def __init__(self, item_type) -> None:
    self.item_type = item_type

class ScreenItemText(ScreenItem):
  def __init__(self, body_key):
    super().__init__("body")
    self.body_key = body_key

class ScreenItemImage(ScreenItem):
  def __init__(self, image_name):
    super().__init__("image")
    self.image_name = image_name

class ScreenItemCard(ScreenItem):
  def __init__(self, body_key, image_name, quantity):
    super().__init__("card")
    self.body_key = body_key
    self.image_name = image_name
    self.quantity = quantity


