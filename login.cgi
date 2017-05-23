#!/usr/bin/perl


use CGI;
use DBI;
use Authen::Simple::PAM;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use strict;
use warnings;
#print qq(Content-type: text/plain\n\n);
# read the CGI params
my $cgi = CGI->new;
my $username = $cgi->param('username');
my $password = $cgi->param('password');
my $filename;
#my $username="pablo";
#my $password="asd789";
my $pam = Authen::Simple::PAM->new(
        service => 'login'
    );


my $cookie = $cgi->cookie(-name=>'ESPIANGEL',
			 -value=>"user=$username",
			 -expires=>'+20m',
			 -path=>'/');

my $datestring = localtime();

if($username eq "root"){
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
		  To      => 'angelespiadsys@gmail.com',
		  Subject => 'Intento de inicio del administrador',
	      ],
	      body => "Le informamos de que se ha intentado realizar\nun inicio de sesión por parte del administrador.",
	  );


  eval { $sender->send($email) };
}

   if($pam->authenticate( $username, $password ) ) {

		print $cgi->header(-cookie=>$cookie);
	    print "Has iniciado sesion correctamente $username";

		$filename = '/scripts/logs/logincorrectos.log';
		open(my $fh, '>>', $filename) or die "Could not open file '$filename' $!";
		print $fh "$datestring;";
		print $fh "Usuario: $username;";
		print $fh "IP = $ENV{REMOTE_ADDR}";
		print $fh ";LOGIN\n";
		close $fh;
		print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/scripts/inicio.cgi\">\n";

		#print $a->redirect('../portal.html');


    }else{

	    print $cgi->header;
		print "Login incorrecto: $username\n";
		print "Intentalo de nuevo\n";

		$filename = '/scripts/logs/loginfallidos.log';
		open(my $fh, '>>', $filename) or die "Could not open file '$filename' $!";
		print $fh "$datestring;";
		print $fh "Usuario=$username;";
		print $fh "IP = $ENV{REMOTE_ADDR}\n";
		close $fh;
		print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../index.html\">\n";


		#die "$!";
}



