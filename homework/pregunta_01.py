# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    # ------------------------------------------------------------
    # 1. Rutas base
    # ------------------------------------------------------------
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, "..", "data", "shipping-data.csv")
    data_path = os.path.normpath(data_path)

    docs_path = os.path.join(base_path, "..", "docs")
    os.makedirs(docs_path, exist_ok=True)

    # ------------------------------------------------------------
    # 2. Cargar datos
    # ------------------------------------------------------------
    df = pd.read_csv(data_path)

    # ------------------------------------------------------------
    # 3. Figuras
    # ------------------------------------------------------------

    # Figura 1: Warehouse_block
    plt.figure(figsize=(6,4))
    df["Warehouse_block"].value_counts().plot(kind="bar")
    plt.title("Shipping per warehouse")
    plt.xlabel("Warehouse block")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(docs_path, "shipping_per_warehouse.png"))
    plt.close()

    # Figura 2: Mode_of_Shipment
    plt.figure(figsize=(6,4))
    df["Mode_of_Shipment"].value_counts().plot(kind="bar")
    plt.title("Mode of shipment")
    plt.xlabel("Mode")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(docs_path, "mode_of_shipment.png"))
    plt.close()

    # Figura 3: Customer_rating
    plt.figure(figsize=(6,4))
    df["Customer_rating"].plot(kind="hist", bins=5)
    plt.title("Average customer rating")
    plt.xlabel("Rating")
    plt.tight_layout()
    plt.savefig(os.path.join(docs_path, "average_customer_rating.png"))
    plt.close()

    # Figura 4: Weight_in_gms
    plt.figure(figsize=(6,4))
    df["Weight_in_gms"].plot(kind="hist", bins=20)
    plt.title("Weight distribution")
    plt.xlabel("Weight (g)")
    plt.tight_layout()
    plt.savefig(os.path.join(docs_path, "weight_distribution.png"))
    plt.close()

    # ------------------------------------------------------------
    # 4. Crear index.html
    # ------------------------------------------------------------
    html_content = """
<!DOCTYPE html>
<html>
<body>

<h1>Shipping Dashboard Example</h1>

<div style="width:45%; float:left;">
    <img src="shipping_per_warehouse.png" alt="Fig 1">
    <img src="mode_of_shipment.png" alt="Fig 2">
</div>

<div style="width:45%; float:left;">
    <img src="average_customer_rating.png" alt="Fig 3">
    <img src="weight_distribution.png" alt="Fig 4">
</div>

</body>
</html>
"""

    with open(os.path.join(docs_path, "index.html"), "w") as f:
        f.write(html_content)
