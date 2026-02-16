import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List


# ===== OOP КЛАСС =====
@dataclass
class Disease:
    name: str
    symptoms: List[str]
    medicines: List[str]
    severity: float = 0.0


# ===== СОЗДАНИЕ ГРАФА =====
def create_graph():
    G = nx.Graph()

    flu = Disease("Грипп", ["Температура", "Кашель"], ["Парацетамол"])
    cold = Disease("Простуда", ["Кашель", "Насморк"], ["Ибупрофен"])

    diseases = [flu, cold]

    for disease in diseases:
        G.add_node(disease.name)

        for symptom in disease.symptoms:
            G.add_node(symptom)
            G.add_edge(disease.name, symptom)

        for medicine in disease.medicines:
            G.add_node(medicine)
            G.add_edge(disease.name, medicine)

    return G


def find_related_entities(graph, start_node):
    if start_node not in graph:
        return []
    return list(graph.neighbors(start_node))


# ===== STREAMLIT =====
st.title("Медицинский Knowledge Graph 🩺")

G = create_graph()

all_nodes = list(G.nodes())
selected_node = st.selectbox("Выберите узел:", all_nodes)

if st.button("Найти связи"):
    results = find_related_entities(G, selected_node)
    st.success(f"{selected_node} связан с: {', '.join(results)}")

st.write("### Визуализация графа")

fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    edge_color='gray',
    node_size=2000,
    font_size=10,
    ax=ax
)

st.pyplot(fig)

