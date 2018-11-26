<!DOCTYPE html>
<html lang="es">
<head>
<title>	Registro Usuarios</title>
<link rel="stylesheet"  href="#">
<link rel="stylesheet"  href="assets/css/formulario_usuarios.css">
<?php require("menu1.html");  ?>
</head>
<body>
<div class="form">
	<form method="POST" action="registro_users.php">
		<br>
		<Center><font size="5px" ><b>Registro de Usuario:</b></font></Center>
		<Center><font size="5px" ><b>_____________________________________________________</b></font></Center>
		<br>
		<!--<label for="id">ID:</label>
		<input type="number" name="id"  placeholder="1738673" required ><br><br>-->
		<label for="username">Nombre de Usuario:</label>
		<input type="text" name="username"  placeholder="Usuario" required ><br><br>	
		<label for="password">Password:</label>
		<input type="password" name="password"  placeholder="*********" required ><br><br>
		<label for="role">Selecciona el puesto:</label>
 		<select name="role"  title="Selecciones un puesto">
    	<option value="Admin" >Administrador</option>
    	<option value="Profesor" >Maestro</option> 
    	<option value="Alumno">Alumno</option></select><br><br>
		<label for="name">Nombre:</label>
		<input type="text" name="name" required ><br><br>

		<label for="firstSurname">Apellido Paterno:</label>
		<input type="text" name="firstSurname" required ><br><br>

		<label for="secondSurname">Apellido Materno:</label>
		<input type="text" name="secondSurname" required ><br><br>

		<label for="email">Email:</label>
		<input type="email" name="email"  placeholder="user_admin@outlook.com" required ><br><br>
		<label for="phone">Telefono:</label>
		<input type="number" name="phone" required ><br><br>
		<label for="address">Dirección:</label>
		<input type="text" name="address" required ><br><br>
		



		<center>
		<input type="reset"  value="Limpiar" class="a">
		<input type="submit" name="registrar" value="Registrar" class="a"></center>
</div>

<?php

include("abrir-conexion.php");
$id = "";
$nombre_u="";
$password="";
$role = "";
$name = "";
$first = "";
$second = "";
$email= "";
$phone = "";
$address = "";

if(isset($_POST['registrar']))
{	
	//$id = $_POST['id'];s
	$nombre_u=$_POST['username'];
	$password=$_POST['password'];
	//$contra = md5($password);
	$role = $_POST['role'];
	$name = $_POST['name'];
	$first = $_POST['firstSurname'];
	$second = $_POST['secondSurname'];
	$email=$_POST['email'];
	$phone = $_POST['phone'];
	$address = $_POST['address'];

	$sql= "INSERT INTO users values('$id','$nombre_u','$password','$role','$name','$first','$second','$email','phone','$address')";
	//$conexion3->query("INSERT INTO user_fime values('$id','$nombre_u','$password','$email'");
	$ejecutar_1=mysqli_query($conexion9,$sql);
	//verificamos la ejecucion
	if(!$ejecutar_1){
	echo "Hubo algun error";
		}

		else{
	echo"<b>DATOS guardados correctamente</b><br>"; ?>
	<script type="text/javascript">
	function redireccionar(){
 		 window.location='Index.php'
	} 
	setTimeout ("redireccionar()", 00000); //tiempo expresado en milisegundos
	</script><?php
		}

		}	

include("cerrar-conexion.php");
?>

</body>
</html>
