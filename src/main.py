from typing import Any, Callable
import flet as ft
from src.decorators.auth import auth_dummy
from src.decorators.attach_decorator import attach_decorator


def main(page: ft.Page) -> None:
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e: Any) -> None:
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e: Any) -> None:
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


@attach_decorator(auth_dummy, is_attached=False)
def run() -> None:
    ft.app(main)


run()
