use Net::OpenSoundControl::Client;
use strict;
my $oschost = "127.0.0.1";
my $oscport = 1234;
my $client = Net::OpenSoundControl::Client->new(Host => $oschost, Port => $oscport ) or die "Could not start client: $@\n";

$client->send(['/center','i',0,'f',$ARGV[0]*1e6]);

