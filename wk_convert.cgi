#!/usr/bin/perl

use CGI;
my $q = CGI->new;
my $in = $q->param('infile');
my $out = $q->param('outfile');

$command = "/usr/local/bin/wkhtmltopdf -nT 22mm ".$in." ".$out;
`$command`;

print "Content-type: application/pdf, name=wk.pdf\n\n";
open(F, "<", $out) || print STDERR "cant open $out";
while(<F>){ print };
close F;
exit;

