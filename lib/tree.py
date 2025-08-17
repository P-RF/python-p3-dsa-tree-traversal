class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    queue = [self.root]

    while queue:
      node = queue.pop()

      if node["id"] == id:
        return node

      queue.extend(node["children"])

    return None