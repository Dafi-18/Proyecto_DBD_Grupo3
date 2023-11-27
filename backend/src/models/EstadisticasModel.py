from .entities.Estadisticas import Estadisticas
from database.dastabase import get_connection


class EstadisticasModel:

    @classmethod
    def get_total_transacciones_mes(cls, fecha):
        query = """
        SELECT COUNT(*) AS Total
        FROM (
            SELECT 'Alquiler'
            FROM Alquiler
            WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM CAST(%s AS DATE))
              AND EXTRACT(YEAR FROM Fecha_alquiler) = EXTRACT(YEAR FROM CAST(%s AS DATE))
            UNION ALL
            SELECT 'Prestamo'
            FROM Prestamo
            WHERE EXTRACT(MONTH FROM Fecha_prestamo) = EXTRACT(MONTH FROM CAST(%s AS DATE))
              AND EXTRACT(YEAR FROM Fecha_prestamo) = EXTRACT(YEAR FROM CAST(%s AS DATE))
            UNION ALL
            SELECT 'Venta'
            FROM Venta
            WHERE EXTRACT(MONTH FROM Fecha_venta) = EXTRACT(MONTH FROM CAST(%s AS DATE))
              AND EXTRACT(YEAR FROM Fecha_venta) = EXTRACT(YEAR FROM CAST(%s AS DATE))
        ) AS transacciones_semana;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha, fecha, fecha, fecha, fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_alquileres_mes(cls, fecha):
        query = """
        SELECT COUNT(*) AS Cantidad_Alquileres
        FROM alquiler
        WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM CAST(%s AS DATE))
            AND EXTRACT(YEAR FROM Fecha_alquiler) = EXTRACT(YEAR FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_ventas_mes(cls, fecha):
        query = """
        SELECT COUNT(*) AS Cantidad_venta
        FROM venta
        WHERE EXTRACT(MONTH FROM Fecha_venta) = EXTRACT(MONTH FROM CAST(%s AS DATE))
            AND EXTRACT(YEAR FROM Fecha_venta) = EXTRACT(YEAR FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha))
                result = cur.fetchone()
        print("Resultado:", result)  # Imprime el resultado
        return result[0] if result else None

    @classmethod
    def get_total_prestamos_mes(cls, fecha):
        query = """
        SELECT COUNT(*) AS Cantidad_prestamos
        FROM prestamo
        WHERE EXTRACT(MONTH FROM fecha_prestamo) = EXTRACT(MONTH FROM CAST(%s AS DATE))
            AND EXTRACT(YEAR FROM fecha_prestamo) = EXTRACT(YEAR FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_recaudado_alquier_mes(cls, fecha):
        query = """"
        SELECT SUM(monto) AS Cantidad_Total_Monto_Recaudado_Alquiler
        FROM alquiler
        WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_recaudado_ventas_mes(cls, fecha):
        query = """"
        SELECT SUM(monto_final) AS Cantidad_Total_Monto_Recaudado_Venta
        FROM venta
        WHERE EXTRACT(MONTH FROM fecha_venta) = EXTRACT(MONTH FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_articulo_mas_alquilado_mes(cls, fecha):
        query = """"
        SELECT a.Nombre_articulo
        FROM alquiler al
        JOIN articulo a ON al.Id_articulo = a.Id_articulo
        WHERE EXTRACT(MONTH FROM al.Fecha_alquiler) = EXTRACT(MONTH FROM CURRENT_DATE)
        AND EXTRACT(YEAR FROM al.Fecha_alquiler) = EXTRACT(YEAR FROM CURRENT_DATE)
        GROUP BY a.Nombre_articulo
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha))
                result = cur.fetchone()
        return result[0] if result else None
