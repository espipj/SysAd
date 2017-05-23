#!/usr/bin/perl

use strict;
use warnings;
use Sys::CPU;
use Memory::Usage;
use Filesys::DiskUsage;
use Filesys::DiskSpace;
use Proc::CPUUsage;
use Email::Send;
use Email::Send::Gmail;
use Email::Simple::Creator;
use Net::Address::IP::Local;

my $mu = Memory::Usage->new();
 
my $cpu = Proc::CPUUsage->new;

# file system /home or /dev/sda5
my $dir = "/home";
 
# get data for /home fs
my ($fs_type, $fs_desc, $used, $avail, $fused, $favail) = df $dir;
 
# calculate free space in %
my $df_free = (($avail) / ($avail+$used)) * 100.0;
 
# display message
my $out = $df_free;
#print $out;

my $usage = $cpu->usage; ## returns usage since new()
my $usageper = $usage;
#print $usageper;

# Record amount in use afterwards
$mu->record('');
my $ram = $mu->report();


# Get the local system's IP address that is "en route" to "the internet":
my $address = Net::Address::IP::Local->public;


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
      Subject => 'Estadisticas Uso del Sistema',
        ],
        body => "Informe acerca del sistema EspiAngel:\n\nUso CPU: $usageper %\nUso RAM:\n$ram\nUso espacio: $out\n\n\nInformación detallada en $address/munin",
    );


  eval { $sender->send($email) };