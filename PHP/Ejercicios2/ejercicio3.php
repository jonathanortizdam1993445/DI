<?php
define("TAM",4); //definimos la tabla 4x4
$uploads_dir =  $_SERVER['DOCUMENT_ROOT']."/Ejercicios2/fotos"; //ruta que queremos utilizar 
		$name = $_FILES['imagen']['name']; //Obtenemos el nombre del archivo subido
		move_uploaded_file($_FILES['imagen']['tmp_name'], $uploads_dir."/".$name); //Movemos la imagen subida al destino que queremos.
function extension(){ //definimos la función que comprobará la extensión 
	chdir('fotos'); 
	$directorio = getcwd();
	$gestor = opendir($directorio);
	$gestor_dir = opendir($directorio);
	while (false !== ($nombre_fichero = readdir($gestor_dir))) { //leemos los archivos del directorio en el que estamos
	    $ficheros[] = $nombre_fichero; //guardamos esos archivos en un array
	}
	$bucle = count($ficheros); //guardamos la extensión del array
	$i = 0;
	while ($i < $bucle){ //comprobamos la extensión
		$comprobar = $ficheros[$i]; 
		$trozo = explode (".", $comprobar); //función con la que comprobamos la extensión
		$extensio = end($trozo); //guardamos la extensión en una variable
	
		if ($extensio == "jpg"){ //vamos comprobando las extensiones y las añadimos a un array nuevo
			$validas[] = $ficheros[$i];
		}else if ($extensio == "gif"){
			$validas[] = $ficheros[$i];
		}else if ($extensio == "bmp"){
			$validas[] = $ficheros[$i];
		}else if ($extensio == "png"){
			$validas[] = $ficheros[$i];
		}
	$i++;
	$comprobar = "";
	}
return $validas; //devolvemos el array con las extensiones
}

function comprobar(){ //función para comprobar si hay minis de nuestras fotos
	$comprobar = extension(); 
	chdir('fotos');
	$i = 0;
	$bucle = count($comprobar); 
	while ($i < $bucle){ //bucle que recorre el array de fotos
    	if (!file_exists("mini/-".$comprobar[$i])){ //comprobamos si existe el archivo
		system("convert -resize 100x100  ". $comprobar[$i] ." mini/MINI-".$comprobar[$i]); //si no existe lo creamos
	}
	$i++;
	}
}

$valida = extension(); //guardamos el array en una variable
comprobar();
$bucle2 = count($valida); //creamos una variable para guardar las extensiones de las imagenes				
$num=0;
$fila=1;
print "<table border=\"1\">\n"; //imprimimos la tabla                  
while($fila<=TAM){ //creamos las filas
	print "<tr>";		                    				                            			  	   
	for ($i = 1; $i <= TAM; $i++){	//creamos las columnas, definimos un enlace para poder hacer cada imagen grande y las asignamos en cada celda  
		print "<td>" . '<a href=fotos/'.$valida[$num].'><img src="fotos/'.$valida[$num].'"width=100 height=100/></a>' . "</td>";
		$num++; 
	}
print "</tr>";
$fila++; 
}			                  
print "</table>\n"; 
?>
