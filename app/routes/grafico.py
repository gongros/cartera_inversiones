from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse
from app.services.datos import cargar_ahorros
from app.services.graficos import graficar_ahorros
import io

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <body>
            <h2>Gráfico de Ahorros</h2>
            <img src="/grafico" alt="Gráfico de ahorros">
        </body>
    </html>
    """

@router.get("/grafico")
def obtener_grafico():
    df = cargar_ahorros()
    fig = graficar_ahorros(df, show=False)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return Response(content=buf.read(), media_type="image/png")
