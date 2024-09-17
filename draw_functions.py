import matplotlib
from matplotlib import pyplot as plt
import io
from setup import *
import folium

matplotlib.use("Agg")

# Função destinada a gerar imagem do gráfico de Geração X Fitness e retornar o buf da imagem
def draw_plot(x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness') -> None:
    fig, ax = plt.subplots(figsize=(4, 3), dpi=80)
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0) 
    ax.plot(x, y)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig) 
    return buf


# Função destinada a gerar os marcadores e adicionar no mapa
def draw_attractions(map: folium.Map):
    for attraction in ATTRACTIONS:
        popup_content = f"""
        <div style="z-index:1001;">
            <h3>{attraction.name}</h3>
            <img src="{attraction.image_path}" alt="Custom Image" style="width:100px;height:auto;">
            <p>Nota: {attraction.score:.1f}</p>
        </div>
        """

        folium.Marker(
            location=attraction.location,
            tooltip="Clique me!",
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color="green"),
        ).add_to(map)