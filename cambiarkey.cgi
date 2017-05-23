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


my $a=new CGI;
my $regemail=$a->param('email');

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;



my $pass = Crypt::RandPasswd->rand_int_in_range(100000,999999);

my $updateestado="UPDATE users SET aut='$pass' WHERE email='$regemail'";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();


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
		  Subject => 'Tu codigo de verificacion es:',
	      ],
	      body => "Codigo: $pass\nEste codigo tiene una duraccion de 2 minutos.",
	  );

eval { $sender->send($email) };
print "Te hemos enviado al correo tu nueva contraseNa";
print $a->redirect('../dobleaut.html');
