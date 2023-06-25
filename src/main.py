from typer import Typer, Option
from fastapi import FastAPI
from typing_extensions import Annotated
import uvicorn, glob

typer = Typer(
    add_completion=False,
    invoke_without_command=True,
    rich_markup_mode="rich"
    )
api = FastAPI()

@typer.callback()
def main(
    host: str = "0.0.0.0",
    port: int = 8000,
    reload: Annotated[bool, Option("-r", "--reload/--no-reload")] = False
    ):

    """
    [blue]Simple API[/blue] to getting [red]thermal informatoin of Raspberry Pi[/red]

    Try [yellow]`GET http://0.0.0.0:8000/thermal`[/yellow] (as default)
    """
    
    uvicorn.run(
        app="main:api",
        host=host, 
        port=port, 
        reload=reload
    )

@api.get("/thermal")
def thermal():
    file_list = glob.glob('/sys/class/thermal/thermal_zone*/temp')
    temp_array = []

    for file_path in file_list:
        with open(file_path, 'r') as file:
            temp_raw = file.read().strip()
            temp = float(temp_raw)/1000
            temp_array.append(temp)
            print(f"{file_path}: {temp:.3f} °C")

    return temp_array

if __name__ == "__main__":
    typer()
