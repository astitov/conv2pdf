# Dockerized HTML to PDF converter
- Docker
- Ubuntu-20
- Perl
- Lighttpd with CGI module
- wkhtmltopdf with patched QT

## Usage
Clone the repo and run `docker build` against `Dockerfile`.

Start container `docker run -p 80:80 [-v /host/dir:/container/dir:Z] -d image_name`.

In browser open `http://localhost:80/cgi_bin/wk_convert.cgi?infile=[input_file]&outfile=[output_file]`.

`input_file` -- an HTML page (local file or a URL) to be rendered to PDF.

`output_file` -- a resulting PDF written on disk and rendered in browser.


## Misc
A pretty useless thing inspired by a freelance gig with beautiful tech specs as follows:

<details>
We need a dockerfile for a container that does the following:

- uses any linux flavor
- supports wkhtmltopdf with patched qt (e.g. default installation on debian has qt issues)
- supports perl cgi calls
- uses any web server
- should support this call:
http://my_docker/wk_convert.cgi?infile=/tmp/infile.html&outfile=/tmp/outfile.pdf

wk_convert.cgi looks like this:
```
#!/usr/bin/perl
use CGI;
`wkhtmltopdf -nT 22mm param('infile') param('outfile')`;
print "Content-type: application/pdf; name=wk.pdf\n\n";
open(F,"<","/tmp/outfile.pdf") || print STDERR "cant < outfile.pdf $!";;
while(<F>) { print };
close F;
exit;
```
(edit the wkhtmltopdf path to whatever you need)

infile.html is located here:

https://www.scapefox.com/infile.html

download and store in /tmp/ in docker for testing purposes

output PDF should look exactly like this pdf:

https://www.scapefox.com/cgi-bin/wkconvert.cgi?infile=/tmp/infile.html&outfile=/tmp/outfile.pdf
</details>
