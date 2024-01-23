import pandas as pd
from sentence_transformers import SentenceTransformer, util
import chromadb 
from chromadb.utils import embedding_functions

def cargar_datos(csv):
    df = pd.read_csv(csv)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(df['details'],batch_size=64,show_progress_bar=True)
    df["embeddings"] = embeddings.tolist()
    df['ids'] = df.index
    df['ids'] = df['ids'].astype('str')
    chroma_client = chromadb.Client()
    client_persistent = chromadb.PersistentClient("D:\loopPY\db")
    db = client_persistent.create_collection(name = "impovadb")
    db.add(
        ids = df["ids"].tolist(),
        embeddings =df['embeddings'].tolist(),
        metadatas= df.drop(['ids','embeddings'],axis=1).to_dict('records')    )
    print(df)
    
def get_data_chroma(query):
    
    try :
        
        client_persistent = chromadb.PersistentClient('D:\loopPY\db') 
        db = client_persistent.get_collection(name='impovadb')

        results = db.query(
            query_texts=[query],
            n_results=1
        )
    
        return(str(results['metadatas'][0][0]['details'])) 
    except Exception:  
        print('error ' + str(Exception))
    
#print(get_data_chroma("cuanto cuesta la core I5"))
#cargar_datos("D:\loopPY\csv\database.csv")

#database