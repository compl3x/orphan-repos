{- 
	luhn number checker in Haskell
	Written by Michael Cowell, 2015
	Written for G51FUN
	
	HOW IT WORKS:
	
		1. The string is split into a list of characters.
		2. Every other number in the list is doubled.
		3. If any number is >9, 9 is subtracted from it.
		4. Number is summed, and modded by 10.
		5. If the modulo result is 0, the number is valid.
		
	USAGE:
		
		luhn "1234567890123456"
-}

import Data.Char (digitToInt)

-- Double every other number
cycleMultiply xs = (zipWith (*) xs (cycle[2,1]))

-- Subtract 9 if above 9
keepBelowNine xs = map (\x -> if x>9 then x-9 else x) xs

-- Check n%10 == 0
checkNum n = (n `mod` 10 == 0)

toList number = map digitToInt number

luhn number = checkNum (sum (keepBelowNine(cycleMultiply( toList number))))