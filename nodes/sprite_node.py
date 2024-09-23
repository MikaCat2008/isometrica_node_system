from textures_manager import TexturesManager

from .scene_node import SceneNode


class SpriteNode(SceneNode):
    texture_name: str

    def set_texture(self, texture_name: str) -> None:        
        self.texture_name = texture_name
        self.render()

    def render(self) -> None:
        textures = TexturesManager.get_instance()

        self.image = textures.get_texture(self.texture_name)

    def serialize(self) -> dict:
        return {
            "texture_name": self.texture_name
        } | super().serialize()
    
    def deserialize(self, data: dict) -> None:
        super().deserialize(data)

        texture_name: str = data["texture_name"]

        self.set_texture(texture_name)
