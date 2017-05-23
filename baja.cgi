#!/usr/bin/perl

use CGI;
use DBI;
use Linux::usermod;
use Authen::Simple::PAM;
use File::Path;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;

#print qq(Content-type: text/plain\n\n);

my $cgi = CGI->new;
my $username=$cgi->param('username');
my $password=$cgi->param('password');

my $pam = Authen::Simple::PAM->new(
        service => 'login'
    );


print $cgi->header;
 if($pam->authenticate( $username, $password ) ) {

   my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
     "user", "passwd")
  or die $DBI::errstr;

my $updateestado="UPDATE users SET estado=2 WHERE username='$username'";
my $statement = $dbh->prepare($updateestado);

# execute your SQL statement
$statement->execute();

my $sql="select * from users where username='$username'";

my $statement = $dbh->prepare($sql);
$statement->execute();

my @data;
@data = $statement->fetchrow_array();
my $correo = $data[6];

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
          To      => $correo,
          Subject => 'Solicitud recibida',
      ],
      body => "Revisaremos tu solicitud y te daremos de baja en menos\nde un minuto\nEsperamos verte pronto $username",
  );

eval { $sender->send($email) };

print "Solicitud de baja recibida para el usuario $username\n";
print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../index.html\">\n";
}else{

  print "Solicitud de baja fallida, ha introducido datos incorrectos";
  print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../baja.html\">\n";
}
