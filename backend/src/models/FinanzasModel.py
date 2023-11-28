from database.dastabase import get_connection


class FinanzasModel():

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
    def get_total_recaudado_alquier_mes(cls, fecha):
        query = """
        SELECT SUM(monto) AS Cantidad_Total_Monto_Recaudado_Alquiler
        FROM alquiler
        WHERE EXTRACT(MONTH FROM Fecha_alquiler) = EXTRACT(MONTH FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, ))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_recaudado_ventas_mes(cls, fecha):
        query = """
        SELECT SUM(monto_final) AS Cantidad_Total_Monto_Recaudado_Venta
        FROM venta
        WHERE EXTRACT(MONTH FROM fecha_venta) = EXTRACT(MONTH FROM CAST(%s AS DATE));
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, ))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_total_recaudado_mes(cls, fecha):
        query = """
        SELECT COALESCE(SUM(monto) + SUM(monto_final), 0) AS Monto_Total_General
        FROM (
            SELECT monto, 0 AS monto_final
            FROM Alquiler
            WHERE EXTRACT(MONTH FROM CAST(%s AS DATE)) = EXTRACT(MONTH FROM fecha_alquiler)

            UNION ALL

            SELECT 0 AS monto, monto_final
            FROM Venta
            WHERE EXTRACT(MONTH FROM CAST(%s AS DATE)) = EXTRACT(MONTH FROM fecha_venta)
        ) AS CombinedData;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (fecha, fecha))
                result = cur.fetchone()
        return result[0] if result else None

    @classmethod
    def get_historial(cls):
        query = """
        SELECT  
            Ar.Nombre_articulo AS Nombre_producto,
            Ar.Tipo_articulo AS Tipo_servicio,
            A.Fecha_alquiler AS Fecha_operacion,
            A.Monto,
            A.Estado_alquiler AS Estado_operacion,
            A.Medio_pago
        FROM
            Alquiler A
        INNER JOIN
            Articulo Ar ON A.Id_articulo = Ar.Id_articulo

        UNION

        SELECT
            A.Nombre_articulo AS Nombre_producto,
            A.Tipo_articulo AS Tipo_servicio,
            V.Fecha_venta AS Fecha_operacion,
            A.Precio_unitario AS Monto,
            V.Estado_pago AS Estado_operacion,
            DV.Medio_pago
        FROM
            Detalle_venta DV
        INNER JOIN
            Venta V ON DV.Id_venta = V.Id_venta
        INNER JOIN
            Articulo A ON DV.Id_articulo = A.Id_articulo;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        return result if result else None
