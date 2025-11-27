import reflex as rx

config = rx.Config(
    app_name="la_recopa",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
