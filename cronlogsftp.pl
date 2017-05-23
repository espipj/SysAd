#!/usr/bin/perl

cat "/var/log/auth.log" | grep sftp > "/home/script/logs/sftplogs.log";