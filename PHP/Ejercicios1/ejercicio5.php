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
  $pintar=true;
    
 //Iniciamos el bucle de las filas
 for($t=0;$t<$filas;$t++){
  echo "<tr>";
  //Iniciamos el bucle de las columnas
  for($y=0;$y<$columnas;$y++){
   if($pintar){
    //Pintamos el cuadro
    echo "<td style=padding:10px;background-color:lightgrey;>".$num."</td>";
    //El próximo no será pintado
    $pintar=false;
    $num++;
   }else{
    //Dejamos cuadro en blanco
    echo "<td style=padding:10px;>".$num."</td>";
    //El próximo será pintado
    $pintar=true;
    $num++;
    }
   }
   //Cerramos columna
   echo "</tr>";
  }
 ?>
 <!-- Cerramos tabla -->
</table>
</body>
</html>
