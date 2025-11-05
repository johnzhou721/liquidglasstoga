"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import asyncio


class OptionScrollApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        scroll_box = toga.Box(style=Pack(direction=COLUMN, margin=8))

        for i in range(1, 51):
            row = toga.Box(style=Pack(direction=ROW, align_items='center', margin_bottom=4))
            lbl = toga.Label(f"Item {i}", style=Pack(width=120))
            btn = toga.Button(f"Action {i}", on_press=self._on_item_pressed)
            row.add(lbl)
            row.add(btn)
            scroll_box.add(row)

        self.scroll_container = toga.ScrollContainer(content=scroll_box, flex=1)

        other_box = toga.Box(style=Pack(direction=COLUMN, margin=8))
        other_box.add(toga.Label("This is another tab."))
        other_box.add(toga.Button("Do something", on_press=self._on_do_something))

        self.option_container = toga.OptionContainer(
            content=[
               ("Scrollable", toga.ScrollContainer(content=toga.Box(
                   children=[self.scroll_container, toga.Label("Additional Text")], direction=COLUMN
                ))),
                # ("Scrollable?", toga.ScrollContainer(content=toga.Box(
                #     children=[
                #         toga.Box(direction=COLUMN, flex=1),
                #         toga.Label("Additional Text")
                #     ],
                #     flex=1,
                #     direction=COLUMN
                # ))),
#                ("Scrollable", self.scroll_container),
                ("Simple", other_box),
                ("Option", toga.OptionContainer(content=[
                    ("Hello!", toga.Box(children=[toga.Label("World!")]))
                                                         ]))
            ],
            style=Pack(flex=1),
        )

        self.main_window.content = self.option_container
        self.main_window.show()
        print(self.main_window._impl.container)

    def _on_item_pressed(self, widget):
        print("a")

    def _on_do_something(self, widget):
        print("Do something pressed")

def main():
    return OptionScrollApp()
