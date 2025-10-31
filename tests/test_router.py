from src.rag.router import simple_route

def test_simple_route_graph():
    q = "show connected nodes in the graph"
    routes = simple_route(q)
    assert "neo4j" in routes

def test_simple_route_sql():
    q = "count number of forests by state"
    routes = simple_route(q)
    assert "sql" in routes

def test_simple_route_default():
    q = "what is the forest cover of India"
    routes = simple_route(q)
    assert "faiss" in routes
