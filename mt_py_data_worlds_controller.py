from fastapi import FastAPI, HTTPException

from mt_py_data_worlds_service import MtPyDataWorldsService

app = FastAPI()

service = MtPyDataWorldsService()

@app.get("/search_engine")
def runSearch(q = None):
    if q is None:
        raise HTTPException(status_code=400, detail="q is null")
    return service.runSearchEngine(q)

@app.get("/weather_predictor")
def runWeatherPredictor(m = None):
    return service.runWeatherPredictor(m)

@app.get("/gospel_analysis")
def gospel_analysis():
    return service.gospel_analysis()

