import React, { useEffect, useState } from 'react';

function Finanzas() {
    const [totalTransaccionesMes, setTotalTransaccionesMes] = useState(null);
    const [totalRecaudadoAlquilerMes, setTotalRecaudadoAlquilerMes] = useState(null);
    const [totalRecaudadoVentaMes, setTotalRecaudadoVentaMes] = useState(null);
    const [totalRecaudadoMes, setTotalRecaudadoMes] = useState(null);
    const [historial, setHistorial] = useState([]);

    useEffect(() => {
        const fecha = '2023-11-28'; // Formato de fecha YYYY-MM-DD

        fetch(`http://localhost:5000/api/estadisticas/total_transacciones_mes?fecha=${fecha}`)
            .then(res => res.json())
            .then(data => {
                setTotalTransaccionesMes(data);
            })
            .catch(error => console.log('Error fetching total transacciones:', error))

        fetch(`http://localhost:5000/api/finanzas/total_recaudado_alquier_mes?fecha=${fecha}`)
            .then(res => res.json())
            .then(data => {
                setTotalRecaudadoAlquilerMes(data);
            })
            .catch(error => console.log('Error fetching total recaudado alquiler:', error))

        fetch(`http://localhost:5000/api/finanzas/total_recaudado_ventas_mes?fecha=${fecha}`)
            .then(res => res.json())
            .then(data => {
                setTotalRecaudadoVentaMes(data);
            })
            .catch(error => console.log('Error fetching total recaudad venta: ', error))

        fetch(`http://localhost:5000/api/finanzas/total_recaudado_mes?fecha=${fecha}`)
            .then(res => res.json())
            .then(data => {
                setTotalRecaudadoMes(data);
            })
            .catch(error => console.log('Error fetcihg total recaudado: ', error))

    }, []);

    useEffect(() => {
        fetch(`http://localhost:5000/api/finanzas/historial_transacciones`)
            .then(res => res.json())
            .then(data => {
                console.log(data[0]);
                setHistorial(data);
            })
            .catch(error => console.log('Error en el historial: ', error));
    }, []);

    return (
        <div>
            <h1>Finanzas</h1>
            {totalTransaccionesMes ? <h2>Total de transacciones del mes: {totalTransaccionesMes}</h2> : <p>Cargando transacciones...</p>}
            {totalRecaudadoAlquilerMes ? <h2>Total recaudado por alquileres del mes: {totalRecaudadoAlquilerMes}</h2> : <p>Cargando recaudación...</p>}
            {totalRecaudadoVentaMes ? <h2>Total recaudado por venta al mes es: {totalRecaudadoVentaMes} </h2> : <p>Cargando recaudación ...</p>}
            {totalRecaudadoMes ? <h2>Total recaudado por venta y alquiler es: {totalRecaudadoMes} </h2> : <p>Cargando Recaudación total ...</p>}

            <div>
                {Array.isArray(historial) && historial.slice(0, 7).map((transaccion, index) => (
                    <div key={index}>
                        <p>Producto: {transaccion[0]}</p>
                        <p>Tipo: {transaccion[1]}</p>
                        <p>Fecha: {transaccion[2]}</p>
                        <p>Monto: {transaccion[3]}</p>
                        <p>Estado: {transaccion[4]}</p>
                        <p>Método de pago: {transaccion[5]}</p>
                    </div>
                ))}
            </div>

        </div>
    );
}

export default Finanzas;