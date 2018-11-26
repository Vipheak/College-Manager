<?php
//Parametros para configurar para la conexion de la base de datos
$host="localhost";
$basededatos="cm_test";
$usuariodb="root";
$clavedb="";
//Lista de Tablas
$tabla_db1= "users";

$conexion9 = new mysqli($host,$usuariodb,$clavedb,$basededatos);
$conexion9->set_charset("utf8");

if($conexion9->connect_errno){
	echo "Nuestro sitio experimenta fallos...";
	exit();
}
?>