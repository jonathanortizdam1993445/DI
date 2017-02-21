<html>
<head meta chrset=utf-8/>
<title>EUROCONVERSOR 1.0</title>
<body>
<p>
    <?php
        $dolares= $_POST['entrada'];//obtenemos el valor introducido anteriormente del formulario
    echo $dolares;
    echo "€";
    echo " = ";
    echo $dolares*1.08;
    echo " $";
    
    
    ?>
</p>
</body>
</html>
