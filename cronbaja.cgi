#!/usr/bin/perl

use warnings;
#use strict;
use Linux::usermod;
use DBI;
use Crypt::RandPasswd;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use Quota;
use Getopt::Std;
use File::Copy;
use File::Path;


my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $sql="select username,nombre,apellido1,apellido2,direccion,email,grupo from users where estado=2";


my $statement = $dbh->prepare($sql);

# execute your SQL statement
$statement->execute();
my @data;
while (@data = $statement->fetchrow_array()) {

	my $usuario = $data[0];
	my $group = $data[6];
	my $regemail = $data[5];

	my $ruta="/home/" . $usuario . "/";
	my $ruta1="/var/mail/" . $usuario . "/";
	if (-e $ruta){
	rmtree($ruta) or die "Cannot rmtree '$path' : $!";

	}
	if(-e $ruta1){

	rmtree($ruta1) or die "Cannot rmtree '$path' : $!";

	}
	Linux::usermod->del($usuario) or die "Deluser: $!\n";


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
		  To      => $regemail,
		  Subject => 'Confirmacion Baja',
	      ],
	      body => "Te hemos dado de baja finalmente\nEstos son tus datos personales:\n
	      Usuario: $usuario\n
	      Correo Electronico: $regemail.",
	  );


  eval { $sender->send($email) };



	#my $updateestado="UPDATE users SET estado=3 WHERE username='$usuario'";
	my $updateestado="DELETE from users WHERE username='$usuario'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();


}
