#!/usr/bin/perl
use strict;
use warnings;

use DBI;
use CGI;
use JSON;

my $cgi = CGI->new;

my %result = ();
my @errors = ();
my %payload = ();

print $cgi->header("application/json");


my $driver = "mysql"; 
my $database = "abills";
my $db_connect_string = "DBI:$driver:database=$database";
my $userid = "cwinsi";
my $password = "12345678";

my $dbh = DBI->connect($db_connect_string, $userid, $password ) or push(@errors, ("Cannot connect to database(("));


my $users_sql = $dbh->prepare("SELECT uid, id, credit, registration
                               FROM users");

$users_sql->execute() or push(@errors, ("Cannot run sql select query"));


my @users = ();

while (my @row = $users_sql->fetchrow_array()) {
    my %user = ();

    my ($uid, $id, $credit, $registration ) = @row;

    $user{"uid"} = $uid;
    $user{"id"} = $id;
    $user{"credit"} = $credit;
    $user{"registration"} = $registration;

    push @users, \%user;
}

$payload{"users"} = \@users;


$result{"payload"} = \%payload;
$result{"errors"} = \@errors;

print JSON->new->utf8->encode(\%result);