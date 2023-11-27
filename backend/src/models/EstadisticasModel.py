from .entities.Estadisticas import Estadisticas
from database.dastabase import get_connection


class EstadisticasModel:
    @staticmethod
    def get_total_transacciones_mes():
        query = """
        SELECT COUNT(*) AS Total
        FROM (
            SELECT 'Alquiler'
            FROM Alquiler
            WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM CURRENT_DATE)
              AND EXTRACT(YEAR FROM Fecha_alquiler) = EXTRACT(YEAR FROM CURRENT_DATE)
            UNION ALL
            SELECT 'Prestamo'
            FROM Prestamo
            WHERE EXTRACT(MONTH FROM Fecha_prestamo) = EXTRACT(MONTH FROM CURRENT_DATE)
              AND EXTRACT(YEAR FROM Fecha_prestamo) = EXTRACT(YEAR FROM CURRENT_DATE)
            UNION ALL
            SELECT 'Venta'
            FROM Venta
            WHERE EXTRACT(MONTH FROM Fecha_venta) = EXTRACT(MONTH FROM CURRENT_DATE)
              AND EXTRACT(YEAR FROM Fecha_venta) = EXTRACT(YEAR FROM CURRENT_DATE)
        ) AS transacciones_semana;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
        return result[0] if result else None

    # Define similar methods for other queries...
