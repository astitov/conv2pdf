#!/usr/bin/perl

use CGI;
my $q = CGI->new;
my $in = $q->param('infile');
my $out = $q->param('outfile') ? $q->param('outfile') : "/tmp/wk_out.pdf";
my $enc = $q->param('encoding') ? $q->param('encoding') : "UTF-8";

$command = "/usr/local/bin/wkhtmltopdf -nT 22mm --encoding ".$enc." ".$in." ".$out;
`$command`;

print "Content-type: application/pdf, name=wk_out.pdf\n\n";
open(F, "<", $out) || print STDERR "cant open $out";
while(<F>){ print };
close F;
exit;

