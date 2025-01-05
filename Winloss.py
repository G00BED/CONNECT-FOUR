#Defines What a Win & Loss are
import BoardList

def Winloss(MyVal):
  #DETERMINES ALL THE POSSIBLE 4 IN A ROWS
  MyVal = 0
  if BoardList.d["a"] == "X" and BoardList.d["b"] == "X" and BoardList.d["c"] == "X" and BoardList.d["d"] == "X":
    return MyVal + 1

  
  if BoardList.d["g"] == "X" and BoardList.d["f"] == "X" and BoardList.d["e"] == "X" and BoardList.d["d"] == "X":
    return MyVal + 1

  
  if BoardList.d["b"] == "X" and BoardList.d["c"] == "X" and BoardList.d["d"] == "X" and BoardList.d["e"] == "X":
    return MyVal + 1

  
  if BoardList.d["f"] == "X" and BoardList.d["e"] == "X" and BoardList.d["d"] == "X" and BoardList.d["c"] == "X":
    return MyVal + 1

  
  if BoardList.d["h"] == "X" and BoardList.d["i"] == "X" and BoardList.d["j"] == "X" and BoardList.d["k"] == "X":
    return MyVal + 1

  
  if BoardList.d["n"] == "X" and BoardList.d["m"] == "X" and BoardList.d["l"] == "X" and BoardList.d["k"] == "X":
    return MyVal + 1

  
  if BoardList.d["i"] == "X" and BoardList.d["j"] == "X" and BoardList.d["k"] == "X" and BoardList.d["l"] == "X":
    return MyVal + 1

  
  if BoardList.d["m"] == "X" and BoardList.d["l"] == "X" and BoardList.d["k"] == "X" and BoardList.d["j"] == "X":
    return MyVal + 1

  
  if BoardList.d["o"] == "X" and BoardList.d["p"] == "X" and BoardList.d["q"] == "X" and BoardList.d["r"] == "X":
    return MyVal + 1

  
  if BoardList.d["u"] == "X" and BoardList.d["t"] == "X" and BoardList.d["s"] == "X" and BoardList.d["r"] == "X":
    return MyVal + 1

  
  if BoardList.d["p"] == "X" and BoardList.d["q"] == "X" and BoardList.d["r"] == "X" and BoardList.d["s"] == "X":
    return MyVal + 1

  
  if BoardList.d["t"] == "X" and BoardList.d["s"] == "X" and BoardList.d["r"] == "X" and BoardList.d["q"] == "X":
    return MyVal + 1

  
  if BoardList.d["cc"] == "X" and BoardList.d["dd"] == "X" and BoardList.d["ee"] == "X" and BoardList.d["ff"] == "X":
    return MyVal + 1

  
  if BoardList.d["ii"] == "X" and BoardList.d["hh"] == "X" and BoardList.d["gg"] == "X" and BoardList.d["ff"] == "X":
    return MyVal + 1

  
  if BoardList.d["dd"] == "X" and BoardList.d["ee"] == "X" and BoardList.d["ff"] == "X" and BoardList.d["gg"] == "X":
    return MyVal + 1

  
  if BoardList.d["hh"] == "X" and BoardList.d["gg"] == "X" and BoardList.d["ff"] == "X" and BoardList.d["ee"] == "X":
    return MyVal + 1

  
  if BoardList.d["a"] == "X" and BoardList.d["h"] == "X" and BoardList.d["o"] == "X" and BoardList.d["v"] == "X":
    return MyVal + 1

  
  if BoardList.d["cc"] == "X" and BoardList.d["v"] == "X" and BoardList.d["o"] == "X" and BoardList.d["h"] == "X":
    return MyVal + 1

  
  if BoardList.d["b"] == "X" and BoardList.d["i"] == "X" and BoardList.d["p"] == "X" and BoardList.d["w"] == "X":
    return MyVal + 1

  
  if BoardList.d["dd"] == "X" and BoardList.d["w"] == "X" and BoardList.d["p"] == "X" and BoardList.d["i"] == "X":
    return MyVal + 1

  
  if BoardList.d["c"] == "X" and BoardList.d["j"] == "X" and BoardList.d["q"] == "X" and BoardList.d["x"] == "X":
    return MyVal + 1

  
  if BoardList.d["ee"] == "X" and BoardList.d["x"] == "X" and BoardList.d["q"] == "X" and BoardList.d["j"] == "X":
    return MyVal + 1

  
  if BoardList.d["ff"] == "X" and BoardList.d["y"] == "X" and BoardList.d["r"] == "X" and BoardList.d["k"] == "X":
    return MyVal + 1

  
  if BoardList.d["d"] == "X" and BoardList.d["k"] == "X" and BoardList.d["r"] == "X" and BoardList.d["y"] == "X":
    return MyVal + 1

  
  if BoardList.d["gg"] == "X" and BoardList.d["z"] == "X" and BoardList.d["s"] == "X" and BoardList.d["l"] == "X":
    return MyVal + 1

  
  if BoardList.d["e"] == "X" and BoardList.d["l"] == "X" and BoardList.d["s"] == "X" and BoardList.d["z"] == "X":
    return MyVal + 1

  
  if BoardList.d["hh"] == "X" and BoardList.d["aa"] == "X" and BoardList.d["t"] == "X" and BoardList.d["m"] == "X":
    return MyVal + 1

  
  if BoardList.d["f"] == "X" and BoardList.d["m"] == "X" and BoardList.d["t"] == "X" and BoardList.d["aa"] == "X":
    return MyVal + 1

  
  if BoardList.d["ii"] == "X" and BoardList.d["bb"] == "X" and BoardList.d["u"] == "X" and BoardList.d["n"] == "X":
    return MyVal + 1

  
  if BoardList.d["g"] == "X" and BoardList.d["n"] == "X" and BoardList.d["u"] == "X" and BoardList.d["bb"] == "X":
    return MyVal + 1

  
  if BoardList.d["v"] == "X" and BoardList.d["p"] == "X" and BoardList.d["j"] == "X" and BoardList.d["d"] == "X":
    return MyVal + 1

  
  if BoardList.d["ff"] == "X" and BoardList.d["z"] == "X" and BoardList.d["t"] == "X" and BoardList.d["n"] == "X":
    return MyVal + 1

  
  if BoardList.d["cc"] == "X" and BoardList.d["w"] == "X" and BoardList.d["q"] == "X" and BoardList.d["k"] == "X":
    return MyVal + 1

  
  if BoardList.d["e"] == "X" and BoardList.d["k"] == "X" and BoardList.d["q"] == "X" and BoardList.d["w"] == "X":
    return MyVal + 1

  
  if BoardList.d["dd"] == "X" and BoardList.d["x"] == "X" and BoardList.d["r"] == "X" and BoardList.d["l"] == "X":
    return MyVal + 1

  
  if BoardList.d["f"] == "X" and BoardList.d["l"] == "X" and BoardList.d["r"] == "X" and BoardList.d["x"] == "X":
    return MyVal + 1

  if BoardList.d["bb"] == "X" and BoardList.d["aa"] == "X" and BoardList.d["z"] == "X" and BoardList.d["y"] == "X":
    return MyVal + 1

  if BoardList.d["v"] == "X" and BoardList.d["w"] == "X" and BoardList.d["x"] == "X" and BoardList.d["y"] == "X":
    return MyVal + 1

  if BoardList.d["w"] == "X" and BoardList.d["x"] == "X" and BoardList.d["y"] == "X" and BoardList.d["z"] == "X":
    return MyVal + 1

  if BoardList.d["aa"] == "X" and BoardList.d["z"] == "X" and BoardList.d["y"] == "X" and BoardList.d["x"] == "X":
    return MyVal + 1

  
  if BoardList.d["a"] == "O" and BoardList.d["b"] == "O" and BoardList.d["c"] == "O" and BoardList.d["d"] == "O":
    return MyVal + 2

  
  if BoardList.d["g"] == "O" and BoardList.d["f"] == "O" and BoardList.d["e"] == "O" and BoardList.d["d"] == "O":
    return MyVal + 2

  
  if BoardList.d["b"] == "O" and BoardList.d["c"] == "O" and BoardList.d["d"] == "O" and BoardList.d["e"] == "O":
    return MyVal + 2

  
  if BoardList.d["f"] == "O" and BoardList.d["e"] == "O" and BoardList.d["d"] == "O" and BoardList.d["c"] == "O":
    return MyVal + 2

  
  if BoardList.d["h"] == "O" and BoardList.d["i"] == "O" and BoardList.d["j"] == "O" and BoardList.d["k"] == "O":
    return MyVal + 2

  
  if BoardList.d["n"] == "O" and BoardList.d["m"] == "O" and BoardList.d["l"] == "O" and BoardList.d["k"] == "O":
    return MyVal + 2

  
  if BoardList.d["i"] == "O" and BoardList.d["j"] == "O" and BoardList.d["k"] == "O" and BoardList.d["l"] == "O":
    return MyVal + 2

  
  if BoardList.d["m"] == "O" and BoardList.d["l"] == "O" and BoardList.d["k"] == "O" and BoardList.d["j"] == "O":
    return MyVal + 2

  
  if BoardList.d["o"] == "O" and BoardList.d["p"] == "O" and BoardList.d["q"] == "O" and BoardList.d["r"] == "O":
    return MyVal + 2

  
  if BoardList.d["u"] == "O" and BoardList.d["t"] == "O" and BoardList.d["s"] == "O" and BoardList.d["r"] == "O":
    return MyVal + 2

  
  if BoardList.d["p"] == "O" and BoardList.d["q"] == "O" and BoardList.d["r"] == "O" and BoardList.d["s"] == "O":
    return MyVal + 2

  
  if BoardList.d["t"] == "O" and BoardList.d["s"] == "O" and BoardList.d["r"] == "O" and BoardList.d["q"] == "O":
    return MyVal + 2

  
  if BoardList.d["cc"] == "O" and BoardList.d["dd"] == "O" and BoardList.d["ee"] == "O" and BoardList.d["ff"] == "O":
    return MyVal + 2

  
  if BoardList.d["ii"] == "O" and BoardList.d["hh"] == "O" and BoardList.d["gg"] == "O" and BoardList.d["ff"] == "O":
    return MyVal + 2

  
  if BoardList.d["dd"] == "O" and BoardList.d["ee"] == "O" and BoardList.d["ff"] == "O" and BoardList.d["gg"] == "O":
    return MyVal + 2

  
  if BoardList.d["hh"] == "O" and BoardList.d["gg"] == "O" and BoardList.d["ff"] == "O" and BoardList.d["ee"] == "O":
    return MyVal + 2

  
  if BoardList.d["a"] == "O" and BoardList.d["h"] == "O" and BoardList.d["o"] == "O" and BoardList.d["v"] == "O":
    return MyVal + 2

  
  if BoardList.d["cc"] == "O" and BoardList.d["v"] == "O" and BoardList.d["o"] == "O" and BoardList.d["h"] == "O":
    return MyVal + 2

  
  if BoardList.d["b"] == "O" and BoardList.d["i"] == "O" and BoardList.d["p"] == "O" and BoardList.d["w"] == "O":
    return MyVal + 2

  
  if BoardList.d["dd"] == "O" and BoardList.d["w"] == "O" and BoardList.d["p"] == "O" and BoardList.d["i"] == "O":
    return MyVal + 2

  
  if BoardList.d["c"] == "O" and BoardList.d["j"] == "O" and BoardList.d["q"] == "O" and BoardList.d["x"] == "O":
    return MyVal + 2

  
  if BoardList.d["ee"] == "O" and BoardList.d["x"] == "O" and BoardList.d["q"] == "O" and BoardList.d["j"] == "O":
    return MyVal + 2

  
  if BoardList.d["ff"] == "O" and BoardList.d["y"] == "O" and BoardList.d["r"] == "O" and BoardList.d["k"] == "O":
    return MyVal + 2

  
  if BoardList.d["d"] == "O" and BoardList.d["k"] == "O" and BoardList.d["r"] == "O" and BoardList.d["y"] == "O":
    return MyVal + 2

  
  if BoardList.d["gg"] == "O" and BoardList.d["z"] == "O" and BoardList.d["s"] == "O" and BoardList.d["l"] == "O":
    return MyVal + 2

  
  if BoardList.d["e"] == "O" and BoardList.d["l"] == "O" and BoardList.d["s"] == "O" and BoardList.d["z"] == "O":
    return MyVal + 2

  
  if BoardList.d["hh"] == "O" and BoardList.d["aa"] == "O" and BoardList.d["t"] == "O" and BoardList.d["m"] == "O":
    return MyVal + 2

  
  if BoardList.d["f"] == "O" and BoardList.d["m"] == "O" and BoardList.d["t"] == "O" and BoardList.d["aa"] == "O":
    return MyVal + 2

  
  if BoardList.d["ii"] == "O" and BoardList.d["bb"] == "O" and BoardList.d["u"] == "O" and BoardList.d["n"] == "O":
    return MyVal + 2

  
  if BoardList.d["g"] == "O" and BoardList.d["n"] == "O" and BoardList.d["u"] == "O" and BoardList.d["bb"] == "O":
    return MyVal + 2

  
  if BoardList.d["v"] == "O" and BoardList.d["p"] == "O" and BoardList.d["j"] == "O" and BoardList.d["d"] == "O":
    return MyVal + 2

  
  if BoardList.d["ff"] == "O" and BoardList.d["z"] == "O" and BoardList.d["t"] == "O" and BoardList.d["n"] == "O":
    return MyVal + 2

  
  if BoardList.d["cc"] == "O" and BoardList.d["w"] == "O" and BoardList.d["q"] == "O" and BoardList.d["k"] == "O":
    return MyVal + 2

  
  if BoardList.d["e"] == "O" and BoardList.d["k"] == "O" and BoardList.d["q"] == "O" and BoardList.d["w"] == "O":
    return MyVal + 2

  
  if BoardList.d["dd"] == "O" and BoardList.d["x"] == "O" and BoardList.d["r"] == "O" and BoardList.d["l"] == "O":
    return MyVal + 2

  
  if BoardList.d["f"] == "O" and BoardList.d["l"] == "O" and BoardList.d["r"] == "O" and BoardList.d["x"] == "O":
    return MyVal + 2

  if BoardList.d["bb"] == "O" and BoardList.d["aa"] == "O" and BoardList.d["z"] == "O" and BoardList.d["y"] == "O":
    return MyVal + 2

  if BoardList.d["v"] == "O" and BoardList.d["w"] == "O" and BoardList.d["x"] == "O" and BoardList.d["y"] == "O":
    return MyVal + 2

  if BoardList.d["w"] == "O" and BoardList.d["x"] == "O" and BoardList.d["y"] == "O" and BoardList.d["z"] == "O":
    return MyVal + 2

  if BoardList.d["aa"] == "O" and BoardList.d["z"] == "O" and BoardList.d["y"] == "O" and BoardList.d["x"] == "O":
    return MyVal + 1 
    return False

