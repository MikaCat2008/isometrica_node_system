from kit import Node, GameManager, Serializable
from nodes import SceneNode


class Scene(Serializable):
    game: GameManager
    root_node: Node

    def update(self) -> None:
        self.root_node.update()

    def draw(self) -> None:
        self.game.screen.fill((0, 0, 0))
        self.game.screen.fblits(
            ( 
                node.image, node.position
            )
            for node in self.root_node.get_nodes()
            if isinstance(node, SceneNode)
        )

    def serialize(self) -> dict:
        return {
            "root_node": self.root_node.serialize()
        }
    
    def initialize(self, data: dict) -> None:
        super().initialize(data)

        root_node: Node = data["root_node"]

        self.game = GameManager.get_instance()
        self.game.ticks.register(1, self.update)

        self.root_node = root_node

    def deserialize(self, serialized_data: dict) -> None:
        serialized_root_node: dict = serialized_data["root_node"]

        root_node = Node(serialized_root_node)

        return {
            "root_node": root_node
        }
