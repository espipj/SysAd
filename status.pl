 #!/usr/bin/perl
 
use strict;
print qq(Content-type: text/plain\n\n);
my @services = ( 'ssh', 'dovecot', 'apache2', 'mysql', 'postfix' );
my $host = `/bin/hostname`;
chomp $host;
 
#añadir wordpress y moodle
foreach my $service (@services) {
 my $status = `/bin/ps cax | /bin/grep $service`;
 	 if (!$status) {
		print "$service no funciona en estos momentos.\n"
	 }
}
