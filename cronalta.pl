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

  my $sender = Email::Send->new(
      {   mailer      => 'Gmail',
          mailer_args => [
              username => 'angelespiadsys@gmail.com',
              password => 'asd778899',
          ]
      }
  );
  my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
    "user", "passwd")
  or die $DBI::errstr;

my $sql="select username,nombre,apellido1,apellido2,direccion,email,grupo from users where estado=0";


my $statement = $dbh->prepare($sql);

# execute your SQL statement
$statement->execute();
my @data;
while (@data = $statement->fetchrow_array()) {

	my $usuario = $data[0];
	my $group = $data[6];
	my $regemail = $data[5];

	my $pass = Crypt::RandPasswd->word( 6, 8 );
	my $ruta="/home/" . $usuario . "/";
	print $ruta;
	unless(mkdir $ruta) {
	die "File cannot be created: $!";
	    }
	chmod(0700, $ruta);# || print $!;
	my $rutasim="/home/" . $usuario . "/apuntes";
	symlink("/home/apuntes", "$rutasim");
	Linux::usermod->add($usuario,$pass,'',$group,'',$ruta,"/bin/bash");
	print "USERADD: $! \n";
	my $user=Linux::usermod->new($usuario);
	my $uid=$user->get(uid);
	my $gid=$user->get(gid);
	my $home=$user->get(home);
	chown($uid, $gid, $ruta);
	copy("/etc/skel/.bash_logout", $ruta . ".bash_logout");
	copy("/etc/skel/.bashrc", $ruta . ".bashrc");
	copy("/etc/skel/.profile", $ruta . ".profile");
	copy("/etc/skel/condiciones.txt", $ruta . "condiciones.txt");
	my $email = Email::Simple->create(
	      header => [
		  From    => 'angelespiadsys@gmail.com',
		  To      => $regemail,
		  Subject => 'Bienvenido a EspiAngel',
	      ],
	      body => "Bienvenido a nuestro servidor:\nTu registro en nuestro sistema se ha realizado correctamente.\nEstos son tus datos personales:\nUsuario: $usuario\nContraseña: $pass\nCorreo Electronico: $regemail.",
	  );


  eval { $sender->send($email) };
	#Establecemos Quota

	my $dev = Quota::getqcarg($ruta);

my ($curblock,$soft,$hard,$btimeout,$curinode,$isoft,$ihard,$itimeout)= Quota::query($dev,$uid) or die "Unable to query quota for $uid:$!\n";
Quota::setqlim($dev,$uid,81920,81920,$isoft,$ihard,1,0);#	When $kind is given and set to 1, $uid is taken as gid and group quota limits are set. KIND=1--> $uid es de GRUPO

	my $updateestado="UPDATE users SET estado=1 WHERE username='$usuario'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();

	my $updateestado="select username from users where estado=1";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
	my @usuarios;
	my $i;
	while (@data = $statement->fetchrow_array()) {

	$usuarios[$i] = $data[0];
	print $usuarios[$i];
	$i++;
	}
	my $grp  = Linux::usermod->new(mail, 1);


	$grp->set(users,"@usuarios");


}






#https://perltricks.com/article/43/2013/10/11/How-to-schedule-Perl-scripts-using-cron/
