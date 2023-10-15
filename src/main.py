"""Thermal Exporter for Raspberry Pi"""
import uvicorn

from typer import Typer, Option
from fastapi import FastAPI
from typing_extensions import Annotated

from thermal.routers.main import router as main_router

typer = Typer(
    add_completion         = False,
    invoke_without_command = True,
    rich_markup_mode       = "rich"
)

api = FastAPI(

)

@typer.callback()
def main(
    host   : str = "0.0.0.0",
    port   : int = 8000,
    reload : Annotated[bool, Option("-r", "--reload")] = False
):

    """
    [blue]Simple API[/blue] to getting [red]thermal informatoin of Raspberry Pi[/red]
    """

    uvicorn.run(
        app   = "main:api",
        host  = host,
        port  = port,
        reload= reload
    )

api.include_router(main_router, prefix="", tags=["main"])

if __name__ == "__main__":
    typer()
