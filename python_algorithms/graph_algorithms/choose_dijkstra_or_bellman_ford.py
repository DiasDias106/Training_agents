import networkx as nx
G = nx.DiGraph()
for row in in_data:
    origem = str(row["origem"])
    destino = str(row["destino"])
    custo = float(row["custo"])
    penalizacao = float(row["penalizacao"])
    peso_total = custo + penalizacao
    print(origem, "->", destino, "custo:", custo, "penalizacao:", penalizacao, "peso_total:", peso_total)
    G.add_edge(origem, destino, weight=peso_total)
    has_negative = any(data["weight"] < 0 for u, v, data in G.edges(data=True))
if has_negative:
    algoritmo = "Bellman-Ford"
else:
    algoritmo = "Dijkstra"
print("\nAlgoritmo recomendado:", algoritmo)