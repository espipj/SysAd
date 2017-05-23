#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use DBI;

#print qq(Content-type: text/plain\n\n);

my $cgi=CGI->new;

my $usuario = $cgi->param('usuario');
my $ape1 = $cgi->param('ape1');
my $ape2 = $cgi->param('ape2');
my $nombre = $cgi->param('nombre');
my $email = $cgi->param('email');
my $direccion = $cgi->param('direccion');
my $group = $cgi->param('grupo');

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;


my $sql="select * from users where email='$email'";

my $statement = $dbh->prepare($sql);
$statement->execute();

my @data;
@data = $statement->fetchrow_array();
my $correo = $data[6];

print $cgi->header();

if(defined $correo && $correo ne ''){



				print "Intente con otro email ya que el email esta ya registrado";

				print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../alta.html\">\n";

	}else{
					my $sql="select * from users where username='$usuario'";

					my $statement = $dbh->prepare($sql);
					$statement->execute();

					my @data;
					@data = $statement->fetchrow_array();
					my $usercomp = $data[1];
					if(defined $usercomp && $usercomp ne ''){
							print "Usuario ya registrado, intente con otro nombre de usuario";
							print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../alta.html\">\n";

				}else{

								my $sql= "INSERT INTO users(username,nombre,apellido1,apellido2,direccion,email,grupo,estado) VALUES(?,?,?,?,?,?,?,?)";
							my $stmt=$dbh->prepare($sql);
							$stmt->execute($usuario,$nombre,$ape1,$ape2,$direccion,$email,$group,'0');

							print $usuario;
							print "\n";
							print $nombre;
							print "\n";
							print $ape1;
							print $ape2;
							print "\n";
							print $email;
							print "\n";
							print $direccion;
							print "\n";
							print $group;
							print "\n";


							print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../index.html\">\n";
				}
	}
