module SenCosTan where

calc :: String -> Float -> [Float]
calc "sin" n = [sin x | x <- [1..n]]
calc "cos" n = [cos x | x <- [1..n]]
calc "tan" n = [tan x | x <- [1..n]]
calc "exp" n = [exp x | x <- [1..n]]
calc "log" n = [log x | x <- [1..n]]