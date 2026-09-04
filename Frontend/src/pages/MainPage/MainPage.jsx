import React from 'react'
import { IonIcon } from '@ionic/react'
import { chevronBackOutline, chevronDownOutline } from 'ionicons/icons'
import './MainPage.css'
import img from '../../../public/main.avif'

const MainPage = () => {
  return (
    <>
        <div>
            <div>
                <nav>
                    <div className='logo'>
                        <h1>Smart Arun</h1>
                    </div>
                    <div className='about-page'>
                        <a href="/about">About us</a>
                        <IonIcon icon={chevronDownOutline}/>
                    </div>
                    <div className='links'>
                        <a href="/login">login</a> 
                        <a href="/signup">signup</a>
                    </div>
                </nav>
                <div>
                    <div>
                        <div>
                        <h1>Got Questions About Mangalayatan? Just Ask.</h1>
                    </div>
                    <div>
                        <p>From fee structures to semester circulars, your AI campus companion has the official details ready.</p>
                    </div>
                    </div>
                    <div>
                        <img src={img} alt="main" />
                    </div>
                </div>
            </div>
        </div>
    </>
  )
}

export default MainPage