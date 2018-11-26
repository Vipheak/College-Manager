<!DOCTYPE html>
<html lang="es">
<head>
<title>	Cualquier paginas</title>
<link rel="stylesheet"  href="assets/css/formulario_grupos.css">
<?php require("menu1.html");  ?>
</head>
<body>
<?php
include("abrir-conexion.php");

if(isset($_POST['Inicio'])){
if(empty($_POST['username']) && empty($_POST['password'])){
	echo "se requiere todos los cambos";
		}

else{
	$username = mysqli_real_escape_string($conexion9, $_POST["username"]);
	$password = mysqli_real_escape_string($conexion9, $_POST["password"]);
	//$password = md5($password);
	$query = "SELECT *FROM users where username = '$username' and password='$password'";
	$result = mysqli_query($conexion9,$query);
	if(mysqli_num_rows($result)> 0){
		echo "<b>Bienvenido $username</b>";}
		else{echo "Hubo un problema";}
	}}	
include("cerrar-conexion.php");
?>
</body>
</html>