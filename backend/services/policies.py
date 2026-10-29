from backend.data_access import read_csv
from backend.observability.logging import log_event

def list_policies(query="", state="", status=""):
    query=query.lower(); out=[]
    for p in read_csv("policies/schemes.csv"):
        if query and query not in (p['policy_name']+' '+p['eligibility_conditions']).lower(): continue
        if state and p['state']!=state: continue
        if status and p['status']!=status: continue
        out.append(p)
    return out

def ask(question):
    q=question.lower(); states=[p['state'] for p in read_csv("policies/schemes.csv") if p['state'].lower() in q]
    matches=list_policies(state=states[0] if states else "")
    result={"answer":"Local test-data retrieval only. These records are not government policy advice.","matches":matches[:4],"rag_status":"Local test-data retrieval; replace with a grounded RAG pipeline."}
    log_event("rag", "local_policy_search", "Policy test-data search completed", data={"query_length":len(question),"retrieved_count":len(result["matches"]),"fallback":"no_vector_store_configured","citations_returned":0})
    return result
