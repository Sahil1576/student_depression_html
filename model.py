import pickle
from pathlib import Path

pipeline_file = Path(__file__).parent / "pipeline.pkl"

def load_pipeline():
    with open(pipeline_file,'rb') as f:
        return pickle.load(f)

def prediction(data:dict)->float:

    try:
        model = load_pipeline()

        predicted = int(model.predict(data)[0])
        return predicted
    except Exception as e:
         return {"Error":str(e)}