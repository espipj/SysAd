use strict;

use warnings;
use Email::Send::SMTP::Gmail;

my $mail=Email::Send::SMTP::Gmail->new( -smtp=>'gmail.com',
                                        -login=>'angelespiadsys@gmail.com',
                                        -pass=>'asd778899');


$mail->send(-to=>'angelespiadsys@gmail.com',
            -subject=>'Backup semanal!',
            -verbose=>'1',
            -body=>'Guardalo',
            -attachments=>'/backups/*');

$mail->bye;
