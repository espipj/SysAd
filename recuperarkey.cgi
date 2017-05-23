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


my $cgi=CGI->new;
#my $username = $cgi->param('username');
my $regemail=$cgi->param('email');

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $sql="select username from users where email='$regemail'";

my $statement = $dbh->prepare($sql);

# execute your SQL statement
$statement->execute();

my @data;
@data = $statement->fetchrow_array();
my $username = $data[0];



my $user = Linux::usermod->new($username);
my $contra=$user->get(password);
my $pass = Crypt::RandPasswd->word( 6, 8 );

$user->set('password', $pass);

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
		  Subject => 'Tu nueva contraseNa',
	      ],
	      body => "ContraseNa: $pass\nSi quieres puedes cambiarla desde tu pagina principal.",
	  );

eval { $sender->send($email) };
print $cgi->header;
print "Te hemos enviado al correo tu nueva contraseNa";
print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../index.html\">\n";
