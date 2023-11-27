from .entities.Estadisticas import Estadisticas
from database.dastabase import get_connection


class EstadisticasModel:
    @staticmethod
    def get_total_transacciones_mes(fecha):
        query = """
        SELECT COUNT(*) AS Total
        FROM (
            SELECT 'Alquiler'
            FROM Alquiler
            WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM %s)
              AND EXTRACT(YEAR FROM Fecha_alquiler) = EXTRACT(YEAR FROM %s)
            UNION ALL
            SELECT 'Prestamo'
            FROM Prestamo
            WHERE EXTRACT(MONTH FROM Fecha_prestamo) = EXTRACT(MONTH FROM %s)
              AND EXTRACT(YEAR FROM Fecha_prestamo) = EXTRACT(YEAR FROM %s)
            UNION ALL
            SELECT 'Venta'
            FROM Venta
            WHERE EXTRACT(MONTH FROM Fecha_venta) = EXTRACT(MONTH FROM %s)
              AND EXTRACT(YEAR FROM Fecha_venta) = EXTRACT(YEAR FROM %s)
        ) AS transacciones_semana;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha, fecha, fecha, fecha, fecha))
                result = cur.fetchone()
        return result[0] if result else None
