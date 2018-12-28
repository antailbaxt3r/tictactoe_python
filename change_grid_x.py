def changeGridX(x, gridLocal):
  if(x == 1):
    gridLocal[0][0] = "*"
    gridLocal[0][2] = "*"
    gridLocal[1][1] = "*"
    gridLocal[2][0] = "*"
    gridLocal[2][2] = "*"

  if(x == 2):
    gridLocal[0][4] = "*"
    gridLocal[0][6] = "*"
    gridLocal[1][5] = "*"
    gridLocal[2][4] = "*"
    gridLocal[2][6] = "*"

  if(x == 3):
    gridLocal[0][8] = "*"
    gridLocal[0][10] = "*"
    gridLocal[1][9] = "*"
    gridLocal[2][8] = "*"
    gridLocal[2][10] = "*"

  if(x == 4):
    gridLocal[4][0] = "*"
    gridLocal[4][2] = "*"
    gridLocal[5][1] = "*"
    gridLocal[6][0] = "*"
    gridLocal[6][2] = "*"

  if(x == 5):
    gridLocal[4][4] = "*"
    gridLocal[4][6] = "*"
    gridLocal[5][5] = "*"
    gridLocal[6][4] = "*"
    gridLocal[6][6] = "*"

  if(x == 6):
    gridLocal[4][8] = "*"
    gridLocal[4][10] = "*"
    gridLocal[5][9] = "*"
    gridLocal[6][10] = "*"
    gridLocal[6][8] = "*"

  if(x == 7):
    gridLocal[8][0] = "*"
    gridLocal[8][2] = "*"
    gridLocal[9][1] = "*"
    gridLocal[10][0] = "*"
    gridLocal[10][2] = "*"

  if(x == 8):
    gridLocal[8][4] = "*"
    gridLocal[8][6] = "*"
    gridLocal[9][5] = "*"
    gridLocal[10][6] = "*"
    gridLocal[10][4] = "*"

  if(x == 9):
    gridLocal[8][8] = "*"
    gridLocal[8][10] = "*"
    gridLocal[9][9] = "*"
    gridLocal[10][10] = "*"
    gridLocal[10][8] = "*"  