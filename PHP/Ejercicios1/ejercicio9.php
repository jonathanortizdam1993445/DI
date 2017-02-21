 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html>
	<head meta charset=utf-8 />
	<body>
		<table border=1 >
			<?php
				function extension(){//la funcion comprueba la extension de los archivos
					chdir('fotos');
					$directorio = getcwd();
					$gestor = opendir($directorio);
					define ("TAM", 4);
					$gestor_dir = opendir($directorio);
					while (false !== ($nombre_fichero = readdir($gestor_dir))) {//leemos los archivos del directorio
					    $ficheros[] = $nombre_fichero;//guardo los archivos en un array
					}
					$bucle = count($ficheros);//guardo la extension del array
					$i = 0;
					while ($i < $bucle){
						$comprobar = $ficheros[$i];
						$trozo = explode (".", $comprobar);//comprobamos la extension
						$extensio = end($trozo);//guardo la extension en una variable
	
						if ($extensio == "jpg"){//comprobamos la extension y los añadimos a un array
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
					return $validas;//devuelve un array de las extensiones
				}
				$valida = extension();//almacenamos en una variable la funcion anterior
				$numero = 0;
				$bucle2 = count($valida);//almacena un array de imagenes
				$fila = 1;
				while ($fila <= TAM){
					print "<tr>";
					for ($j = 1; $j <= TAM; $j++){ 
					//mostramos las imagenes y las enlazamos
						print "<td>" . '<a href=fotos/'.$valida[$numero].'><img src="mini/MINI-'.$valida[$numero].'" width=100 height=100/></a>' . "</td>";
						$numero++;
					}
					print "</tr>";
					$fila++;
				}
			?>
		</table>
	</body>
</html>
