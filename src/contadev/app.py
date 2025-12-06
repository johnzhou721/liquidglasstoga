import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class OptionScrollApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Scrollable tab
        scroll_box = toga.Box(style=Pack(direction=COLUMN, margin=8))
        for i in range(1, 51):
            row = toga.Box(style=Pack(direction=ROW, align_items='center', margin_bottom=4))
            lbl = toga.Label(f"Item {i}", style=Pack(width=120))
            btn = toga.Button(f"Action {i}", on_press=self._on_item_pressed)
            row.add(lbl)
            row.add(btn)
            scroll_box.add(row)
        self.scroll_container = toga.ScrollContainer(content=scroll_box, flex=1)

        # Simple tab
        other_box = toga.Box(style=Pack(direction=COLUMN, margin=8, background_color="deepskyblue"))
        other_box.add(toga.Label("This is another tab."))
        other_box.add(toga.Button("Do something", on_press=self._on_do_something))
        other_box2 = toga.Box(style=Pack(direction=COLUMN, margin=8, background_color="deepskyblue"))
        other_box2.add(toga.Label("This is another tab."))
        other_box2.add(toga.Button("Do something", on_press=self._on_do_something))

        # Web tab
        webview = toga.WebView(url="https://google.com")

        # Option container
        self.option_container = toga.OptionContainer(
            content=[
                ("Simple", other_box),
                ("Scrollable", toga.ScrollContainer(content=toga.Box(
                    children=[self.scroll_container, toga.Label("Additional Text")], direction=COLUMN
                ))),
                ("Web", webview),  # New Web tab
                ("Option", toga.OptionContainer(content=[
                    ("Hello!", toga.Box(children=[toga.Label("World!")], background_color="deepskyblue"))
                ])),
                ("Scrollable?", toga.ScrollContainer(content=toga.Box(
                    children=[toga.Label(
                        "Additional Text\n" * 25
                                         )]
                ))),
                ("Scrollable!", toga.ScrollContainer(content=toga.Box(
                    children=[toga.Label(
                        "Additional Text\n" * 100
                                         )]
                ), horizontal=False)),
                ("Simple", other_box2),
            ],
            style=Pack(flex=1, background_color="magenta"),
        )

        self.main_window.content = self.option_container
        self.main_window.show()

    def _on_item_pressed(self, widget):
        print("Item pressed")

    def _on_do_something(self, widget):
        print("Do something pressed")


def main():
    return OptionScrollApp()
