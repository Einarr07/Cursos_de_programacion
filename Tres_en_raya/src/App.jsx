import { useState } from 'react'
import './App.css'
import confetti  from 'canvas-confetti'

import { Square } from './components/Square.jsx'
import { TURNS } from './constants'
import { checkWinnerFrom, checkEndGame } from './logic/board'
import { WinnerModal } from './components/WinnerModal'

function App() {
  const [board, setBoard] = useState(
      Array(9).fill(null)
    )

  const [turn, setTurn] = useState(TURNS.X)
    // null == no hay ganador
    // false == empate
  const [winner, setWinner] = useState(null)

  const resetGame = () =>{
    setBoard(Array(9).fill(null))
    setTurn(TURNS.X)
    setWinner(null)
  }


  const updateBoard = (index) => {
    // Evitamos actualizar si es que el cuadro ya tiene algo
    if (board[index] || winner) return
    // Actualizar el tablero
    const newBoard = [...board]
    newBoard[index] = turn
    setBoard(newBoard)
    // Cambiar el turno
    const newTurn = turn === TURNS.X ? TURNS.O : TURNS.X
    setTurn(newTurn)
    // Verificar si hay un gandor
    const newWinner = checkWinnerFrom(newBoard)
    if(newWinner){
      confetti()
      setWinner(newWinner)
    } else if (checkEndGame(newBoard)){ // Verificar si existe un empate
      setWinner(false)
    }
  }

  return (
  <main className='board'>
    <h1>Tres en raya</h1>
    <button onClick={resetGame}>Resetear el juego</button>
    <section className='game'>
    {
      board.map((_, index) =>{
        return(
          <Square 
            key={index}
            index={index}
            updateBoard={updateBoard}
          >
            {board[index]}
          </Square>
        )
      })
    }
    </section>

    <section className='turn'>
      <Square isSelected={turn === TURNS.X}>
        {TURNS.X}
      </Square>

      <Square isSelected={turn === TURNS.O}>
        {TURNS.O}
      </Square>
    </section>

    <WinnerModal resetGame={resetGame} winner={winner}/>
  </main>
  
  
  )
}

export default App
