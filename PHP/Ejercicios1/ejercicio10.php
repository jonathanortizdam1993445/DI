<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<?php
	define ("TAM", 4); //definimos el tamaño para la tabla 
	function extension(){
		chdir('fotos'); //cambiamos al directorio fotos
		$directorio = getcwd(); //obtenemos el directorio donde estamos y los guardamos en una variable
		$gestor_dir = opendir($directorio); //abrimos un gestor de directorio
		while (false !== ($nombre_fichero = readdir($gestor_dir))) { //bucle para leer los archivos del directorio 
		    $ficheros[] = $nombre_fichero; //guardamos los nombres en el array 
		}
		$bucle = count($ficheros); //creamos una variable que valga la extension del array 
		$i = 0;
		while ($i < $bucle){ //bucle para comprobar extension 
			$comprobar = $ficheros[$i]; //le asignamos a la variable el valor de la posicion 
			$trozo = explode (".", $comprobar); //metodo con el que comprobamos la extension 
			$extensio = end($trozo); //sacamos la extension y la metemos en una variable 
			//comprobamos las extension y añadimos en un nuevo array
			if ($extensio == "jpg"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "gif"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "bmp"){
				$validas[] = $ficheros[$i];
			}else if ($extensio == "png"){
				$validas[] = $ficheros[$i];
			}
			$i++;
			$comprobar = ""; //reiniciamos variables
		}
		return $validas; //devolvemos el array
	}

	function comprobar(){
		$comprobar = extension(); 
		chdir('fotos');
//		chdir('mini'); 
		$i = 0;
		$bucle = count($comprobar); 
		while ($i < $bucle){ //bucle para recorrer tantas veces como grande sea el array
    		if (!file_exists("mini/MINI-".$comprobar[$i])){ //comprueba que exista el archivo
//			chdir('..'); forma distinta de hacerlo 
			system("convert -resize 100x100  ". $comprobar[$i] ." mini/MINI-".$comprobar[$i]); //comando para crear una nueva imagen
		}
		$i++;
		}
	}

	$valida = extension(); //asignamos a una variable el array
	comprobar();
	$numero = 0;
	$bucle2 = count($valida); //creamos una variable que valga la extension del array 
	$fila = 1;
	echo "<table border=1>"; 
	while ($fila <= TAM){ //bucle para hacer la tabla
		print "<tr>";
		for ($j = 1; $j <= TAM; $j++){ //for para recorrer la tabla y asignar las fotos 
			print "<td>" . '<a href=fotos/'.$valida[$numero].'><img src="mini/MINI-'.$valida[$numero].'"/></a>' . "</td>";
			$numero++;
		}
		print "</tr>";
		$fila++;
	}
	echo "</table>";
?>
