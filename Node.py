from typing import Optional


class Node:
    """
    Класс, представляющий узел красно-черного дерева.
    """

    def __init__(self, value: object, color: str) -> None:
        """
        Инициализация узла.

        Args:
            value (object): Значение узла
            color (str): Цвет узла ("красный" или "черный")
        """
        self.value = value
        self.color = color
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

