import './App.css'
import { TwitterFollowCart } from './TwitterFollowCard'

const users = [
    {
        userName: 'midudev',
        name: 'Miguel Ángel Durán',
        isFollowing: true
    },
    {
        userName: 'martindev',
        name: 'Antonio Hermez Perez',
        isFollowing: true
    },
    {
        userName: 'Rubio5',
        name: 'El rubius',
        isFollowing: true
    },
    {
        userName: 'esfera_iphone',
        name: 'Esfera de la fortuna',
        isFollowing: true
    },
    {
        userName: 'AoTJewels',
        name: 'Attack on Titan',
        isFollowing: true
    },
    {
        userName: 'JJKcontents',
        name: 'Jujutsu Kaisen',
        isFollowing: true
    }
]
export function App (){
    return(
        <section className='App'>
           {
           users.map(({userName, name, isFollowing}) =>{
                return(
                    <TwitterFollowCart 
                        key={userName}
                        userName={userName}
                        initialIsFollowing={isFollowing}
                    >    
                        {name}
                    </TwitterFollowCart>
                )
            })
            }
        </section>
    )
}

