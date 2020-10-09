
use strict;
use warnings;


my %department_number_for = (
    finance     => 13,
    programming => 2,
    janitorial  => 17,
    executive   => 0,
    );

my @tttt = @department_number_for{'finance', 'programming', 'executive'};



print qq[@tttt \n];
print qq[@department_number_for{'finance', 'programming', 'executive'}\n];

#print qq{@department_number_for(finance, programmin) \n};
