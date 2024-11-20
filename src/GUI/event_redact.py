from GUI.event_add import AddEventWindow
from DB.init_db import EventManager


class ChangeEventWindow(AddEventWindow):
    def __init__(self, title_: str, size_x: int, size_y: int,
                 *args, **kwargs) -> None:
        super().__init__(title_, size_x, size_y, *args, **kwargs)

        self.show_all_events()

    def show_all_events(self):
        event_manager = EventManager('my_database')
        events = event_manager.get_events()
        print(events)

        # Надо добавить открытие нового окна со всеми имеющимися событиями.


    def change_event(self):
        pass  # Открытие окна изменения. Можно взять окно добавления, но переназвать и сделать механизм переназначения содержимого

