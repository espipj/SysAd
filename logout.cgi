#!/usr/bin/perl

use warnings;
use strict;
use CGI;

my $cgi = CGI->new;

my $datestring = localtime();
my $cookie = $cgi->cookie('ESPIANGEL');

my @carray;
@carray=split('=',$cookie);


my $filename = '/scripts/logs/logincorrectos.log';
open(my $fh, '>>', $filename) or die "Could not open file '$filename' $!";
print $fh "$datestring;";
print $fh "Usuario: $carray[1];";
print $fh "IP = $ENV{REMOTE_ADDR}";
print $fh ";LOGOUT\n";
close $fh;

my $cookie1 = $cgi->cookie(-name=>'ESPIANGEL',
			 -value=>"user=$datestring LOGOUT",
			 -expires=>'+20m',
			 -path=>'/');

print $cgi->header(-cookie=>$cookie1);


print "Cerrando sesion...";
print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../index.html\">\n";