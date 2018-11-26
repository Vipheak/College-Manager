<!DOCTYPE html>
<html lang="es">
<head>
<title>	Iniciar Sesion</title>
<link rel="stylesheet"  href="assets/css/formulario_inicio_sesion.css">
<?php require("menu1.html");  ?>
</head>
<body>

<div class="form">
	<form method="POST" action="pagina.php">
		<br>
		<Center><font size="5px" ><b>Login</b></font></Center>
		<Center><font size="5px" ><b>_____________________________</b></font></Center>
		<br>
		<center><img src="imagenes/usuario.png" width="200px" height="200px" /></center><br>
		<center><label for="username"><b>Nombre de Usuario:</b></label></center>
		<center><input type="text" name="username"  placeholder="Usuario" required ></center><br>	
		<center><label for="password"><b>Contraseña:<b></label></center>
		<center><input type="password" name="password"  placeholder="*********" required ></center><br>
		<center><input type="submit" name="Inicio" value="Iniciar sesion" class="a"></center>
</div>

</body>
</html>
