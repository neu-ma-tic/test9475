from __future__ import annotations
import logging
import os
import hikari
import lightbulb

from pathlib import Path

log = logging.getLogger(__name__)


class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self._extensions = [
            p.stem for p in Path(".").glob("./protótipo/extensões/*.py")
        ]

        super().__init__(
            token = os.environ['TOKEN'],
            default_enabled_guilds = 781888263857504266,
            owner_ids =626593759798231040,
            case_insensitive_prefix_commands = True,
            intents = hikari.Intents.ALL,
            banner = None,
            prefix = lightbulb.when_mentioned_or('#'),
            delete_unbound_commands = True,
        )

    def run(self) -> None:
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)

        super().run(activity=hikari.Activity(
            name="/help • Version 0.1.0",
            type=hikari.ActivityType.WATCHING,
        ))

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        for ext in self._extensions:
            try:
                self.load_extensions(f"protótipo.extensões.{ext}")
                log.info(f"Extensão {ext} carregada.")
            except Exception as e:
                log.critical(f"ERRO: Extensão {ext} não pode ser carregada.")
                print(e) 
        

    async def on_started(self, event: hikari.StartedEvent) -> None:
        log.info("Aplicação iniciada.")

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        log.info("Aplicação terminada.")

