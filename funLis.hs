module FunLis where

--funcionLista :: [a] -> [a]
--funcionLista (x:xs) = cuadrado x : funcionLista xs

--cuadrado :: Int -> Int
--cuadrado n = n * n

cuadrado :: Int -> Int
cuadrado x = x^2

funcionLista :: [Int] -> [Int]
funcionLista xs = map cuadrado xs