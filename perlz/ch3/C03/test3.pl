use strict;
use warnings;
use diagnostics;


my @things_1 = ('lia', 'gia','potics',);
my $numb_th = scalar  @things_1;

print "$numb_th \n";

##############################################################
my @things_2 = ('lia1', 'gia1','potics1',);
my %count = (useless => scalar @things_2);

print "$count{useless} \n";
#############################################################
my %orders = (
		carol => 13.2,
		valera => 17.9,
		'billy'=> 0.
);

my @flatten = %orders;
print qq[@flatten \n];
##########################################################

my @swords = ('katana','wakizashi');
my $num_swords = scalar @swords;
my ($left_hand) = @swords;
my ($left_hand, $right_hand) = @swords;

#($right_hand, $left_hand) = ($left_hand, $right_hand);


print qq[$num_swords \n];
print qq[($left_hand, $right_hand) \n];

######################################################


my @numbers = (1, 2, 3, 4, 5);
for my $number (@numbers){
			my $reciprocal = 1 / $number;
			print qq[The reciprocal of $number is $reciprocal;\n];
	}


