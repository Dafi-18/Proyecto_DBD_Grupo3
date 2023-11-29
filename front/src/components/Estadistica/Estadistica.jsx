import React, { useEffect, useState } from 'react';

function Estadisticas() {
    const [totalAqlquileresMes, setTotalAlquileresMes] = useState(null);
    const [totalTransacciones, setTotalTransacciones] = useState(null);
    const [totalVentasMes, setTotalVentasMes] = useState(null);
    const [totalPrestamosMEs, setTotalPrestamosMes] = useState(null);
    const [totalRecaudadoAlquilerMes, setTotalRecaudadoAlquilerMes] = useState(null);
    const [totalRecaudadoVentaMes, setTotalRecaudadoVentaMes] = useState(null);
    const [ArtiquloMasAlquiladoMes, setArticuloMasAlquiladoMes] = useState(null);
    const [ArticuloCantidadMasAlquiladoMes, setArticuloCantidadMasAlquiladoMes] = useState(null);
    const [ArticuloMenosAlquilado, setArticuloMenosAlquilado] = useState(null);
    const [ArticuloCantidadMenosAlquilado, setArticuloCantidadMenosAlquilado] = useState(null);
    const [ArticuloMasPrestadoMes, setArticuloMasPrestadoMes] = useState(null);
    const [ArticuloCantidadMasPrestadoMes, setArticuloCantidadMasPrestadoMes] = useState(null);
    const [ArticuloMenosPrestadoMes, setArticuloMenosPrestadoMes] = useState(null);
    const [ArticuloCantidadMenosPrestadoMes, setArticuloCantidadMenosPrestadoMes] = useState(null);
    const [ArticuloMasVendidoMes, setArticuloMasVendidoMes] = useState(null);
    const [ArticuloCantidadMasVendidoMes, setArticuloCantidadMasVendidoMes] = useState(null);
    const [ArticuloMenosVendidoMes, setArticuloMenosVendidoMes] = useState(null);
    const [ArticuloCantidadMenosVendidoMes, setArticuloCantidadMenosVendidoMes] = useState(null);


    useEffect(() => {
        const fecha = '2023-11-28'; // Formato de fecha YYYY-MM-DD

        fetch(`http://localhost:5000/api/estadisticas/total_alquileres_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalAlquileresMes(data);
            })
            .catch(error => console.log('Error fetching artículo menos vendido:', error));

        fetch(`http://localhost:5000/api/estadisticas/total_transacciones_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalTransacciones(data);
            })
            .catch(error => console.log('Error fetching total transacciones:', error));

        fetch(`http://localhost:5000/api/estadisticas/total_ventas_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalVentasMes(data);
            })
            .catch(error => console.log('Error fetching total ventas: ', error));

        fetch(`http://localhost:5000/api/estadisticas/total_prestamos_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalPrestamosMes(data);
            })
            .catch(error => console.log('Error fetcih total prestamos: ', error))

        fetch(`http://localhost:5000/api/estadisticas/total_recaudado_alquiler_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalRecaudadoAlquilerMes(data);

            })
            .catch(error => console.log('Error fetcih total recaudado alquiler: ', error))

        fetch(`http://localhost:5000/api/estadisticas/total_recaudado_venta_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setTotalRecaudadoVentaMes(data);

            })
            .catch(error => console.log('Error fetcih total recaudado ventas: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_mas_alquilado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMasAlquiladoMes(data);

            })
            .catch(error => console.log('Error fetcih articulo mas alquilado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_mas_aquilado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMasAlquiladoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad mas alquilado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_menos_alquilado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMenosAlquilado(data);
            })
            .catch(error => console.log('Error fetcih articulo menos alquilado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_menos_aquilado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMenosAlquilado(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad menos alquilado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_mas_prestado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMasPrestadoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo mas prestado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_mas_prestado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMasPrestadoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad mas prestado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_menos_prestado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMenosPrestadoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo menos prestado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_menos_prestado_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMenosPrestadoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad menos prestado: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_mas_vendido_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMasVendidoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo mas vendido: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_mas_vendido_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMasVendidoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad mas vendido: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_menos_vendido_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloMenosVendidoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo menos vendido: ', error))

        fetch(`http://localhost:5000/api/estadisticas/articulo_cantidad_menos_vendido_mes?fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                setArticuloCantidadMenosVendidoMes(data);
            })
            .catch(error => console.log('Error fetcih articulo cantidad menos vendido: ', error))

    }, []);

    return (
        <div>
            <h1>Estadísticas</h1>
            {totalAqlquileresMes ? <h2>Total de alquileres al mes: {totalAqlquileresMes}</h2> : <p>Cargando alquileres...</p>}
            {totalTransacciones ? <h2>Total de transacciones del mes: {totalTransacciones}</h2> : <p>Cargando transacciones...</p>}
            {totalVentasMes ? <h2>Total de ventas del mes: {totalVentasMes.total_ventas_mes}</h2> : <p>Cargando ventas...</p>}
            {totalPrestamosMEs ? <h2>total de prestamos al mes: {totalPrestamosMEs.total_prestamos_mes}</h2> : <p>Cargando prestamos...</p>}
            {totalRecaudadoAlquilerMes ? <h2>Total recaudado de alquiler al mes: {totalRecaudadoAlquilerMes.total_recaudado_alquiler_mes}</h2> : <p>Cargando recaudado...</p>}
            {totalRecaudadoVentaMes ? <h2>Total recaudado de ventas al mes: {totalRecaudadoVentaMes.total_recaudado_venta_mes}</h2> : <p>Cargando recaudado...</p>}
            {ArtiquloMasAlquiladoMes ? <h2>Articulo mas alquilado del mes: {ArtiquloMasAlquiladoMes.articulo_mas_alquilado_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMasAlquiladoMes ? <h2>Cantidad de articulo mas alquilado del mes: {ArticuloCantidadMasAlquiladoMes.articulo_cantidad_mas_aquilado_mes}</h2> : <p>Cargando cantidad...</p>}
            {ArticuloMenosAlquilado ? <h2>Articulo menos alquilado del mes: {ArticuloMenosAlquilado.articulo_menos_alquilado_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMenosAlquilado ? <h2>Cantidad de articulo menos alquilado del mes: {ArticuloCantidadMenosAlquilado.articulo_cantidad_menos_aquilado_mes}</h2> : <p>Cargando cantidad...</p>}
            {ArticuloMasPrestadoMes ? <h2>Articulo mas prestado del mes: {ArticuloMasPrestadoMes.articulo_mas_prestado_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMasPrestadoMes ? <h2>Cantidad de articulo mas prestado del mes: {ArticuloCantidadMasPrestadoMes.articulo_cantidad_mas_prestado_mes}</h2> : <p>Cargando cantidad...</p>}
            {ArticuloMenosPrestadoMes ? <h2>Articulo menos prestado del mes: {ArticuloMenosPrestadoMes.articulo_menos_prestado_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMenosPrestadoMes ? <h2>Cantidad de articulo menos prestado del mes: {ArticuloCantidadMenosPrestadoMes.articulo_cantidad_menos_prestado_mes}</h2> : <p>Cargando cantidad...</p>}
            {ArticuloMasVendidoMes ? <h2>Articulo mas vendido del mes: {ArticuloMasVendidoMes.articulo_mas_vendido_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMasVendidoMes ? <h2>Cantidad de articulo mas vendido del mes: {ArticuloCantidadMasVendidoMes.articulo_cantidad_mas_vendido_mes}</h2> : <p>Cargando cantidad...</p>}
            {ArticuloMenosVendidoMes ? <h2>Articulo menos vendido del mes: {ArticuloMenosVendidoMes.articulo_menos_vendido_mes}</h2> : <p>Cargando articulo...</p>}
            {ArticuloCantidadMenosVendidoMes ? <h2>Cantidad de articulo menos vendido del mes: {ArticuloCantidadMenosVendidoMes.articulo_cantidad_menos_vendido_mes}</h2> : <p>Cargando cantidad...</p>}


        </div>
    );
}

export default Estadisticas;