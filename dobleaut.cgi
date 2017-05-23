#!/usr/bin/perl

use warnings;
#use strict;
use CGI;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use Linux::usermod;
use Crypt::RandPasswd;
use DBI;
#print qq(Content-type: text/plain\n\n);


my $a=new CGI;
my $key=$a->param('doble');
my $regemail=$a->param('email');
my $password=$a->param('password');

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $sql="select username, aut from users where email='$regemail'";

my $statement = $dbh->prepare($sql);

# execute your SQL statement
$statement->execute();

my @data;
@data = $statement->fetchrow_array();
	my $key1 = $data[1];
	my $username = $data[0];
print $a->header;
if($key eq $key1){
	my $user = Linux::usermod->new($username);
	$user->set('password', $password);
	my $updateestado="UPDATE users SET aut=NULL WHERE email='$regemail'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	print "Cambio realizado satisfactoriamente.\nLe enviaremos un correo con sus nuevos datos.";

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
		  Subject => 'Actualizacion de datos en EspiAngel',
	      ],
	      body => "Estos son tus datos actualizados\nTu actualizacion en nuestro sistema se ha realizado correctamente.\nEstos son tus datos personales:\nUsuario: $username\nContraseña: $password\nCorreo Electronico: $regemail.",
	  );


  eval { $sender->send($email) };
  print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/scripts/inicio.cgi\">\n";
}
else{
	print "Cambio no realizado, datos erroneos.";
  print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../dobleaut.html\">\n";
}
