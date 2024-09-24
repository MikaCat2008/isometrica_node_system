from functools import cache

from pygame.font import Font, SysFont

from .scene_node import SceneNode


@cache
def get_font(size: int) -> Font:
    return SysFont("Arial", size)


class TextNode(SceneNode):
    text: str

    def set_text(self, text: str) -> None:
        self_text = getattr(self, "text", None)
        
        if self_text == text:
            return

        self.text = text
        self.render()

    def render(self) -> None:
        self.image = get_font(12).render(self.text, False, (255, 0, 0))

    def serialize(self) -> dict:
        return {
            "text": self.text
        } | super().serialize()
    
    def initialize(self, data: dict) -> None:
        super().initialize(data)

        text: str = data["text"]

        self.set_text(text)

    def deserialize(self, serialized_data: dict) -> dict:
        text: str = serialized_data["text"]
        
        self.text = text
        self.set_text(text)

        return {
            "text": text
        } | super().deserialize(serialized_data) 
