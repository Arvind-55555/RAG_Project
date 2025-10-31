def simple_route(q: str):
    ql = q.lower()
    targets = set()
    if any(x in ql for x in ['graph','relationship','connected','path']):
        targets.add('neo4j')
    if any(x in ql for x in ['count','average','sum','group by','select']):
        targets.add('sql')
    if any(x in ql for x in ['news','recent','today','what happened']):
        targets.add('web')
    if not targets:
        targets.add('faiss')
    return list(targets)
