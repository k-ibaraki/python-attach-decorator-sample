from typing import Callable, Any
import functools
import flet as ft


def auth_dummy(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return ft.app(__dummy_ft_main)
    return wrapper


def __dummy_ft_main(page: ft.Page) -> None:
    page.add(ft.Text("認証してください"))
