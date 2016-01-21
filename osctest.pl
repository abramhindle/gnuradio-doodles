use Net::OpenSoundControl::Client;
use strict;
my $oschost = $ARGV[0] || "127.0.0.1";
my $oscport = 12345;
my $client = Net::OpenSoundControl::Client->new(Host => $oschost, Port => $oscport ) or die "Could not start client: $@\n";

$client->send(['/foo','i',1,'f',rand(),'s','Perl Test']);
$client->send(['/center','i',1,'f',50000*rand()]);
$client->send(['/center','i',2,'f',50000*rand()]);
$client->send(['/center','i',3,'f',50000*rand()]);
$client->send(['/center','i',4,'f',50000*rand()]);
# $client->send(['/center','i',0,'f',24000000 + 110000000*rand()]);


$client->send(['/low','i',1,'f',1+200*rand()]);
$client->send(['/low','i',2,'f',1+200*rand()]);
$client->send(['/low','i',3,'f',1+200*rand()]);
$client->send(['/low','i',4,'f',1+200*rand()]);


$client->send(['/high','i',1,'f',201+4000*rand()]);
$client->send(['/high','i',2,'f',201+4000*rand()]);
$client->send(['/high','i',3,'f',201+4000*rand()]);
$client->send(['/high','i',4,'f',201+4000*rand()]);
