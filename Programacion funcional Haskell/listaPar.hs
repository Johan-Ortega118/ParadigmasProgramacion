module ListaPar where

--lista :: [Int] -> [Int]
--lista (x:xs) = map par xs

filtro :: (a -> Bool) -> [a] -> [a]
filtro _ [] = []
filtro p (x:xs)
     | p x       = x : filtro p xs
     | otherwise = filtro p xs

par :: Int -> Bool
par x = if mod x 2 == 0 then True else False
--    x == True putStrLn x

--if mod x 2 == 0 then True else False
main = print (filtro (par)[1,2..10])
