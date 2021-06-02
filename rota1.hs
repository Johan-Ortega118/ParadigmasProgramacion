module Rota1 where

rota1 :: [a] -> [a]
rota1 (x:xs) = xs ++ [x]
