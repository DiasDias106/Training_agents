import heapq
import pandas as pd

START = "S"
GOAL = "H"

df = pd.DataFrame(
    in_data.metas,
    columns=[m.name.strip() for m in in_data.domain.metas]
)
for var in in_data.domain.attributes:
    df[var.name.strip()] = [float(in_data[i][var]) for i in range(len(in_data))]

df.columns = df.columns.str.strip()

graph = {}
for _, row in df.iterrows():
    origem = str(row['Origem']).strip()
    destino = str(row['Destino']).strip()
    custo = int(float(row['Custo est']))
    bloq = str(row['Bloqueios']).strip().lower()
    if bloq == 'sim':
        continue
    graph.setdefault(origem, []).append((custo, destino))


def heuristic(node, goal):
    return 0 if node == goal else 1

def astar(graph, start, goal):
    open_list = [(0, 0, start, [start])]
    visited = {}
    nos_explorados = 0
    while open_list:
        prioridade, custo, atual, caminho = heapq.heappop(open_list)
        if atual in visited and visited[atual] <= custo:
            continue
        visited[atual] = custo
        nos_explorados += 1
        if atual == goal:
            return custo, caminho, nos_explorados
        for custo_aresta, vizinho in graph.get(atual, []):
            novo_custo = custo + custo_aresta
            if vizinho not in visited or visited[vizinho] > novo_custo:
                nova_prioridade = novo_custo + heuristic(vizinho, goal)
                heapq.heappush(open_list, (nova_prioridade, novo_custo, vizinho, caminho + [vizinho]))
    return None, [], nos_explorados

custo_total, caminho, nos_explorados = astar(graph, START, GOAL)

if caminho:
    print("=" * 40)
    print(f" A* | {START} → {GOAL}")
    print("=" * 40)
    print(f" Caminho       : {' → '.join(caminho)}")
    print(f" Custo Total   : {custo_total}")
    print(f" Nós Explorados: {nos_explorados}")
    print("=" * 40)
    print("\nDetalhe por passo:")
    for i in range(len(caminho) - 1):
        o = caminho[i]
        d = caminho[i + 1]
        c = next((x for x, v in graph.get(o, []) if v == d), '?')
        print(f"  {o} → {d} (custo: {c})")
    print("-" * 40)
    print(f" Custo Total   : {' + '.join(str(next((x for x, v in graph.get(caminho[i], []) if v == caminho[i+1]), '?')) for i in range(len(caminho)-1))} = {custo_total}")
    print("=" * 40)
else:
    print(f"Sem caminho encontrado entre {START} e {GOAL}.")
    print(f" Nós Explorados: {nos_explorados}")

out_data = in_data