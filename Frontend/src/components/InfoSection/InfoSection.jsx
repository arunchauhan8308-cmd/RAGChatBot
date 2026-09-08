import React from 'react'
import MuAi from '../../../src/public/InfoSection/AskMuAi.png'
import MUPortalGuide from '../../../src/public/InfoSection/MuPortalGuide.png'
import MUData from '../../../src/public/InfoSection/MuData.png'

import './InfoSection.css'

const InfoSection = () => {
  return (
    <>
        <div className='images-container'>
            <div className='mu-images'>
                <div>
                    <img src={MuAi} alt="Ask MU AI" />
                </div>
                <div>
                    <h2>
                        Ask MU AI
                    </h2>
                </div>
            </div>
            <div className='mu-images'>
                <div>
                    <img src={MUData} alt="Official MU Data" />
                </div>
                <div>
                    <h2>
                        Official MU Data
                    </h2>
                </div>
            </div>
            <div className='mu-images'>
                <div>
                    <img src={MUPortalGuide} alt="24/7 MU Portal Guide" />
                </div>
                <div>
                    <h2>
                        24/7 MU Portal Guide
                    </h2>
                </div>
            </div>
        </div>
    </>
  )
}

export default InfoSection