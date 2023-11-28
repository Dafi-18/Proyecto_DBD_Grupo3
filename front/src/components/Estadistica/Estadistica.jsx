import React, { useEffect, useState } from 'react';

function Estadisticas() {
    const [totalAqlquileresMes, setTotalAlquileresMes] = useState(null);
    const [totalTransacciones, setTotalTransacciones] = useState(null);
    const []

    useEffect(() => {
        const fecha = '2023-11-28'; // Formato de fecha YYYY-MM-DD

        fetch(`http://localhost:5000/api/estadisticas/total_alquileres_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                console.log('Total Alquileres al mes:', data);
                setTotalAlquileresMes(data);
            })
            .catch(error => console.log('Error fetching artículo menos vendido:', error));

        fetch(`http://localhost:5000/api/estadisticas/total_transacciones_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                console.log('Total transacciones:', data);
                setTotalTransacciones(data);
            })
            .catch(error => console.log('Error fetching total transacciones:', error));
    }, []);

    return (
        <div>
            <h1>Estadísticas</h1>
            {articuloMenosVendido && totalTransacciones ? (
                <div>
                    <h2>Total de alquileres al mes: {totalAqlquileresMes}</h2>
                    <h2>Total de transacciones del mes: {totalTransacciones}</h2>
                </div>
            ) : (
                <p>Cargando...</p>
            )}
        </div>
    );
}

export default Estadisticas;