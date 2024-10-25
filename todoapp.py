import flet as ft

listaitens = []

def main(page: ft.Page):
    imagem = ft.Image(
        src=f"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUNJQR4qBNndm2q76Lb0SyjOJERl54xbV8tQ&s",
        width= 200,
        height= 200,
        visible=False
    )
    def kkk(e):
       if c2.value == "hahaha":
        imagem.visible=True
        page.add(imagem)
       else:
        page.add(
        ft.Row([
            ft.Checkbox(c2.value),
            ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                    on_click=None)
        ])
       )
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.FIRE_EXTINGUISHER),
        leading_width=40,
        title=ft.Text("To do app"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    c1 = ft.Text("add your todo item bellow")
    c2 = ft.TextField(text_align=ft.TextAlign.CENTER,on_submit=kkk)
    page.add(ft.Text("Nigga"),c1,c2,listaitens)

ft.app(main)