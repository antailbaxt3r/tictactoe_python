def changeGridO(x, gridLocal):
  if(x == 1):
    gridLocal[0][1] = "*"
    gridLocal[1][0] = "*"
    gridLocal[1][2] = "*"
    gridLocal[2][1] = "*"
    

  if(x == 2):
    gridLocal[0][5] = "*"
    gridLocal[1][4] = "*"
    gridLocal[1][6] = "*"
    gridLocal[2][5] = "*"

  if(x == 3):
    gridLocal[0][9] = "*"
    gridLocal[1][8] = "*"
    gridLocal[1][10] = "*"
    gridLocal[2][9] = "*"

  if(x == 4):
    gridLocal[4][1] = "*"
    gridLocal[5][0] = "*"
    gridLocal[5][2] = "*"
    gridLocal[6][1] = "*"

  if(x == 5):
    gridLocal[4][5] = "*"
    gridLocal[5][4] = "*"
    gridLocal[5][6] = "*"
    gridLocal[6][5] = "*"

  if(x == 6):
    gridLocal[4][9] = "*"
    gridLocal[5][8] = "*"
    gridLocal[5][10] = "*"
    gridLocal[6][9] = "*"

  if(x == 7):
    gridLocal[8][1] = "*"
    gridLocal[9][0] = "*"
    gridLocal[9][2] = "*"
    gridLocal[10][1] = "*"

  if(x == 8):
    gridLocal[8][5] = "*"
    gridLocal[9][4] = "*"
    gridLocal[9][6] = "*"
    gridLocal[10][5] = "*"

  if(x == 9):
    gridLocal[8][9] = "*"
    gridLocal[9][8] = "*"
    gridLocal[9][10] = "*"
    gridLocal[10][9] = "*"