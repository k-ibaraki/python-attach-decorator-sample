from typing import Callable, Any
import functools
import flet as ft


def auth_dummy(func: Callable[..., Any]) -> Callable[..., Any]:

    # ダミーのft.main関数
    def _dummy_ft_main(page: ft.Page) -> None:
        page.add(ft.Text("認証してください"))

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # ft.appにダミーのft.main関数を渡す
        return ft.app(_dummy_ft_main)
    return wrapper
