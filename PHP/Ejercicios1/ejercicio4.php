 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html>
<head meta charset=utf-8/>
<body>
<table border=1>
     <?php
    //Creamos los parametros iniciales
  $filas = 10;
  $columnas = 10;
  $num = 1;
    
 //Iniciamos el bucle de las filas
 for($t=0;$t<$filas;$t++){
  echo "<tr>";
  //Iniciamos el bucle de las columnas
  for($y=0;$y<$columnas;$y++){
    //decimos que las celdas de las filas se rellenen y autoincrementen el valor hasta ocuparlas todas
    echo "<td>".$num."</td>";
    $num++;
   }
   //Cerramos columna
   echo "</tr>";
  }
 ?>
 <!-- Cerramos tabla -->
</table>
</body>
</html>
