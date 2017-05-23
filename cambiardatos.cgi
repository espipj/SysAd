#!/usr/bin/perl

use warnings;
#use strict;
use CGI;
use Authen::Simple::PAM;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use Linux::usermod;
use Crypt::RandPasswd;
use DBI;
#print qq(Content-type: text/plain\n\n);

my $a=new CGI;
my $usuario=$a->param('username');
my $nombre=$a->param('nombre');
my $apellido1=$a->param('ape1');
my $apellido2=$a->param('ape2');
my $regemail=$a->param('email');
my $direccion=$a->param('direccion');
my $password=$a->param('password');
my $pam = Authen::Simple::PAM->new(
        service => 'login'
    );




my $cookie = $a->cookie('ESPIANGEL');

my @carray;
@carray=split('=',$cookie);
print $a->header;
print $carray[1];
	print <br>;

 if($pam->authenticate( $carray[1], $password ) ) {
 	print "Autenticado.";
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
my $updateestado;
if($username eq $carray[1]){
	print "Cambiando datos...\n";
	print <br>;
	if($nombre ne ""){
	$updateestado="UPDATE users SET nombre='$nombre' WHERE username='$carray[1]'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Nombre cambiado a: $nombre\n";
	print <br>;
	}
	if($apellido1 ne ""){
	$updateestado="UPDATE users SET apellido1='$apellido1' WHERE username='$carray[1]'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Primer Apellido cambiado a: $apellido1\n";
	}
	if($apellido2 ne ""){
	$updateestado="UPDATE users SET apellido2='$apellido2' WHERE username='$carray[1]'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Segundo Apellido cambiado a: $apellido2\n";
	}
	if($direccion ne ""){
	$updateestado="UPDATE users SET direccion='$direccion' WHERE username='$carray[1]'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Direccion cambiada a: $direccion\n";
	}
	if($regemail ne ""){
	$updateestado="UPDATE users SET email='$regemail' WHERE username='$carray[1]'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Email cambiado a: $regemail\n";
	}

}else{
	print "El usuario no existe\n";


}

my $sql="select username,nombre,apellido1,apellido2,direccion,email,grupo from users where username='$carray[1]'";
$statement = $dbh->prepare($sql);
$statement->execute();

my @data;
@data = $statement->fetchrow_array();

my $eusername=$data[0];
my $enombre=$data[1];
my $eape1=$data[2];
my $eape2=$data[3];
my $edireccion=$data[4];
my $eemail=$data[5];


    my $sender = Email::Send->new(
      {   mailer      => 'Gmail',
          mailer_args => [
              username => 'angelespiadsys@gmail.com',
              password => 'asd778899',
          ]
      }
    );

    my $email = Email::Simple->create(
          header => [
    	  From    => 'angelespiadsys@gmail.com',
    	  To      => $eemail,
    	  Subject => 'Cambio de datos en EspiAngel',
          ],
          body => "El cambio de datos en nuestro sistema se ha realizado correctamente.\nEstos son tus datos personales:\nUsuario: $eusername\nNombre: $enombre\nApellido 1: $eape1\nApellido 2: $eape2\nDireccion: $edireccion\n
          Correo Electronico: $eemail.",
      );
 eval { $sender->send($email) };

		print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=/scripts/inicio.cgi\">\n";
 }else{
 	print "Fallo en la autenticacion";

	print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../cambiodatos.html\">\n";
 }
