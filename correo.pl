#!/usr/bin/perl

use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;


my $datestring = localtime();

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
		  Subject => 'Login del administrador en el sistema',
	      ],
	      body => "El administrador acaba de logearse en el sistema a fecha: $datestring",
	  );


  eval { $sender->send($email) };
