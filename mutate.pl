use Net::OpenSoundControl::Client;
use Time::HiRes qw(sleep);
use strict;
my $oschost = $ARGV[0] || "127.0.0.1";
my $oscport = 1234;
my $client = Net::OpenSoundControl::Client->new(Host => $oschost, Port => $oscport ) or die "Could not start client: $@\n";

$client->send(['/foo','i',1,'f',rand(),'s','Perl Test']);
my @subs = (
	sub { $client->send(['/center','i',1,'f',50000*rand()]); },
	sub { $client->send(['/center','i',2,'f',50000*rand()]); },
	sub { $client->send(['/center','i',3,'f',50000*rand()]); },
	sub { $client->send(['/center','i',4,'f',50000*rand()]); },
	sub { $client->send(['/low','i',1,'f',1+200*rand()]); },
	sub { $client->send(['/low','i',2,'f',1+200*rand()]); },
	sub { $client->send(['/low','i',3,'f',1+200*rand()]); },
	sub { $client->send(['/low','i',4,'f',1+200*rand()]); },
	sub { $client->send(['/high','i',1,'f',201+4000*rand()]); },
	sub { $client->send(['/high','i',2,'f',201+4000*rand()]); },
	sub { $client->send(['/high','i',3,'f',201+4000*rand()]); },
	sub { $client->send(['/high','i',4,'f',201+4000*rand()]); },
);

while(1) {
	my $sub = $subs[rand(scalar(@subs))];
	$sub->();
	sleep rand();
}
