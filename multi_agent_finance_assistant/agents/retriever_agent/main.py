from fastapi import FastAPI
import faiss
import numpy as np

app = FastAPI()

index = faiss.IndexFlatL2(3)
documents = {
    0: "TSMC beat estimates by 4%",
    1: "Samsung missed earnings by 2%",
    2: "Asia tech exposure up from 18% to 22%"
}

vectors = np.array([[0.1, 0.2, 0.3],
                    [0.3, 0.2, 0.1],
                    [0.4, 0.5, 0.6]]).astype('float32')
index.add(vectors)

@app.get("/api/retrieve")
def retrieve(query_vector: list[float]):
    D, I = index.search(np.array([query_vector]).astype('float32'), k=2)
    return {"results": [documents[i] for i in I[0]]}