import reflex as rx

config = rx.Config(
    app_name="LA_RECOPA",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)