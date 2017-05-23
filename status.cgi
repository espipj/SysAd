#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use DBI;
use Term::ANSIColor qw(:constants);


my $cgi = CGI->new;

print $cgi->header();

#print qq(Content-type: text/plain\n\n);

my @services = ( 'ssh', 'dovecot', 'apache2', 'mysql');
my $host = `/bin/hostname`;
chomp $host;


foreach my $service (@services) {
 my $status = `/bin/ps cax | /bin/grep $service`;
 	 if (!$status) {
		#print RED, "$service no funciona en estos momentos.\n", RESET;
		print "$service DOWN<br>";
	 }
	 if($status){
	 	#print GREEN, "$service funciona correctamente.\n", RESET;
	 	print "$service UP<br>";
	 }
}
