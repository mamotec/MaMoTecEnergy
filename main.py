from fastapi import FastAPI

from modbus.read_modbus import read_holding_registers

app = FastAPI()


@app.get("/")
def root():
    result = read_holding_registers().registers
    print(result)
    return {tuple(result)}
