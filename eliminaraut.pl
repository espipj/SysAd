#!/usr/bin/perl

use warnings;
#use strict;
use DBI;

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $updateestado="UPDATE users SET aut=NULL";
	my $statement = $dbh->prepare($updateestado);
	$statement->execute();
