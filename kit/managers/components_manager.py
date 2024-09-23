from .manager import Manager
from .component import Component


class ComponentsManager(Manager):
    component_factories: dict[str, type[Component]]
    
    def __init__(self) -> None:
        super().__init__()

        self.component_factories = {}

    def register_components(self, components: list[type[Component]]) -> None:
        for node in components:
            self.component_factories[node.__name__] = node

    def deserialize_component(self, data: dict) -> Component:
        component_name: str = data["__component_name__"]
        factory = self.component_factories[component_name]
        
        return factory(data)
