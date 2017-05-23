#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use DBI;

my $cgi = CGI->new;
my $cookie = $cgi->cookie('ESPIANGEL');

my @carray;
@carray=split('=',$cookie);
#print $a->header;
#print $carray[1];

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $sql="select username from users where username='$carray[1]'";

my $statement = $dbh->prepare($sql);

# execute your SQL statement
$statement->execute();
my @data;
@data = $statement->fetchrow_array();
	my $username = $data[0];

print $cgi->header(-charset => 'UTF-8');

if(defined $username && $username ne ''){

my $html = qq{
<html lang="en-us">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>EspiAngel Servidor</title>

	<!-- Load fonts -->
	<link href='http://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Lora' rel='stylesheet' type='text/css'>

	<!-- Load css styles -->
	<link rel="stylesheet" type="text/css" href="../css/bootstrap.css" />
	<link rel="stylesheet" type="text/css" href="../css/font-awesome.css" />
	<link rel="stylesheet" type="text/css" href="../css/style.css" />
        <link rel="shortcut icon" href="../ea1.ico">
        <script type="text/javascript">(function() {var walkme = document.createElement('script'); walkme.type = 'text/javascript'; walkme.async = true; walkme.src = 'https://cdn.walkme.com/users/12d0730106694bcdb08e1e2f8e9bf4a6/test/walkme_12d0730106694bcdb08e1e2f8e9bf4a6_https.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(walkme, s); window._walkmeConfig = {smartLoad:true}; })();</script>

</head>
<body>
	<div class="jumbotron home home-fullscreen" id="home">
		<div class="mask"></div>
		<a href="#" class="logo">
			<img src="../ea.png" width="70" height="70" norder-radius="2px">
		</a>
		<a href="" class="menu-toggle" id="nav-expander"><i class="fa fa-bars"></i></a>
		<!-- Offsite navigation -->
		<nav class="menu">
			<a href="#" class="close"><i class="fa fa-close"></i></a>
			<h3>Menu</h3>
			<ul class="nav">
				<li><a data-scroll href="#home">EA Server</a></li>
				<li><a data-scroll href="#services">Servicios</a></li>
				<li><a data-scroll href="#cambio">Cambiar Contraseña</a></li>
				<li><a data-scroll href="#datos">Cambiar datos personales</a></li>
				<li><a data-scroll href="#baja">Dar de baja</a></li>
				<li><a data-scroll href="#status">Status</a></li>
				<li><a data-scroll href="#logout">Cerrar Sesion</a></li>
			</ul>
		</nav>
		<div class="container">
			<div class="header-info">
				<h1>EspiAngel</h1>
				<p>Servidor Departamento Informática y automática<br> de la USAL
				</p>
				<!--<a href="#" class="btn btn-primary">Login</a>-->
			</div>
		</div>
	</div>
	<!-- Services section start -->
	<section id="services">
		<div class="container">
			<div class="row">
				<div class="col-md-4">
					<div class="service-item">
						<a href="../wordpress/wp-login.php">
							<img border="0" src="../wordpress.png" width="150" height="100">
						</a>
						<h3>Wordpress</h3>
						<p>Crea tu blog personal con la herramienta de código<br>libre Wordpress
						</p>
					</div>
				</div>
				<div class="col-md-4">
					<div class="service-item">
						<p>
							<a href="../moodle">
								<img border="0" src="../moodle.jpg" width="150" height="100">
							</a>
						</p>
						<h3>Moodle</h3>
						<p>Plataforma educativa de código libre para que tanto tú<br>como los demás usuarios podais disfrutar de<br>sus ventajas
						</p>
					</div>
				</div>
				<div class="col-md-4">
					<div class="service-item">
					<a href="../correo">
						<img border="0" src="../roundcube.png" width="180" height="100">
					</a>
						<h3>Roundcube</h3>
						<p>Mantente en contacto con los demás usuarios de nuestro<br>servidor y comparte
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>



	<section id="services">
		<div class="container">
			<div class="row">
				<div class="col-md-4">
					<div id="cambio" class="service-item">
						<a href="../cambiarpass.html">
							<img border="0" src="../pass.png" width="150" height="100">
						</a>
						<h3>Cambiar contraseña</h3>
						<p>Cambia tu contraseña del portal
						</p>
					</div>
				</div>
				<div class="col-md-4">
					<div id="datos" class="service-item">
						<p>
							<a href="../cambiodatos.html">
								<img border="0" src="../info.png" width="150" height="100">
							</a>
						</p>
						<h3>Cambia datos personales</h3>
						<p>Cambia tu informacion personal en nuestro portal
						</p>
					</div>
				</div>
				<div id="baja" class="col-md-4">
					<div class="service-item">
					<a href="../baja.html">
						<img border="0" src="../baja.png" width="150" height="100">
					</a>
						<h3>Darse de baja</h3>
						<p>Elimina tus datos de nuestro servicio
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- Services section end -->

	<section id="status">
		<div class="container">
			<div class="row">
				<div class="col-md-4">
					<div id="status" class="service-item">
						<a href="status.cgi">
							<img border="0" src="../servicios.png" width="150" height="100">
						</a>
						<h3>Web Status</h3>
						<p>Comprueba que servicios funcionan y cuáles no
						</p>
					</div>
				</div>
				<div class="col-md-4">
					<div id="logout" class="service-item">
						<a href="logout.cgi">
							<img border="0" src="../logout.png" width="100" height="100">
						</a>
						<h3>Log-Out</h3>
						<p>Cierra sesion
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>


	<!-- Footer end  -->

	<!-- Load jQuery -->
	<script type="text/javascript" src="../js/jquery-1.11.2.min.js"></script>

	<!-- Load Booststrap -->
	<script type="text/javascript" src="../js/bootstrap.js"></script>

	<script type="text/javascript" src="../js/smooth-scroll.js"></script>

	<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>

	<!-- Load custom js for theme -->
	<script type="text/javascript" src="../js/app.js"></script>
</body>
</html>
};

print $html;

}else{


		print "No ha iniciado sesion";

		print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../index.html\">\n";



}
