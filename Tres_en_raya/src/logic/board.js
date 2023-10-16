import { WINNER_COMBOS } from "../constants"

export const checkWinnerFrom = (boardToCheck) => {
    // Verificamos las combinaciones ganadoras 
    // Para saber quien es el vencedor
    for (const combo of WINNER_COMBOS){
      const [a,b,c] = combo
      if (
        boardToCheck[a] &&
        boardToCheck[a] === boardToCheck[b] &&
        boardToCheck[a] === boardToCheck[c]
      ){
        return boardToCheck[a]
      }
    }
    // Si no existe un ganador
    return null
  }
export const checkEndGame = (newBoard) =>{
    // Revisamos si ya NO existen espacios vacios
    // y si el resultado fue un empate
    return newBoard.every((Square) => Square !== null)
  }