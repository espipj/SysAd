use File::Backup("backup");
use DBI;

#Sacar usuarios que existan en este momento

my $dbh = DBI->connect("DBI:mysql:database=name;host=localhost;port=port",
  "user", "passwd")
  or die $DBI::errstr;

my $updateestado="select username from users WHERE estado=1";
my $statement = $dbh->prepare($updateestado);

# execute your SQL statement
$statement->execute();

my @users;

while(@users = $statement->fetchrow_array()){
    my $user = $users[0];
    print $user;
    backup(
    from          => "/home/" . $user . "/",
    to            => "/home/backups",
    torootname    => "",
    keep          => "7",
    tar           => "usr/bin/tar",
    compress      => "/usr/bin/gzip",
    tarflags      => "-cf",
    compressflags => "",
    tarsuffix     => '.tar',
  );
}
