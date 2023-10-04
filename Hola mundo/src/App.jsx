import './App.css'
import { TwitterFollowCart } from './TwitterFollowCard'

export function App (){
    return(
        <section className='App'>
            <TwitterFollowCart userName="martindev" name="Antonio Hermez Perez" />
            <TwitterFollowCart userName="midudev" name="Miguel Ángel Durán" />
            <TwitterFollowCart userName="Rubio5" name="El rubius" />
            <TwitterFollowCart userName="esfera_iphone" name="Esfera de la fortuna" />
            <TwitterFollowCart userName="AoTJewels" name="Attack on Titan" />
            <TwitterFollowCart userName="JJKcontents" name="Jujutsu Kaisen" />
        </section>
    )
}

