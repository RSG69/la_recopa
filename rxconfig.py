import reflex as rx

config = rx.Config(
    app_name="la_recopa",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
