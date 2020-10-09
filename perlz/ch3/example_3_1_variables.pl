use strict;
use warnings;
use diagnostics;

my $hero ='ovid';
my $fool = $hero;
print "$hero isn't that much hero. $fool is a fool.\n";

my $hero = 'anybody else';
print "$hero is probably more of a hero than $fool.\n";
##########################################################
my %snacks = (
		stinky => 'limburger',
		yummy => 'brie',
		surprise => 'soap slices',
);

my @cheese_tray = values %snacks;
print "Our cheese tray will have: ";
for my $cheese (@cheese_tray){
			print "'$cheese'";
}

print "\n";
#########################################################

print "@cheese_tray.\n";
