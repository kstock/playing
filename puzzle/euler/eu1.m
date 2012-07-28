function [ total ] = eu1(n)
%{
Find the sum of all the multiples of 3 or 5 below 1000.
http://projecteuler.net/problem=1
%}

    total = 0;
    for i = 1:(n-1),
        if mod(i,3) == 0
            total = total + i;
        else if mod(i,5) == 0
            total =total + i;
            end
        end
    end
end

