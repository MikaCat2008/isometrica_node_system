from functools import cache

from pygame.font import Font, SysFont

from .scene_node import SceneNode


@cache
def get_font(size: int) -> Font:
    return SysFont("Arial", size)


class TextNode(SceneNode):
    text: str

    def set_text(self, text: str) -> None:
        if text == self.text:
            return

        self.text = text
        self.render()

    def render(self) -> None:
        self.image = get_font(12).render(self.text, False, (255, 0, 0))

    def serialize(self) -> dict:
        return {
            "text": self.text
        } | super().serialize()
    
    def deserialize(self, data: dict) -> None:
        super().deserialize(data)

        text: str = data["text"]
        
        self.text = text
        self.set_text(text)
